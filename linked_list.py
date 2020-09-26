class link:
    def __init__(self, pointer, value):
        self.pointer = pointer
        self.value = value

class AddNode:
    def __init__(self, arr, value):
        self.arr = arr
        self.value = value
        self.node = 0
    
    def __repr__(self):
        return 'Node: %s, Value: %s' % (self.value, self.value)

if __name__ == '__main__':
    # initialise an array of length 100 which simulates the linked list datatype.
    arr = [link(i, None) for i in range(100)]
    
    # add node
    