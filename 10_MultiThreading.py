import time
import random
from concurrent.futures import ThreadPoolExecutor  # Used to run multiple tasks concurrently

tables = ['order', 'customer', 'sale']


def time_taken(i):
    # Generate a random waiting time between 1 and 10 seconds
    wait = random.randint(1, 10)

    # Simulate some work by making the program wait
    time.sleep(wait)

    # Print which table completed and how long it took
    print(f'I am {i} - took = {wait} seconds')


print('---------------------------without multithreading--------------------------')

# Without multithreading:
# The loop runs one table at a time.
# It waits for the first table to finish before starting the next table.
for i in tables:
    time_taken(i)


print('---------------------------with multithreading-----------------------------')

# With multithreading:
# ThreadPoolExecutor creates multiple threads so that tasks can run concurrently.
#
# max_workers = len(tables)
# Since we have 3 tables, 3 worker threads will be created.
with ThreadPoolExecutor(max_workers=len(tables)) as executor:

    # executor.map() sends each table to the time_taken() function.
    # The three tasks can run concurrently instead of waiting for each other.
    executor.map(time_taken, tables)

# Important:
# Without multithreading:
#     order -> wait -> customer -> wait -> sale -> wait
#
# With multithreading:
#     order    \
#     customer  |--> run concurrently
#     sale     /
#
# Therefore, the total execution time with multithreading can be much lower
# when the tasks spend time waiting (for example, I/O, API calls, database calls, etc.).

