
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, limit = None):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("List is Full")

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("List is Empty")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        else:
            print("List is Empty")

    def is_empty(self):
        return self.size == 0

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    def hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
        return hash_value

    def assign(self, key, value, collision_count=0):
        array_index = self.hash(key) + collision_count

        if not self.array[array_index]:
            self.array[array_index] = Node(key, value)
        else:
            current_node = self.array[array_index].get_value()
            if current_node[0] != key:
                collision_count += 1
                self.assign(key, value, collision_count)
                print("collision_count: {c}".format(c=collision_count))
            else:
                self.array[array_index] = Node(key, value)


    def retrieve(self, key, collision_count=0):
        array_index = self.hash(key) + collision_count
        current_node = self.array[array_index].get_value()
        if not self.array[array_index].is_empty() and current_node[0] != key:
            collision_count += 1
            print("collision_count: {c}".format(c=collision_count))
            self.assign(key, collision_count)

        else:
            return current_node
