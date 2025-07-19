"""

There is a given list of strings where each string contains only lowercase letters from , inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. 
In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

Input (stdin)
7
aab
defgab
abcde
aabcde
cedaaa
bbbbbbbbbb
jabjjjad

Expected Output
BAD SET
aabcde

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            if current.end:
                return False  # Existing word is a prefix of current word
        if current.children:
            return False  # Current word is a prefix of existing word
        current.end = True
        return True
        
def noPrefix(words):
    trie = Trie()
    for word in words:
        if not trie.insert(word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")
    
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
