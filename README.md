# mcp-epochs

> MCP tool that provides current Unix timestamp (epochs) to LLMs.

[![PyPI](https://img.shields.io/pypi/v/mcp-epochs.svg)](https://pypi.org/project/mcp-epochs/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-epochs.svg)](https://pypi.org/project/mcp-epochs/)
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
git clone https://github.com/dclavijo/mcp-epochs.git
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
