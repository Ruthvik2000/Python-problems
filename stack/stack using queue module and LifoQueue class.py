# If you’re implementing a stack in a threading environment, then it’s likely a good idea to use a LifoQueue.
"""
In general, you should use a deque if you’re not using threading. 
If you are using threading, then you should use a LifoQueue unless you’ve measured your performance 
and found that a small boost in speed for pushing and popping will make enough difference to warrant the maintenance risks.
list may be familiar, but it should be avoided because it can potentially have memory reallocation issues. 
The interfaces for deque and list are identical, and deque doesn’t have these issues, 
which makes deque the best choice for your non-threaded Python stack.
"""
