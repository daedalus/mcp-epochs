# SPEC.md — mcp-epochs

## Purpose
An MCP (Model Context Protocol) server tool that provides the current Unix timestamp (epochs) to LLMs, giving them awareness of time.

## Scope
- **In scope:**
  - Single MCP tool that returns current Unix timestamp in seconds (and optionally milliseconds)
  - STDIO transport for MCP protocol
- **Not in scope:**
  - Timezone conversions (returns UTC)
  - Historical timestamps
  - Date formatting

## Public API / Interface

### MCP Tool: `get_unix_time`
Returns the current Unix timestamp.

**Parameters:** None

**Returns:**
- `unix_time` (int): Current Unix timestamp in seconds
- `unix_time_ms` (int): Current Unix timestamp in milliseconds
- `iso8601` (str): Current time in ISO 8601 format

**Error Behavior:** None (no error conditions for simple time fetch)

## Edge Cases
1. System clock is set to epoch (1970-01-01) - returns 0
2. System clock is far in the future (year 9999) - returns large positive integer
3. Multiple rapid calls - each returns slightly different time
4. System leap second - handled by underlying time library
5. Negative timestamps (before 1970) - not possible on standard systems

## Performance & Constraints
- O(1) operation, no memory allocation
- Pure stdlib, no external dependencies for core functionality
- Python 3.11+ required
