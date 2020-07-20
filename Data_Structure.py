
class Node:
    def __init__(self, key, value):
        self.data = (key, value)

    def get_data(self):
        return self.data

    def get_value(self):
        return self.data[1]

    def get_key(self):
        return self.data[0]

"""
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
"""
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]
        self.biggest_collision = 0


    def hash(self, key, collision_count):
        # returns number value of each letter
        values = {'E': '1', 'T': '2', 'A': '3', 'O': '4', 'I': '5', 'N': '6', 'S': '7', 'R': '8', 'H': '9', 'D': '10', 'L': '11', 'U': '12', 'C': '13',
              'M': '14', 'F': '15', 'Y': '16', 'W': '17', 'G': '18', 'P': '19', 'B': '20', 'V': '21', 'K': '22', 'X': '23', 'Q': '24', 'J': '25', 'Z': '26'}

        list_size = 2677549
        hash_value = []
        temp_array = ""

        for i in key:
            hash_value.append(values[i])

        hash_value.append(str(collision_count))
        temp_array = temp_array.join(hash_value)
        temp_array = str(int(temp_array) % list_size)
        temp_array = temp_array[-6:]
        array_index = int(temp_array)
        return array_index



    def assign(self, key, value, collision_count=0):
        array_index = self.hash(key, collision_count)
        if not self.array[array_index]:
                self.array[array_index] = Node(key, value)
        else:
            current_node = self.array[array_index].get_key()
            if current_node != key:
                try:
                    collision_count += 1
                    self.assign(key, value, collision_count)
                    if collision_count > self.biggest_collision:
                        self.biggest_collision = collision_count
                except RecursionError:
                    print("RecursionError: {s}".format(s=self.array[array_index].get_key()))
                    print("Current_node {c} vs Key {k}".format(c=current_node, k = key))
                    print("array_index:  {a}".format(a=array_index))
                    print("Key: {k}".format(k=key))
            else:
                self.array[array_index] = Node(key, value)
        return collision_count

    def retrieve(self, key, collision_count=0):
        array_index = self.hash(key, collision_count)
        current_node = self.array[array_index].get_data()
        #print("current_node = {c}".format(c=current_node))
        while current_node[0] != key:
            #print("current_node = {c}".format(c=current_node))
            collision_count += 1
            #print("collision_count: {c}".format(c=collision_count))
            array_index = self.hash(key, collision_count)
            current_node = self.array[array_index].get_data()

        return current_node
