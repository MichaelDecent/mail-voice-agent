from app.services.mcp_client import MCPClient


class LLMService:
    """Placeholder LLM service with function-calling enabled."""

    async def handle_transcript(self, transcript: str, mcp_client: MCPClient) -> str:
        """Send transcript to LLM, call MCP functions as needed, and return response text."""
        # TODO: integrate actual LLM with function calling
        return "This is a placeholder response."
