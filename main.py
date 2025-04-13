from unifi import mcp
import unifi_sites
import unifi_clients
import unifi_devices


# TODO(mikecutalo): refactor project structure
if __name__ == "__main__":
    mcp.run(transport='stdio')
