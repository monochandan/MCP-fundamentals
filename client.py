import asyncio
from fastmcp import Client
import os

import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
async def main():
    # Connect to the server via stdio (by running server.py as a sub process)
    server_path = os.path.abspath("server.py")
    async with Client(server_path) as client:
        print("Listing Resources: ")
        resources = await client.list_resources()
        print(resources)

        print("\nListing tools:")
        tools = await client.list_tools()
        print(tools)

if __name__ == "__main__":
    asyncio.run(main())