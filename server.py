'''
add resources to the MCP server
'''
import aiosqlite
from fastmcp import FastMCP
from typing import List, Dict, Optional

import asyncio

import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# https://gofastmcp.com/servers/fastmcp
mcp = FastMCP("Employee MCP server")

db_path = "my_db/employees.db"

# async -  defines a function that runs asynchronously (non-blocking).

# await -  pauses the function until the async task completes (e.g., database call, API request).

# They let the  code handle I/O operations efficiently without freezing the app

# https://gofastmcp.com/servers/resources
@mcp.resource("employees://all") # read only acces to the data for the LLM or client application
async def get_all_employees() -> List[Dict]:
    """Returns all employees records as a list of dictionaries. """
    # https://pypi.org/project/aiosqlite/
    async with aiosqlite.connect(db_path) as db_conn:
        cursor = await db_conn.execute("SELECT * from employees")
        columns = [column[0] for column in cursor.description] # every tuples 0th index is the column name
        # row = await cursor.fetchone()
        print(cursor) # an object
        # print(row[0])
        # print('hello')
        # for i in row:
        #     print(i)
        #print(cursor.description)
        # async for row in cursor: # (1, 'water', 'vap', 'wv@gmail.com', 85000.0, '2033-10-01')
        #     print(row)
        employees = [dict(zip(columns, row)) async for row in cursor]
        print(employees)
        await cursor.close()
    return employees
        #print(columns)
    
@mcp.resource("employees://{employee_id}") # read only access to data sources
async def get_employee_by_id(employee_id: int) -> Optional[Dict]:
    """Return an employee by his or her ID"""
    async with aiosqlite.connect(db_path) as conn:
        cursor = await conn.execute("SELECT * FROM employees where id = ?", (employee_id,))
        row = await cursor.fetchone()

        if row:
            columns = [column[0] for column in cursor.description]
            result = dict(zip(columns, row))
            # print(result)
        else:
            result = None
        await cursor.close()
    return result

@mcp.tool() # actions that the AI model can invoke through the MCP protocol
async def delete_employee(employee_id: int) -> bool:
    """Delete employee record based on employee ID. Return True id successfull. """
    async with aiosqlite.connect(db_path) as conn:
        try:
            cursor = await conn.execute("DELETE FROM employees WHERE id  = ?", (employee_id,))
            await conn.commit(conn)
            success = cursor.rowcount ; 0 # if rowcount is 0, then no record was deleted
            await cursor.close()

        except Exception as e:
            success = False
        return success
    
# async def main():
#     # connect to the server via stdio (by running server.py as a sub process)
#     async with Client("server.py") as client:
#         print("Listing resources:")
#         resources = await client.list_resources()
#         print(resources)

#         print('\nlisting tools:')
#         tools = await client.list_tools()
#         print(tools)
    
if __name__ == "__main__":
    mcp.run(transport="stdio") # resources and tools availiable to the clients. Using stdio transport for simplicity.
    

# mcp 1.9.1
# fastmcp 2.5.0