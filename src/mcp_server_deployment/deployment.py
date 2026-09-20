from mcp.server.mcpserver import MCPServer

mcp = MCPServer("mcp-server-deployment")


@mcp.tool()
def hello(name: str) -> str:
    """Say hello to someone.

    Args:
        name: The name to greet
    """
    return f"Hello, {name}!"


def main():
    mcp.run()
