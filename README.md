# a3

**Question 1: Explain the advantages of using asynchronous programming in this context. Why is it better than using a traditional blocking approach?**

Asynchronous programming allows the client to continue working after a request has been sent. This is better than traditional blocking, where the client stops working until it receives a response, because after the client is fetching weather data about one city, they are able to fetch for other cities as well, rather than sequentially doing one city at a time. In other words, if the client fetches data about one city, they are able to complete other tasks in the time it takes for a response. This allows for the application to handle multiple requests seamlessly. 

**Question 2: Describe how asynchronous functions are used in your script. What roles do async def , await , and asyncio play in managing concurrent tasks?**

Firstly, “async def” defines an asynchronous function, meaning it will send requests without pausing the program. Next, “await” holds only the “get_weather” function, until a response is received. Next, “async with aiohttp.ClientSession() as session” creates a session in order to efficiently handle the HTTP connection. Lastly, “asyncio.run(get_weather(city_name))” starts an event loop that runs “get_weather” until it is completed. 

**A short explanation of how the program works.**
