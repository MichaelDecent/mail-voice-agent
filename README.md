# Mail Voice Agent

This project contains a FastAPI backend for a voice-controlled email assistant. It demonstrates streaming audio input and output, placeholder integrations for ASR/LLM/TTS, and OAuth2 based authentication.

## Running

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
```

Start the server:

```bash
uvicorn app.main:app --reload
```

The `/voice/stream` websocket accepts audio chunks and streams synthesized audio responses.
