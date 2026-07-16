# Week 01 · Tue · Practice — Python Idioms, Exceptions, Context Managers, Debugging

## Files
- `1_warmup.py` — mutable-default-argument fix and bare-except fix.
- `2_comprehensions.py` — verbose loop → list comprehension, verbose loop → dict comprehension, and one deliberate case left as a plain loop (nested condition + side effect).
- `3_custom_exception.py` — `InsufficientFundsError(Exception)`, raised from `withdraw()` and caught specifically at the call site.
- `4_context_manager.py` — a `Timer` context manager (class-based `__enter__`/`__exit__`) and an equivalent `@contextlib.contextmanager` version. Both guarantee the elapsed time prints even if the wrapped code raises.

## How to run
```bash
python3 1_warmup.py
python3 2_comprehensions.py
python3 3_custom_exception.py
python3 4_context_manager.py
```
# Python-Deeper-Idioms-Exceptions-Context-Managers-Debugging
