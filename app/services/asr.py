from typing import Optional


class ASRService:
    """Placeholder ASR service."""

    async def transcribe_chunk(self, audio: bytes) -> Optional[str]:
        """Transcribe a chunk of audio. Returns partial transcript if available."""
        # TODO: integrate real ASR engine
        return None

    def is_end_of_utterance(self, audio: bytes) -> bool:
        """Detect end of utterance. Placeholder implementation."""
        return False
