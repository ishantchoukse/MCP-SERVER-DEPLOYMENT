# MCP Server Deployment

A simple MCP (Model Context Protocol) server implementation with an addition tool.

## Installation

```bash
uv sync
```

## Usage

### Running the server

```bash
uv run mcp-server-deployment
```

Or run as a module:

```bash
uv run python -m mcp_server_deployment
```

### Available Tools

#### `add_two_number`

Add two numbers together.

**Parameters:**
- `first_number` (int): First number to add
- `second_number` (int): Second number to add

**Returns:** int - The sum of the two numbers

**Example:**
```
add_two_number(5, 3) -> 8
```

## Development

### Requirements

- Python >= 3.14
- uv package manager

### Project Structure

```
src/mcp_server_deployment/
├── __init__.py
├── __main__.py
└── deployment.py    # Main server implementation
```

## License

MIT
