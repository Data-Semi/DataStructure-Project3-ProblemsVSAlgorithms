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