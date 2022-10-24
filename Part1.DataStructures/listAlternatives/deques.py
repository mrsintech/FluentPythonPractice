from collections import deque

# -=-=-=-=-=-=- DEQUES AND OTHER QUEUES -=-=-=-=-=-=- #
# deque means double-ended queue
# collections.deque is a thread-safe double-ended queue designed for fast
# inserting and removing from both ends.

# deque can be created with fixed maximum length. If a bounded deque is full,
# when you add a new item, it discards an item from the opposite end.

dq = deque(range(10), maxlen=10)  # maxlen is optional
print(dq)
# Rotating with n > 0 takes items from the right end and prepends them to
# the left; when n < 0 items are taken from left and appended to the right.
dq.rotate(4)
print(dq)

dq.rotate(-5)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)

# ProTip: deques are fast when adding or removing from its ends, it may be
# costly if removing items from the middle of a deque, its not as fast, it is
# really optimized for appending and poping from ends.

# the append and popleft operations are atomic, so deque is safe to use as a
# FIFO queue in multithreaded applications without the need for locks

# NOTE: a_list.pop(p) allows removing from position p, but deque does not
# support that option.

# List of Other Python standard library packages implement queues

# 1. queue
# This provides the synchronized (i.e., thread-safe) classes SimpleQueue, Queue
# LifoQueue, and PriorityQueue. These can be used for safe communication
# between threads. All except SimpleQueue can be bounded by providing a max
# size argument greater than 0 to the constructor. However, they don’t discard
# items to make room as deque does. Instead, when the queue is full, the
# insertion of a new item blocks—i.e., it waits until some other thread makes
# room by taking an item from the queue, which is useful to throttle the number
# of live threads.

# 2. multiprocessing
# Implements its own unbounded SimpleQueue and bounded Queue, very similar to
# those in the queue package, but designed for interprocess communication. A
# specialized multiprocessing.JoinableQueue is provided for task management.

# 3. asycio
# Provides Queue, LifoQueue, PriorityQueue, and JoinableQueue with APIs
# inspired by the classes in the queue and multiprocessing modules, but adapted
# for managing tasks in asynchronous programming.

# 4. headq
# In contrast to the previous three modules, heapq does not implement a queue
# class, but provides functions like heappush and heappop that let you use a
# mutable sequence as a heap queue or priority queue.
