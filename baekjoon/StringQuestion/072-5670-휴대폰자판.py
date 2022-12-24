import sys


class Node(object):
    def __init__(self, key=None, click=0) -> None:
        self.key = key
        self.click = click
        self.children = {}

class Trie(object):
    def __init__(self) -> None:
        self.head = Node()

    def insert(self, string) -> None:
        curr_node = self.head
        for c in string:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)
            curr_node = curr_node.children[c]
            curr_node.click += 1

    def count(self, curr_node=None) -> int:
        if curr_node == None:
            curr_node = self.head
        
        total = 0
        for c in curr_node.children:
            if curr_node.click != curr_node.children[c].click:
                total += curr_node.children[c].click
            total += self.count(curr_node.children[c])
        return total


input = sys.stdin.readline
while (N := input().rstrip()) != '':
    N = int(N)
    tree = Trie()
    for _ in range(N):
        tree.insert(ins:=input().rstrip())
    print("{:.2f}".format(round(tree.count() / N, 2)))