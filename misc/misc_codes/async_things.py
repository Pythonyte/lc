import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    # You can share the session across all tasks, so the session is created here as a context manager.
    # The tasks can share the session because they are all running on the same thread.
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            # it creates a list of tasks using asyncio.ensure_future(), which also takes care of starting them
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        # asyncio.gather() to keep the session context alive until all of the tasks have completed
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


"""
Warnings:
Another, more subtle, issue is that all of the advantages of cooperative multitasking get thrown away if one of the tasks doesn’t cooperate. A minor mistake in code can cause a task to run off and hold the processor for a long time, starving other tasks that need running. There is no way for the event loop to break in if a task does not hand control back to it.
"""