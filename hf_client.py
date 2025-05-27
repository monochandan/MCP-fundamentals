# https://huggingface.co/docs/smolagents/en/installation

from mcp.client.stdio import StdioServerParameters
from smolagents import ToolCollection
from smolagents.mcp_client import MCPClient
import asyncio
import warnings
import os
from fastmcp import Client
from smolagents import CodeAgent, InferenceClientModel
# from smolagents.mcp_client import MCP
# server_parameters = StdioServerParameters(command ="uv", args=["run", "hf_server.py"])

# try:
# from the hf_server.py file, we can create a client that connects to the server and retrieves the tools.
# async def main():
#     server_path = os.path.abspath("hf_server.py")
#     async with Client(server_path) as client:
#         tools = await client.list_tools()
#         # print(tools)
#         print("\n".join(f"{tool.name}: {tool.description}"for tool in tools))

# https://huggingface.co/learn/mcp-course/unit1/mcp-clients   
# with ToolCollection.from_mcp(
# server_parameters,
# trust_remote_code = True
# )as tools:
#     print("\n".join(f"{tool.name}: {tool.description}" for tool in tools.tools))


# with MCPClient(
#     {"url": "https://abidlabs-mcp-tools.hf.space/mcp/sse",
#      "transport": "sse"}
# )as tools:
#     print("\n".join(f"{t.name}: {t.description}") for t in tools)

# async def main():
#     server_path = {"url": "file:///C:/Users/looka/OneDrive/Documents/Thesis/RAG_MCP/my.html"
#                    , "transport": "sse"}
#     async with MCPClient(server_path) as client:
#         tools = await tools.list_tools()
#         print(tools)

# if __name__ == "__main__":
#     asyncio.run(main())
    # asyncio.get_event_loop().run_until_complete(main())
    # asyncio.get_event_loop().close()




# model = InferenceClientModel()

# server_parameters = StdioServerParameters(command ="uv", args=["run", "hf_server.py"])
# # agent = CodeAgent(tools=[], model=model, add_base_tools=True)

# with ToolCollection.from_mcp(
#     server_parameters, 
#     trust_remote_code=True
# )as tool_collection:
#     agent = CodeAgent(tools = [*tool_collection.tools], model=model)
#     agent.run("What is the weather in Trier, Germany now?")


# connecting to mcp package
server_parameters = StdioServerParameters(
    command="uv",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},

)

with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tools_collection:
    # model = InferenceClientModel()
    agent = CodeAgent(tools=[*tools_collection.tools], add_base_tools=True)
    agent.run("Please find a remedy for hangover")
