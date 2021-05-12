from collections import deque


class Node:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {}
        self.mark = False
        self.crumbs = char


class Trie:
    def __init__(self):
        self.root = Node("")
        self.length = 0

    def add(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
        if not node.end:
            self.length += 1
        node.end = True

    def pop(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                raise KeyError(word)
        if node.end:
            node.end = False
            self.length -= 1
        else:
            raise KeyError(word)

    def contains(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if not node.end:
            return False
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.add('salad')
    trie.add('apple')
    trie.add('mango')
    trie.add('juice')
    trie.add('carrot')
    trie.add('broccoli')

    print(trie.contains('sal'))
    print(trie.contains('salad'))