import json
from unifi import mcp, make_unifi_request


@mcp.tool()
async def list_unifi_devices(site_id: str, offset:int =0, limit:int=25) -> str:
    """List adopted devices of a site (paginated). 
    Response contains basic information about site's adopted devices.

    Args:
        site_id (str): The site id to get devices for
    """

    path = f"v1/sites/{site_id}/devices?offset={offset}&limit={limit}"
    data = await make_unifi_request(path)

    if not data["data"]:
        return "No devices found"

    # TODO (mikecutalo): fix output format
    return json.dumps(data["data"])


@mcp.tool()
async def get_device_details(site_id: str, device_id: str) -> str:
    """Get detailed information about a specific adopted device.
    Response includes more information about a single device,
    as well as more detailed information about device features,
    such as switch ports and/or access point radios

    Args:
        site_id (str): The site id to get clients for
        device_id (str): The id of the device to get details for
    """

    path = f"v1/sites/{site_id}/devices/{device_id}"
    data = await make_unifi_request(path)

    # TODO (mikecutalo): fix output format
    return json.dumps(data)


@mcp.tool()
async def get_device_statistics(site_id: str, device_id: str) -> str:
    """Get latest (live) statistics of a specific adopted device.
    Response contains latest readings from a single device,
    such as CPU and memory utilization, uptime, uplink tx/rx rates etc

    Args:
        site_id (str): The site id to get clients for
        device_id (str): The id of the device to get statistics for
    """

    path = f"v1/sites/{site_id}/devices/{device_id}/statistics/latest"
    data = await make_unifi_request(path)

    # TODO (mikecutalo): fix output format
    return json.dumps(data)
