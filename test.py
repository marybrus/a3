import asyncio
import aiohttp
import random
import time
from datetime import datetime

Cities = ["London", "New York", "Tokyo", "Paris", "São Paulo"]
Rounds = 10
Output = "weather_log.txt"

async def get_weather(city, queue):
    # This function fetches weather data
    url = f"https://wttr.in/{city}?format=j1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            current = data['current_condition'][0]
            temp_c = current['temp_C']
            humidity = current['humidity']
            desc = current['weatherDesc'][0]['value']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            weather_info = f"{timestamp} - {city}: {temp_c}°C, {humidity}% humidity, {desc}"
            await queue.put(weather_info)

async def log_weather(queue):
    # This function logs the output into the file "Output"
    with open(Output, "a") as file:
        while True:
            weather_info = await queue.get()
            file.write(weather_info + "\n")
            print(weather_info)  
            queue.task_done()

async def main():
    # This it the main function that gets data once every second for 10 seconds
    # for the given cities and logs them
    queue = asyncio.Queue()
    
    consumer_task = asyncio.create_task(log_weather(queue))

    for round_num in range(Rounds):
        print(f"--- Round {round_num + 1} ---")
        producer_tasks = [get_weather(city, queue) for city in Cities]
        await asyncio.gather(*producer_tasks) 
        await asyncio.sleep(random.uniform(1, 3))

    await queue.join() 
    consumer_task.cancel()  

if __name__ == "__main__":
    asyncio.run(main())
