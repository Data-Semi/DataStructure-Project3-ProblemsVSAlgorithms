## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        #base condition
        suffix_list = []
        if self.is_word == True:  # found a word
            suffix_list.append(suffix)
            
        if len(self.children) != 0:  # this node has children
            for char in self.children:
                suffix_list.extend(self.children[char].suffixes(suffix+char))

        return suffix_list
    ## Recursive function that collects the suffix for 
    ## all complete words below this point

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node

test_trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    test_trie.insert(word)

def find_suffixes_by_given_prefix(MyTrie, prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(' '.join(prefixNode.suffixes()))
        else:
            print("The prefix " + prefix + " not found")
    else:
        print('')

print(test_trie.root.suffixes())  #print out all the contents inside the trie
#sould be:
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
find_suffixes_by_given_prefix(test_trie, "ant")  # should print: hology agonist onym
find_suffixes_by_given_prefix(test_trie, "anti")  # should print: The prefix anti not found
find_suffixes_by_given_prefix(test_trie, "")  # sould print an empty line
find_suffixes_by_given_prefix(test_trie, "tr") # sould print: ie igger igonometry ipod