import json
from unifi import mcp, make_unifi_request


@mcp.tool()
async def get_connected_clients(site_id: str, filter: str = "", offset: int = 0, limit: int = 25) -> str:
    """List connected clients of a site (paginated).
    Clients are either physical devices (computers, smartphones, connected by wire or wirelessly),
    or active VPN connections.

    Args:
        site_id (str): The site id to get clients for
        offset (int): The offset to start at
        limit (int): The maximum number of clients to return
        filter (str): The filter to apply to the request
            Filter properties:
            Name                Type	  Allowed functions
            id                  UUID	  eq ne in notIn
            type                STRING	  eq ne in notIn
            macAddress          STRING	  isNull isNotNull eq ne in notIn
            ipAddress           STRING	  isNull isNotNull eq ne in notIn
            connectedAt         TIMESTAMP isNull isNotNull eq ne gt ge lt le
            access.type         STRING	  eq ne in notIn
            access.authorized   BOOLEAN	  isNull isNotNull eq ne
    """

    # TODO (mikecutalo): work on the filter examples
    path = f"v1/sites/{site_id}/clients?offset={offset}&limit={limit}"
    data = await make_unifi_request(path)

    if not data["data"]:
        return "No devices found"

    # TODO (mikecutalo): fix output format
    return json.dumps(data["data"])

@mcp.tool()
async def get_connected_client_details(site_id: str, client_id: str) -> str:
    """Get details of a specific connected client,
    such as its IP and MAC addresses, and other properties.

    Args:
        site_id (str): The site id to get clients for
        client_id (str): The id of the client to get details for
    """

    path = f"v1/sites/{site_id}/clients/{client_id}"
    data = await make_unifi_request(path)

    # TODO (mikecutalo): fix output format
    return json.dumps(data)
