from time import time
from collections import deque

def queue(queue, pushed=1):
	t1 = time()
	queue.insert(0, 4)
	queue.pop()
	t2 = time()
	print("Tempo necessario con lista: {}".format(t2 - t1))

def queue_con_deque(queue, pushed=1):
	t1 = time()
	queue.appendleft(pushed)
	queue.popleft()
	t2 = time()
	print("Tempo necessario con deque: {}".format(t2-t1))

queue_l = list(range(10000000))
queue_d = deque(queue_l)

queue(queue_l)
queue_con_deque(queue_d)
