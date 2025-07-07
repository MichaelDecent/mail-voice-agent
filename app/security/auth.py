from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer

# OAuth2 settings - normally configured with real authorization server
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://auth.example.com/authorize",
    tokenUrl="https://auth.example.com/token",
)


async def verify_token(token: str = Depends(oauth2_scheme)) -> None:
    """Verify the OAuth2 token. Placeholder for real verification."""
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    # TODO: implement real token verification and session management
