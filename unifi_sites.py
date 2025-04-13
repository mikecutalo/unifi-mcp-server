import json
from unifi import mcp, make_unifi_request

@mcp.tool()
async def get_unifi_sites() -> str:
    """Get a list of all unifi sites that this api key has access to.
    """
    data = await make_unifi_request("v1/sites")
    if not data["data"]:
        return "No sites found"

    return json.dumps(data["data"])
