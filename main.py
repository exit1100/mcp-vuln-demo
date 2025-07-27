from mcp.server.fastmcp import FastMCP # Parameter is not strictly needed now, but good practice to keep if you add more complex params later
import random

# Create the FastMCP instance with stdio transport
mcp = FastMCP("mcp-vuln-demo")

# Define the tool using the @mcp.tool() decorator
@mcp.tool()
def get_weather(city: str) -> str:
    """
    Returns weather of the city

    :param city: The city to get the weather for
    """
    weather_status = ["맑음 ☀️", "흐림 ☁️", "비 🌧️", "눈 ❄️", "안개 🌫️", "태풍 🌀"]
    wind_directions = ["북풍", "남풍", "동풍", "서풍", "북동풍", "남서풍"]

    temperature = random.randint(-10, 40)        # °C
    humidity = random.randint(30, 90)            # %
    wind = random.choice(wind_directions)
    condition = random.choice(weather_status)

    return (
        f"{city}의 날씨 정보입니다.\n"
        f"🌡️ 기온: {temperature}°C\n"
        f"💧 습도: {humidity}%\n"
        f"🌬️ 바람: {wind} 방향\n"
        f"🌥️ 상태: {condition}"
    )

# Run the server if the script is executed directly
if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="stdio")