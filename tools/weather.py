import asyncio
import python_weather


async def get_weather_() -> int:
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('New York')
        return weather.temperature

def get_weather():
    temp = asyncio.run(get_weather_())
    return temp

if __name__ == '__main__':
    temp = asyncio.run(get_weather_())
    print(f"Η θερμοκρασία είναι: {temp}°F")