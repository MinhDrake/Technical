from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # [a-z]
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, val: str):

        node = self.root
        for c in val:
            pos = ord(c) - ord('a')

            if self.children[pos] is None:
                self.children[pos] = TrieNode()

            node = self.children[pos]

        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if node.children[idx] is None:
                return False

            node = node.children[idx]

        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')

            if node.children[idx] is None:
                return False

            node = node.children[idx]

        return True


class ReverseTrie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.stream_characters = []

        for word in words:
            node = self.root
            for c in reversed(word):
                pos = ord(c) - ord('a')
                if node.children[pos] is None:
                    node.children[pos] = TrieNode()
                node = node.children[pos]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.stream_characters.append(letter)

        node = self.root
        for c in reversed(self.stream_characters):
            pos = ord(c) - ord('a')
            if node.is_word:
                return True
            if node.children[pos] is None:
                return False
            node = node.children[pos]

        return node.is_word

# example
main = ReverseTrie(["cd", "f", "kl"])
print(main.query("a"))
print(main.query("b"))
print(main.query("c"))
print(main.query("d"))
print(main.query("e"))
print(main.query("f"))
print(main.query("g"))
print(main.query("h"))
print(main.query("i"))
print(main.query("j"))
print(main.query("k"))
print(main.query("l"))
print(main.query("m"))
print(main.query("n"))
print(main.query("o"))
print(main.query("p"))
print(main.query("q"))
print(main.query("r"))
print(main.query("s"))
print(main.query("t"))
print(main.query("u"))
print(main.query("v"))
print(main.query("w"))
print(main.query("x"))
print(main.query("y"))
print(main.query("z"))


from typing import List

class TrieNode:
    def __init__(self):
        self.childrens = [None] * 9
class Trie:
    def __init__(self, nums: List[int]):
        self.root = TrieNode()

        for num in nums:
            node = self.root
            str_num = str(num)
            for i in range(len(str_num)):
                idx = int(str_num[i])
                if not node.childrens[idx]:
                    node.childrens[idx] = TrieNode()
                node = node.childrens[idx]
    def searchPrefix(self, num: int):
        str_num = str(num)
        node = self.root
        count = 0
        for num in str_num:
            idx = int(num)
            if node.childrens[idx]:
                node = node.childrens[idx]
                count += 1
            else:
                break
        return count


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]):
        trie = Trie(arr1)
        ans = 0
        for num in arr2:
            ans = max(ans, trie.searchPrefix(num))
        return ans


sol = Solution()
print(sol.longestCommonPrefix([10], [17,11]))