from typing import AsyncIterator


class TTSService:
    """Placeholder text-to-speech service."""

    async def synthesize_stream(self, text: str) -> AsyncIterator[bytes]:
        """Yield audio chunks for the given text."""
        # TODO: integrate real TTS engine
        yield b""
