import sys


class Node(object):
    def __init__(self, key=None) -> None:
        self.key = key
        self.children = {}

class Trie(object):
    def __init__(self, root_key=None) -> None:
        self.head = Node(root_key)

    def insert(self, string: str) -> None:
        curr_node = self.head
        for char in string:
            if not char in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

    def find(self, string: str) -> bool:
        curr_node = self.head
        for char in string:
            if not char in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    tree = Trie()
    cnt = 0
    for _ in range(N):
        tree.insert(input().rstrip())
    for _ in range(M):
        if (tree.find(input().rstrip())):
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()