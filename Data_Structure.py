
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

    def hash(self, key, test_value, collision_count):
        # returns number value of each letter
        values = {'E': '0', 'T': '1', 'A': '2', 'O': '3', 'I': '4', 'N': '5', 'S': '6', 'R': '7', 'H': '8', 'D': '9', 'L': '9', 'U': '8', 'C': '7',
              'M': '6', 'F': '5', 'Y': '6', 'W': '5', 'G': '4', 'P': '3', 'B': '2', 'V': '0', 'K': '0', 'X': '0', 'Q': '0', 'J': '0', 'Z': '0'}
        x = 0
        y = 0
        z = 0
        values[test_value[0]] = test_value[1]
        hash_value = []
        for j in range(0,6):
            hash_value.append(str(j))

        temp_value = 0
        temp_str= "HELLOWORLD"
        #print("key: {k}".format(k=key))
        for i in key:
            if x < 6:
                hash_value[x] = values[i]
                #print("hash_value: {h}".format(h=hash_value))
            elif x % 2 == 0:
                hash_value[-1] = values[i]
            else:
                hash_value[-2] = values[i]
            x += 1
        while len(hash_value) < 6:
            hash_value.append(values[temp_str[y]])
            y += 1
        if collision_count > 0 and collision_count < 10:
            hash_value[-1] = str(collision_count)
        elif collision_count > 9:
            if collision_count < 100:
                for i in str(collision_count):
                    hash_value[z] = i
                    z += 1
            elif collision_count < 200:
                for i in str(collision_count):
                    hash_value[z] = i
                    z += 2
            elif collision_count < 300:
                if z % 2 == 0:
                    for i in str(collision_count):
                        hash_value[z] = i
                        z += 1
                else:
                    for i in str(collision_count):
                        hash_value[-z] = i
                        z += 1
            elif collision_count < 400:
                for i in str(collision_count):
                    hash_value[-z] = i
                    z += 2
            elif collision_count < 500:
                for i in str(collision_count):
                    hash_value[-z] = i
                    z += 1
            elif collision_count < 600:
                z = 1
                for i in str(collision_count):
                    hash_value[z] = i
                    z += 1
            elif collision_count < 700:
                z = -1
                for i in str(collision_count):
                    hash_value[z] = i
                    z -= 1
            elif collision_count < 750:
                if z % 2 == 0:
                    for i in str(collision_count):
                        hash_value[z] = i
                        z += 1
                else:
                    for i in str(collision_count):
                        hash_value[-z] = i
                        z += 1
            elif collision_count < 800:
                for i in str(collision_count):
                    if z % 2 == 0:
                        hash_value[-z] = i
                    else:
                        hash_value[z] = i
                    z += 1
            elif collision_count < 850:
                for i in str(collision_count):
                    if z % 2 == 0:
                        hash_value[-z] = i
                    else:
                        hash_value[z] = i
                    z += 2
            elif collision_count < 900:
                for i in str(collision_count):
                    if z % 2 == 0:
                        hash_value[z] = i
                    else:
                        hash_value[-z] = i
                    z += 1
            elif collision_count < 950:
                for i in str(collision_count):
                    if z % 2 == 0:
                        hash_value[z] = i
                    else:
                        hash_value[-z] = i
                    z += 2

            else:
                for i in str(collision_count):
                    hash_value[-z] = i
                    z += 1

        #print("inside hash_value: {h}".format(h=hash_value))
        temp_str = ""
        temp_str = temp_str.join(hash_value[:6])
        """
        if collision_count > 900:
            print("key: {k}".format(k=key) )
            print("hash_value2: {h}".format(h=hash_value))
            print("temp_str: " +temp_str)

        if temp_str == "":
            temp_str = values[key[0]] + '1'
        """
        try:
            #print("inside hash_value: {h}".format(h=hash_value))
            return int(temp_str)
        except ValueError:
            print("Value Error!")
            print(temp_str)
            return 0

    def assign(self, key, value, test_value, collision_count=0,):
        array_index = self.hash(key, test_value, collision_count)
        #print("key: {k}".format(k=key))
        if not self.array[array_index]:
                #print("space empty")
                self.array[array_index] = Node(key, value)
        else:
            """
            if collision_count > 900:
                print("array_index: {a}".format(a=str(array_index)))
                print("Current_node {c} vs Key {k}".format(c=self.array[array_index].get_value(), k = key))
            """
            current_node = self.array[array_index].get_value()
            if current_node != key:
                try:
                    #print("collision_count: {c}".format(c=collision_count))
                    #print("Already in space: {a}".format(a=self.array[array_index].get_value()))
                    collision_count += 1
                    self.assign(key, value, test_value, collision_count)
                    if collision_count > self.biggest_collision:
                        self.biggest_collision = collision_count
                        #print("big: " +str(self.biggest_collision))
                except RecursionError:
                    collision_count += 1000
                    #print("RecursionError: {s}".format(s=self.array[array_index].get_value()))
                    #print("Current_node {c} vs Key {k}".format(c=current_node, k = key))
                    #print("array_index:  {a}".format(a=array_index))
                    #print("Key: {k}".format(k=key))
            else:
                self.array[array_index] = Node(key, value)
        return collision_count

    def retrieve(self, key, collision_count=0):
        array_index = self.hash(key) + collision_count
        current_node = self.array[array_index].get_value()
        if not self.array[array_index].is_empty() and current_node[0] != key:
            collision_count += 1
            print("collision_count: {c}".format(c=collision_count))
            self.assign(key, collision_count)

        else:
            return current_node
