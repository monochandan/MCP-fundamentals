from fastmcp import Client
import asyncio
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

async def interect_with_server():
    print("-- Creating Client--")

    client = Client(r"my_server.py")

    # client = Client("http://localhpost:8080")

    #print(f"Client configured to connect to: {client.target}")

    try:
        async with client:
            print("--clinet connected--")
            greet_result = await client.call_tool("greet", {"name": "Remote Client"})
            print(f"Greet Result: {greet_result}")

            add_result = await client.call_tool("add", {"a": 5, "b": 10})
            print(f"Add Result: {add_result}")

            config_data = await client.read_resource("data://config")
            print(f"Config Resource: {config_data}")

            user_profile = await client.read_resource("users://102/profile")
            print(f"User 101 Profile: {user_profile}")
    except Exception as e:
        print(f"an errro occured: {e}")
    
    finally:
        print("-- client interaction finiched --")
    
if __name__ == "__main__":
    asyncio.run(interect_with_server())
    # print("Client interaction completed.")

