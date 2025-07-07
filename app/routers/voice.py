from fastapi import APIRouter, WebSocket, Depends
from fastapi.websockets import WebSocketDisconnect
from typing import AsyncIterator

from app.services.asr import ASRService
from app.services.llm import LLMService
from app.services.tts import TTSService
from app.services.mcp_client import MCPClient
from app.security.auth import oauth2_scheme, verify_token

router = APIRouter()

asr_service = ASRService()
llm_service = LLMService()
tts_service = TTSService()
mcp_client = MCPClient()


async def stream_tts(text: str) -> AsyncIterator[bytes]:
    async for chunk in tts_service.synthesize_stream(text):
        yield chunk


@router.websocket("/stream")
async def voice_stream(websocket: WebSocket, token: str = Depends(oauth2_scheme)):
    await verify_token(token)
    await websocket.accept()

    transcript = ""
    try:
        async for audio_chunk in websocket.iter_bytes():
            partial = await asr_service.transcribe_chunk(audio_chunk)
            if partial:
                transcript += partial
            if asr_service.is_end_of_utterance(audio_chunk):
                response_text = await llm_service.handle_transcript(
                    transcript, mcp_client
                )
                async for audio_response in stream_tts(response_text):
                    await websocket.send_bytes(audio_response)
                transcript = ""
    except WebSocketDisconnect:
        await websocket.close()
