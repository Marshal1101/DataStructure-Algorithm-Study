import sys


class Node(object):
    def __init__(self, key, level=0):
        self.key = key
        self.level = level
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, arr):
        curr_node = self.head
        for food in arr:
            if food not in curr_node.children:
                curr_node.children[food] = Node(food)
                curr_node.children[food].level = curr_node.level + 1
            curr_node = curr_node.children[food]

    def levelprint(self, level):
        ret = ""
        for _ in range(1, level):
            ret += "--"
        return ret

    def mapprint(self, food=None):
        if food == None: curr_node = self.head
        else:
            curr_node = food
            print(f"{self.levelprint(curr_node.level)}{curr_node.key}")
        for food in sorted(curr_node.children.keys()):
            self.mapprint(curr_node.children[food])


def main():
    input = sys.stdin.readline
    N = int(input())
    tree = Trie()
    for _ in range(N):
        line = input().split()
        tree.insert(line[1:])

    tree.mapprint()


if __name__ == '__main__':
    main()