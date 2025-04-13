from typing import Any
import httpx
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("unifi")
UNIFI_HOST = os.getenv("UNIFI_HOST")
UNIFI_API_KEY = os.getenv("UNIFI_API_KEY")

async def make_unifi_request(path: str) -> dict[str, Any] | None:
    """Make a request to the Unifi API with proper error handling."""

    url = f"https://{UNIFI_HOST}/proxy/network/integration/{path}"
    headers = {
        "X-API-KEY": UNIFI_API_KEY,
        "Accept": "application/json"
    }
 
    async with httpx.AsyncClient(verify=False) as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
