"""
Kata 1 - Warm-up
Redo yesterday's two fixes: the mutable default argument
(cache) bug, and the bare-except fix.
"""


# Fix 1: Mutable default argument bug

def add_item_buggy(item, cache={}):
    """
    BUGGY VERSION - do not use.
    The {} default is created ONCE at function definition time and
    shared across every call that doesn't pass its own cache.
    """
    cache[item] = True
    return cache


def add_item_fixed(item, cache=None):
    """
    FIXED VERSION.
    Use None as the default, and create a fresh dict inside the
    function body if the caller didn't pass one.
    """
    if cache is None:
        cache = {}
    cache[item] = True
    return cache


# Fix 2: Bare except 

def parse_number_buggy(user_input):
    """
    BUGGY VERSION - do not use.
    A bare except catches everything, including KeyboardInterrupt
    and real bugs, hiding what actually went wrong.
    """
    try:
        return int(user_input)
    except:
        print("Something went wrong")
        return None


def parse_number_fixed(user_input):
    """
    FIXED VERSION.
    Catch the specific exception we expect (ValueError) and nothing else.
    """
    try:
        return int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        return None


if __name__ == "__main__":

    print(add_item_fixed("apple"))          # {'apple': True}
    print(add_item_fixed("banana"))         # {'banana': True}  --- not shared with above

    print(parse_number_fixed("42"))         # 42
    print(parse_number_fixed("not_a_num"))  # prints message, returns None
