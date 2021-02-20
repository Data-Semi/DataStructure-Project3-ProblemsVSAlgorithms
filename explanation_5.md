# Autocomplete with Tries 

## Problem description

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

## Program description  
A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.  

This is a autocomplete function implemented by a working trie for storing strings.  

A Trie class that contains the root node (empty string)  
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.  

The functhion `suffixes` in the TrieNode returns all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().  

## Time compexity
Both of the function `insert`, `find` includes a for loop, which related the length of the given input string. Therefore, both of them have a time complexity of O(n).  
The function `suffixes` is a recursive function that has time complexity O(n). 

## Space complexity  
Every time the program traverses a inputted string and add it to the existing structure, the program performs a few operations like initializing. This is a constant time operation.  
It takes O(1) to create a new node. It is not necessarily O(1) but O(C) where C is a constant.  
This is repeated in the worst case for all the strings with length m(m caractors).  
Here m would be the length of the longest string (worst case complexity) which would be repeated for all the strings and hence the space complexity is O(n * m).
