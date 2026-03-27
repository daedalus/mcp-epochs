import time
from typing import Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-epochs", json_response=True)


@mcp.tool(
    name="get_unix_time",
    description="Get the current Unix timestamp in seconds and milliseconds",
)
def get_unix_time() -> dict[str, Any]:
    """Get the current Unix timestamp.

    Returns the current time as a Unix timestamp (seconds since 1970-01-01 00:00:00 UTC),
    along with millisecond precision and ISO 8601 formatted string.

    Args:
        None. This function takes no arguments.

    Returns:
        dict[str, Any]: A dictionary containing:
            - unix_time (int): Current Unix timestamp in seconds since epoch.
            - unix_time_ms (int): Current Unix timestamp in milliseconds since epoch.
            - iso8601 (str): Current UTC time in ISO 8601 format (e.g., "2026-03-26T21:30:00Z").

    Raises:
        None. This function does not raise any exceptions.

    Examples:
        >>> result = get_unix_time()
        >>> isinstance(result["unix_time"], int)
        True
        >>> result["unix_time"] > 0
        True
    """
    now = time.time()
    return {
        "unix_time": int(now),
        "unix_time_ms": int(now * 1000),
        "iso8601": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
    }


def run_server() -> int:
    """Run the MCP server with stdio transport.

    Starts the MCP server using STDIO transport, which is the standard
    transport for local desktop MCP clients like Claude Desktop or Cursor.

    Args:
        None.

    Returns:
        int: Returns 0 on normal exit.

    Raises:
        KeyboardInterrupt: Raised when the server is interrupted by the user.
        SystemExit: Raised when the server process terminates.
    """
    mcp.run(transport="stdio")
    return 0
