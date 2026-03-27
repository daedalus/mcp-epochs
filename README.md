# mcp-epochs

mcp-name: io.github.daedalus/mcp-epochs

> MCP tool that provides current Unix timestamp (epochs) to LLMs.

[![PyPI](https://img.shields.io/pypi/v/mcp-epochs.svg)](https://pypi.org/project/mcp-epochs/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-epochs.svg)](https://pypi.org/project/mcp-epochs/)
[![Coverage](https://codecov.io/gh/daedalus/mcp-epochs/branch/master/graph/badge.svg)](https://codecov.io/gh/daedalus/mcp-epochs)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Install

```bash
pip install mcp-epochs
```

## Usage

```bash
mcp-epochs
```

This runs the MCP server with STDIO transport. The server provides a `get_unix_time` tool.

## MCP Configuration

```json
{
  "mcpServers": {
    "mcp-epochs": {
      "command": "mcp-epochs"
    }
  }
}
```

## Development

```bash
git clone https://github.com/daedalus/mcp-epochs.git
cd mcp-epochs
pip install -e ".[test]"

# run tests
pytest

# format
ruff format src/ tests/

# lint
ruff check src/ tests/

# type check
mypy src/
```

## API

### `get_unix_time()`

Returns the current Unix timestamp as a dictionary with the following keys:

- `unix_time` (int): Current Unix timestamp in seconds since epoch.
- `unix_time_ms` (int): Current Unix timestamp in milliseconds since epoch.
- `iso8601` (str): Current UTC time in ISO 8601 format (e.g., "2026-03-26T21:30:00Z").

### `run_server()`

Starts the MCP server using STDIO transport for local desktop MCP clients.
