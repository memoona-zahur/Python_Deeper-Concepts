"""
Kata 3 - Custom exception
Define InsufficientFundsError(Exception) with a message that includes
the actual numbers, raise it from withdraw(), and catch it
specifically at the call site.
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the available balance."""

    def __init__(self, balance, amount):
        message = f"Cannot withdraw {amount}: balance is only {balance}"
        super().__init__(message)
        self.balance = balance
        self.amount = amount


def withdraw(balance, amount):
    breakpoint()  
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


if __name__ == "__main__":
    # Successful withdrawal
    print(withdraw(100, 30))  # 70

    # Failing withdrawal - caught specifically, not with ValueError
    # or a bare except.
    try:
        withdraw(100, 150)
    except InsufficientFundsError as e:
        print(f"Transaction failed: {e}")
        print(f"Balance was: {e.balance}, attempted: {e.amount}")

# pdb commands:
# 1. c - continue the program until the next breakpoint
# 2. n - next line ---> this executes the current line and stops at the next line in the current function.
# 3. s - step ---> this steps into the next function call (if the next line calls another function, it takes you inside it).
# 4. p <variable> - print variable with its value
# 5. l - list the code around the current line
