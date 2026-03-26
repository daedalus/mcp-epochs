import time
from typing import Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-epochs", json_response=True)


@mcp.tool(
    name="get_unix_time",
    description="Get the current Unix timestamp in seconds and milliseconds",
)
def get_unix_time() -> dict[str, Any]:
    """Get the current Unix timestamp."""
    now = time.time()
    return {
        "unix_time": int(now),
        "unix_time_ms": int(now * 1000),
        "iso8601": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
    }


def run_server() -> int:
    """Run the MCP server with stdio transport."""
    mcp.run(transport="stdio")
    return 0
