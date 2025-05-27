from fastmcp import FastMCP, Client
import asyncio ## need for the cient
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
mcp = FastMCP("My MCP Server")

print("FastMCP server object created")

@mcp.tool()
def greet(name: str)-> str:
    """Return a simple greetings"""
    return f"Hello, {name}"

@mcp.tool()
def add(a: int, b:int) -> int:
    """Add this two number"""
    return a + b 
print("Tools greet and add  are added") 


APP_CONFIG = {"theme": "dark", "version":"1.1", "feature_flags": ["new_dashboard"]}

@mcp.resource("data://config")
def get_config() -> dict:
    """Provide the application """
    return APP_CONFIG

print("Resource 'data://config' added")

USER_PROFILES = {
    101: {"name": "Alice", "status": "active"},
    102: {"name": "Bob", "status": "inactive"},
}

@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieve an users profile by the user ID."""
    return USER_PROFILES.get(user_id, {"error": "User not found"})

print("Resource template 'users://{user_id}/profile' added.")


@mcp.prompt("summarize")
async def summarize_prompt(text: str) -> list[dict]:
    """Generate a prompt to summarize the provided text."""
    return [
        {"role": "system", "content": "You are a helpful assistant skilled at summarization."},
        {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
    ]
print("Prompt 'summarize' added.")



# testing the server locally
async def test_server_locally():
    print("\n Testing server locally")
    client = Client(mcp)

    async with client:
        greet_result = await client.call_tool("greet", {"name": "FastMCP User"})
        print(f"Greet Result: {greet_result}")

        add_result = await client.call_tool("add", {"a":5, "b":10})
        print(f"Add result: {add_result}")

        config_data = await client.read_resource("data://config")
        print(f"Config resource: {config_data}")

        user_profile = await client.read_resource("users://101/profile")
        print(f"User 101 profile: {user_profile}")

        prompt_mssg = await client.get_prompt("summarize", {"text": "This is some text"})
        print(f"Prompt message: {prompt_mssg}")


if __name__ == "__main__":
    # print("Starting FastMCP server...")
    # print("\n Starting the server via __main__")
    mcp.run(transport="stdio")  # This will start the server and block the thread
    # print("FastMCP server is running...")
    #asyncio.run(test_server_locally())