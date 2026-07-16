"""
Kata 4 - Context manager
Write a context manager that times a block of code and prints the
elapsed time on exit, even if the code inside raises an exception.
Two versions: class-based (__enter__/__exit__) and function-based
(@contextlib.contextmanager)
"""

import time
from contextlib import contextmanager


# Version A: class-based 

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start
        print(f"[Timer] Elapsed: {elapsed:.4f}s")
        # Returning False (or None) means: don't suppress the
        # exception - let it propagate normally after cleanup runs.
        return False


# Version B: @contextmanager (function-based)

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        # This runs whether or not the block raised - same guarantee
        # __exit__ gives above, and the same guarantee Monday's
        # `with open(...)` relies on
        elapsed = time.time() - start
        print(f"[timer] Elapsed: {elapsed:.4f}s")


if __name__ == "__main__":
    print("<--- class-based, no exception --->")
    with Timer():
        time.sleep(0.2)

    print("<--- class-based, with exception --->")
    try:
        with Timer():
            time.sleep(0.1)
            raise ValueError("boom")
    except ValueError as e:
        print(f"Caught after cleanup: {e}")

    print("<--- function-based, no exception --->")
    with timer():
        time.sleep(0.2)

    print("<--- function-based, with exception --->")
    try:
        with timer():
            time.sleep(0.1)
            raise ValueError("boom")
    except ValueError as e:
        print(f"Caught after cleanup: {e}")
