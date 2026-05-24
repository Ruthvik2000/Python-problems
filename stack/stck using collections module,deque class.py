#While the interface for list and deque were similar, LifoQueue uses .put() and .get() to add and remove data from the stack
from collections import deque
x=deque()
x.append(10)
x.append(20)
x.append(30)
print(x)
x.pop()
print(x)
x.pop()
x.pop()
print(x)
"""
output:
deque([10, 20, 30])
deque([10, 20])
deque([])
"""
x.pop()
print(x)
"""
output:
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    x.pop()
IndexError: pop from an empty deque
"""