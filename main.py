from mcp.server.fastmcp import FastMCP 
import random


mcp = FastMCP("mcp-vuln-demo")

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

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="stdio")