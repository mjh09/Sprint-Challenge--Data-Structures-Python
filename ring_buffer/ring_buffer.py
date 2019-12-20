from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            
        elif self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            
        elif self.current == None:
            self.storage.delete(self.storage.tail)
            self.storage.add_to_tail(item)
            self.current = 1
        
        elif self.current == 1:
            x = self.storage.tail.value

            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)
            
            self.storage.add_to_tail(item)
            self.storage.add_to_tail(x)
            self.current = 2


        elif self.current == 2:
            x = self.storage.tail.value
            y = self.storage.tail.prev.value

            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)

            self.storage.add_to_tail(item)
            self.storage.add_to_tail(y)
            self.storage.add_to_tail(x)
            self.current = 3

        elif self.current == 3:
            x = self.storage.tail.value
            y = self.storage.tail.prev.value
            z = self.storage.tail.prev.prev.value

            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)

            self.storage.add_to_tail(item)
            self.storage.add_to_tail(z)
            self.storage.add_to_tail(y)
            self.storage.add_to_tail(x)
            self.current = 4

        elif self.current == 4:
            x = self.storage.tail.value
            y = self.storage.tail.prev.value
            z = self.storage.tail.prev.prev.value
            a = self.storage.tail.prev.prev.prev.value

            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)
            self.storage.delete(self.storage.tail)

            self.storage.add_to_tail(item)
            self.storage.add_to_tail(a)
            self.storage.add_to_tail(z)
            self.storage.add_to_tail(y)
            self.storage.add_to_tail(x)
            self.current = None
        





    def get(self):
        list_buffer_contents = []

        while True:
            try:
                ele = self.storage.remove_from_tail()
                list_buffer_contents.extend(ele)
            except:
                break
        
        for ele in list_buffer_contents:
            self.append(ele)
        return list_buffer_contents

# # ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
