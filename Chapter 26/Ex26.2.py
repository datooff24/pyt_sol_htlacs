import time


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


# ----------------------------------------------------------------------------------------------------------------------

# Queue is prioritized by popping out the largest elements first
class PriorityQueueLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def __str__(self):
        return "Head: {0}, length: {1}".format(self.head, self.length)

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # if the node has highest priority, then it should be pushed to the front.
            if node.cargo >= self.head.cargo:
                node.next = self.head
                self.head = node
                return

            # We create two nodes, where previous is the node before current
            previous = None
            current = self.head
            while current is not None and node.cargo <= current.cargo:
                previous = current
                current = current.next

            # If does nodes belong at the end
            if current is not None:
                previous.next = node
                node.next = current

            # If the node does belong at the end
            else:
                self.last.next = node
                self.last = node

        # We are always adding a node, no matter where we place it
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo


# Test

queue1 = PriorityQueueLinkedList()
for num in [100, 20, 9, 500, 31]:
    queue1.insert(num)

# Largest element is 500
print(f"Head of the queue: {queue1.head.cargo}")

# Remove 500 first, next item will be 100
queue1.remove()
print(f"New head of the queue: {queue1.head.cargo}")

# Remove 100, next item 31, etc.
queue1.remove()
print(f"New head of the queue: {queue1.head.cargo}")


# ----------------------------------------------------------------------------------------------------------------------

# Comparison of both implementations
def compare_queue_ADT(queue_length, priority_queue_linkedlist, priority_queue):
    """"Compares the performance of PriorityQueue and PriorityQueueLinkedList for a priority_queue_linkedlist of
    length queue_length """
    # Compare the performance when inserting items into the queues.
    # First PriorityQueueLinkedList
    start1 = time.process_time()
    for i in range(queue_length):
        priority_queue_linkedlist.insert(i)
    end1 = time.process_time()

    # Secondly PriorityQueue
    start2 = time.process_time()
    for i in range(queue_length):
        priority_queue.insert(i)
    end2 = time.process_time()

    print("PriorityQueueLinkedList insert total time taken: {0}, PriorityQueue insert total time taken: {1}".format(
        end1 - start1, end2 - start2))
    # Conclusion: varies

    # Compare the performance when removing items from the queues.
    # First PriorityQueueLinkedList
    start1 = time.process_time()
    for i in range(queue_length):
        priority_queue_linkedlist.remove()
    end1 = time.process_time()

    # Secondly PriorityQueue
    start2 = time.process_time()
    for i in range(queue_length):
        priority_queue.remove()
    end2 = time.process_time()

    print("PriorityQueueLinkedList remove total time taken: {0}, PriorityQueue remove total time taken: {1}".format(
        end1 - start1, end2 - start2))
    # Conclusion: PriorityQueueLinkedList is faster


priority_queue = PriorityQueue()
priority_queue_linkedlist = PriorityQueueLinkedList()
compare_queue_ADT(10000, priority_queue_linkedlist, priority_queue)
