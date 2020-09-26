# class Tree:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

# def initialiseTree(value:str, array):
#     for n in range(len(value)):
#         array.append(Tree[data=value[]])
#         if 


# def recursion(n):
#     if n != 0:

# if __name__ == '__main__':
#     arr = []
#     string = 'HFOWQN'



class Binary_tree:
    """
    params:
    size: the size of the tree
    items: all items
    """

    def __init__(self, **kwargs):

        items = kwargs.get("items", "")
        self.size = kwargs.get("size", len(items))
        self.nodes = [self.Node(left_node=i+1) for i in range(self.size)]
        self.nodes[-1].left_node = None
        self.free_ptr = 0
        if items:
            for item in items:
                self.insert(item)

    def insert(self, item):
        # check if the tree has a root
        if self.free_ptr == 0:
            self.nodes[0].data = item
            self.free_ptr = self.nodes[0].left_node
            self.nodes[0].left_node = self.nodes[0].right_node = None
            return
        # check if the size is full
        elif self.free_ptr is None:
            # append another node
            self.nodes[-1].left_node = len(self.nodes)
            self.nodes.append(self.Node())
        this_ptr = 0        # start from the root
        previous_ptr = (None, None)     # (last ptr, left / right (0 or 1))

        while self.nodes[this_ptr].data is not None:
            if self.nodes[this_ptr].data > item:
                # turn left
                previous_ptr = (this_ptr, 0)
                if self.nodes[this_ptr].left_node is None:
                    break
                this_ptr = self.nodes[this_ptr].left_node
            else:
                # turn right
                previous_ptr = (this_ptr, 1)
                if self.nodes[this_ptr].right_node is None:
                    break
                this_ptr = self.nodes[this_ptr].right_node
        
        # found an empty node
        # store content
        this_ptr = self.free_ptr
        self.free_ptr = self.nodes[this_ptr].left_node
        self.nodes[this_ptr] = self.Node(item)
        
        # link to last node
        if previous_ptr[1]:
            self.nodes[previous_ptr[0]].right_node = this_ptr
        else:
            self.nodes[previous_ptr[0]].left_node = this_ptr

    
    def find_nodes(self, value):
        this_ptr = 0

        while this_ptr is not None and self.nodes[this_ptr].data != value:
            if self.nodes[this_ptr].data > value:
                this_ptr = self.nodes[this_ptr].left_node
            else:
                this_ptr = self.nodes[this_ptr].right_node
        return this_ptr

    def print_nodes(self):
        for index, node in enumerate(self.nodes):
            print("%d: %s" %(index, node))

    class Node:

        def __init__(self, data = None, left_node = None, right_node = None):
                self.data = data
                self.left_node = left_node
                self.right_node = right_node
        
        def __str__(self):
                return f"left: {self.left_node}, data: {self.data}, right: {self.right_node}"


class test_binary_tree(Binary_tree):

    """
    practice tree on recursion and search algorithms
    """
    def inTraverse(self, ptr):
        if ptr is not None:
            self.inTraverse(self.nodes[ptr].left_node)
            print(self.nodes[ptr].data, end = '')
            self.inTraverse(self.nodes[ptr].right_node)

    def preTraverse(self, ptr):
        if ptr is not None:
            print(self.nodes[ptr].data, end = '')
            self.preTraverse(self.nodes[ptr].left_node)
            self.preTraverse(self.nodes[ptr].right_node)
    
    def postTraverse(self, ptr):
        if ptr is not None:
            self.postTraverse(self.nodes[ptr].left_node)
            self.postTraverse(self.nodes[ptr].right_node)
            print(self.nodes[ptr].data, end = '')


if __name__ == "__main__":
    b_tree = test_binary_tree(items = "FCSBEDR")
    b_tree.print_nodes()
    print("\n\n in traverse:")
    b_tree.inTraverse(0)

    print("\n\n pre traverse:")
    b_tree.preTraverse(0)

    print("\n\n post traverse:")
    b_tree.postTraverse(0)

    print('\n')

