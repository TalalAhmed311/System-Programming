import asyncio
import aiohttp
import time
import concurrent



## Synchronous HTTP client with a single thread

def run(num_requests):
    for _ in range(num_requests):
        time.sleep(0.5)


start = time.time()
run(100)
total_time = time.time() - start

print(f"Synchronous Single-Thread: {total_time}")



## Synchronous HTTP client with multiprocessing

def _make_request(paylod):
    time.sleep(0.5)

def run(num_requests):
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(_make_request, {}) for _ in range(num_requests)]
        concurrent.futures.wait(futures)

start = time.time()
run(100)
total_time = time.time() - start

print(f"Synchronous Multi-Processing: {total_time}")


## Synchronous HTTP client with Threading

def _make_request(paylod):
    time.sleep(0.5)

def run(num_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(_make_request, {}) for _ in range(num_requests)]
        concurrent.futures.wait(futures)


start = time.time()
run(100)
total_time = time.time() - start

print(f"Synchronous Multi-threading: {total_time}")


# ## Asynchronous HTTP client with asyncio

async def _make_request(session):
     await asyncio.sleep(0.5)

async def _run(num_requests):
      async with aiohttp.ClientSession() as session:
            tasks = [_make_request(session) for _ in range(num_requests)]
            await asyncio.gather(*tasks)
     

def run(num_requests):
     asyncio.run(_run(num_requests))


start = time.time()
run(10000)
total_time = time.time() - start

print(f"Async with asyncio: {total_time}")




## Asynchronous HTTP client with multiprocessing


async def _make_request(sessios):
    await asyncio.sleep(0.5)
    
async def _run(num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [_make_request(session) for i in range(num_requests)]
        await asyncio.gather(*tasks)

def _run_job(num_requests):
    asyncio.run(_run(num_requests))


def run(num_requests):
    num_jobs = 6  # Number of callables (jobs) we want to submit to the ProcessPoolExecutor
    num_requests_per_job = num_requests // num_jobs
    remainder_requests = num_requests % num_jobs

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_jobs+1) as executor:
        futures = [executor.submit(_run_job, num_requests_per_job) for _ in range(num_jobs)]

        if remainder_requests:
            futures.append(executor.submit(_run_job,remainder_requests))

        concurrent.futures.wait(futures)


start = time.time()
run(10000)
total_time = time.time() - start
print(f"Async with Multi-Processing: {total_time}")



## Asynchronous HTTP client with multithreading

async def _make_request(sessios):
     await asyncio.sleep(0.5)
     
async def _run(num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [_make_request(session) for _ in range(num_requests)]
        await asyncio.gather(*tasks)

def _run_job( num_requests):
    asyncio.run(_run(num_requests))


def run(num_requests):
    num_jobs = 6  # Number of callables (jobs) we want to submit to the ProcessPoolExecutor
    num_requests_per_job = num_requests // num_jobs
    remainder_requests = num_requests % num_jobs

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_jobs+1) as executor:
        futures = [executor.submit(_run_job, num_requests_per_job) for _ in range(num_jobs)]

        if remainder_requests:
            futures.append(executor.submit(_run_job,remainder_requests))

        concurrent.futures.wait(futures)


start = time.time()
run(10000)
total_time = time.time() - start

print(f"Async with Multi-threading: {total_time}")
