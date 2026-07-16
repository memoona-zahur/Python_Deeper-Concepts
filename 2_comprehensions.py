"""
Kata 2 - Comprehension refactor
Rewrite a verbose loop as a list comprehension, and a verbose loop
building a dict from two parallel lists as a dict comprehension.
Then show one case where a comprehension would make things WORSE,
and leave that one as a plain loop on purpose.
"""


# Part A: verbose loop ---> list comprehension

def filter_long_names_verbose(names):
    result = []
    for name in names:
        if len(name) > 3:
            result.append(name.upper())
    return result


def filter_long_names_comprehension(names):
    return [name.upper() for name in names if len(name) > 3]


# Part B: verbose loop ---> dict comprehension

def build_dict_verbose(keys, values):
    d = {}
    for k, v in zip(keys, values):
        d[k] = v
    return d


def build_dict_comprehension(keys, values):
    return {k: v for k, v in zip(keys, values)}


# Part C: deliberately NOT a comprehension 
# This has a nested condition AND a side effect (flagging an order)
# Cramming that into a comprehension would hide the side effect and
# make the line hard to read at a glance - so it stays a loop.

class Order:
    def __init__(self, order_id, status, total):
        self.id = order_id
        self.status = status
        self.total = total
        self.flagged = False

    def flag_for_review(self):
        self.flagged = True

# flagged_ids = [order.flag_for_review() or order.id for order in orders       # if we tried to cram it into a comprehension, 
#                if order.status == "pending" and order.total > 100]           # it would look like this, but it's not as clear


def flag_high_value_pending_orders(orders):
    """
    Kept as a loop on purpose: it has a side effect (flag_for_review)
    and nested conditions.
    """
    flagged_ids = []
    for order in orders:
        if order.status == "pending":
            if order.total > 100:
                order.flag_for_review()
                flagged_ids.append(order.id)
    return flagged_ids


if __name__ == "__main__":
    names = ["Ali", "Bilal", "Ayesha", "Mahrukh", "Zoi"]
    print(filter_long_names_verbose(names))
    print(filter_long_names_comprehension(names))
    assert filter_long_names_verbose(names) == filter_long_names_comprehension(names)

    keys = ["name", "age", "city"]
    values = ["Memoona", 23, "Lahore"]
    print(build_dict_verbose(keys, values))
    print(build_dict_comprehension(keys, values))
    assert build_dict_verbose(keys, values) == build_dict_comprehension(keys, values)

    orders = [
        Order(1, "pending", 150),
        Order(2, "pending", 50),
        Order(3, "shipped", 200),
    ]
    print(flag_high_value_pending_orders(orders))  # [1]
