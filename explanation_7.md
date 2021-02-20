# HTTPRouter using a Trie

## Problem description

HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.  

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /  

Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

## Program description  

The router will initialize itself with a RouteTrie for holding routes and associated handlers. It also supports adding a handler by a path and looking up a handler by a path. All of these operations is delegated to the RouteTrie.  

The RouteTrie stores handlers under path parts, the function `split_path` is to split a path around the '/' character, and also handles trailing slashes of a path.  
A request for '/about' or '/about/' is probably looking for the same page, the program will return the same handler.  
Requests for '' or '/' are probably looking for the root handler, the program will return root handler.  

I have added a not found handler to the Router which is returned whenever a path is not found in the Trie.  

## Time compexity

Both of the function `add_handler`, `lookup` includes a for loop, which related the length of the given input `path`. Therefore, both of them have a time complexity of O(n).  
The other functions in this program has no loop inside, takes constant time complexity O(1).  

## Space complexity  

Every time the program traverses a path and add it to the existing structure, the program performs a few operations like initializing. This is a constant time operation.  
It takes O(1) to create a new node. It is not necessarily O(1) but O(C) where C is a constant.  
This is repeated in the worst case for all the paths with length m(m tokens).  
Here m would be the length of the longest path (worst case complexity) which would be repeated for all the paths and hence the space complexity is O(n * m).