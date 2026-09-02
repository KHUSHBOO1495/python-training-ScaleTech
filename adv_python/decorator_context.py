import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper


class DatabaseConnection:

    def __enter__(self):
        print("Database connection opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database connection closed")


@timer
def process_data():

    with DatabaseConnection():
        print("Processing data...")
        time.sleep(2)

process_data()
