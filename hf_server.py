from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """ Get the curret weather for a specified location."""
    return f"Weather in {location}: Cloudy, -10°C"

@mcp.tool()
def get_time(location: str) -> str:
    """ Get the current time for a specified location. """
    return f"Current time of the {location}: 10 at the morning"

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as aresource. """
    return f"Weather data for {location}: Cloudy, -10°C"

@mcp.prompt()
def weather_report(location: str) -> str:
    """ Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""


if __name__ == "__main__":
    mcp.run()


