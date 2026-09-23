from mcp.server.mcpserver import MCPServer

mcp=MCPServer("Demo")

@mcp.tool()
def add_two_number(first_number:int,second_number:int) -> int:
    """
    Add two numbers
    args:
        first_number: type integer
        second_number: type integer
    returns:
        int: addition result
    """

    return first_number+second_number

