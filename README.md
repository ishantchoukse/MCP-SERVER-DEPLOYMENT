# MCP Server Deployment

A simple MCP (Model Context Protocol) server implementation with a hello tool.

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

#### `hello`

Say hello to someone.

**Parameters:**
- `name` (string): The name to greet

**Example:**
```
hello("World") -> "Hello, World!"
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
