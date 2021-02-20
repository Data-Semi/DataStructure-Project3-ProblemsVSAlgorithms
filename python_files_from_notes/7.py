#!/usr/bin/env python
# coding: utf-8

# HTTPRouter using a Trie
# For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.
# 
# There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.
# 
# The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
# 
# 

# First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /
# 
# In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler
# 
# We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:
# 
# (root, None) -> ("about", None) -> ("me", "About Me handler")
# 
# We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
# 
# 

# In[17]:


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        token_list = path.split("/")  #split path to tokens list

        for token in token_list:
            if token not in current_node.children:
                current_node.insert(token)
            current_node = current_node.children[token]
        #add handler to the leaf node
        current_node.handler = handler
        
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        token_list = path.split("/")  #split path to tokens list        
        
        for token in token_list:
            if token not in current_node.children:
                return None
            current_node = current_node.children[token]

        return current_node.handler
    


# Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.
# 
# Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
# 
# Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
# 
# More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.
# 
# 

# In[29]:


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, token, handler):
        # Insert the node as before
        self.children[token] = RouteTrieNode(handler)
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_hander):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler
        self.not_found_handler = not_found_hander

    def add_handler(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        token_list = self.split_path(path)  #split path to tokens list

        for token in token_list:
            if token not in current_node.children:
                current_node.insert(token,self.not_found_handler)
            current_node = current_node.children[token]
        #add handler to the leaf node
        current_node.handler = handler
        
    def lookup(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        token_list = self.split_path(path)  #split path to tokens list 
        #if the path is not root path: "" or "/", search the path down. else, just return the rood handler
        if token_list != [""]: 
            for token in token_list:
                if token not in current_node.children:
                    return self.not_found_handler
                current_node = current_node.children[token]
        return current_node.handler
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == "" or path == "/":
            return [""]
        if path[-1] == "/":  # ignore the　tailed "/"
            return path[:-1].split("/")        
        return path.split("/")


# In[30]:


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler","not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# ## Program description  
# The router will initialize itself with a RouteTrie for holding routes and associated handlers. It also supports adding a handler by a path and looking up a handler by a path. All of these operations is delegated to the RouteTrie.  
# 
# The RouteTrie stores handlers under path parts, the function `split_path` is to split a path around the '/' character, and also handles trailing slashes of a path.  
# A request for '/about' or '/about/' is probably looking for the same page, the program will return the same handler.  
# Requests for '' or '/' are probably looking for the root handler, the program will return root handler.  
# 
# I have added a not found handler to the Router which is returned whenever a path is not found in the Trie.  
# 
# 
# ## Time compexity
# Both of the function `add_handler`, `lookup` includes a for loop, which related the length of the given input `path`. Therefore, both of them have a time complexity of O(n).
# The other functions in this program has no loop inside, takes constant time complexity O(1).
# 
# ## Space complexity  
# Every time the program traverses a path and add it to the existing structure, the program performs a few operations like initializing. This is a constant time operation.
# It takes O(1) to create a new node. It is not necessarily O(1) but O(C) where C is a constant.
# This is repeated in the worst case for all the paths with length m(m tokens).
# Here m would be the length of the longest path (worst case complexity) which would be repeated for all the paths and hence the space complexity is O(n*m).
# 
# 
