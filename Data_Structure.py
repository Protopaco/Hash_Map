
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
        self.biggest_collision = 0

    def hash(self, key, collision_count):
        # returns number value of each letter
        values = {'A': '', 'B': 1, 'C': 2, 'D': 3, 'E': '', 'F': 4, 'G': 5, 'H': 6, 'I': '', 'J': 7, 'K': 8, 'L': '', 'M': 9,
              'N': '', 'O': '', 'P': 1, 'Q': 2, 'R': '', 'S': '', 'T': '', 'U': '', 'V': 3, 'W': 4, 'X': 5, 'Y': 6, 'Z': 7}
        x = 0
        hash_value = "1"
        temp_value = ""
        for i in key:
            if len(hash_value) < 6:
                    hash_value += str(values[i])
            #if len(hash_value) > 5:
                    #hash_value = str(int(hash_value) - collision_count)
            x += 1
        if collision_count > 0:
            hash_value = str(int(hash_value) + collision_count)
            print("hash: " +str(hash_value))

        return int(hash_value)

    def assign(self, key, value, collision_count=0):
        array_index = self.hash(key, collision_count)
        if not self.array[array_index]:
            self.array[array_index] = Node(key, value)
        else:
            current_node = self.array[array_index].get_value()
            if current_node[0] != key:
                #print("collision_count: {c}".format(c=collision_count))
                collision_count += 1
                self.assign(key, value, collision_count)
                if collision_count > self.biggest_collision:
                    self.biggest_collision = collision_count
                    print("big: " +str(self.biggest_collision))
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
