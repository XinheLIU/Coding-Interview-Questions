class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()
        
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word =True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        if word is None:
            return False
        return self.search_helper(self.root, word, 0)
        
    def search_helper(self, node, word, index):
        if node is None:
            return False
            
        if index >= len(word):
            return node.is_word
        
        char = word[index]
        if char != '.':
            return self.search_helper(node.children.get(char), word, index + 1)
            
        for child in node.children:
            if self.search_helper(node.children[child], word, index + 1):
                return True
                
        return False