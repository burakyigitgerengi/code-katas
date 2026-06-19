class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if not current_node.left:
                        current_node.left = Node(data)
                        return
                    else:
                        current_node = current_node.left

                else:
                    if current_node.right is None:
                        current_node.right = Node(data)
                        return
                    else:
                        current_node = current_node.right

    def search(self, data):
        current_node = self.root
        while True:
            if current_node.data == data:
                return True
            elif data < current_node.data and current_node.left:
                if current_node.left:
                    current_node = current_node.left
            elif data > current_node.data and current_node.right:
                current_node = current_node.right
            else:
                return False
