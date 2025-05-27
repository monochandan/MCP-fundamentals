#from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

load_dotenv()

#mcp = FastMCP("Github API")

# print(github_token)
# code : https://huggingface.co/learn/mcp-course/unit1/mcp-clients  
def make_github_request():
    github_token = os.environ.get("GUTHUB_TOKEN")
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable is not set.")
    else:
        headers = {"Authorization": f"Bearer {github_token}"}
        print(headers)
    return 0

if __name__ == "__main__":
    make_github_request()