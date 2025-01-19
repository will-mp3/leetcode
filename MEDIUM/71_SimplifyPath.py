"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. 
For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        # initialize stack
        stack = []

        # split the input on "/" as the delimiter
        for x in path.split("/"):
            # if current portion is .., pop from our stack to symbolize moving up a directory
            if x == "..":
                if stack:
                    stack.pop()

            # if current portion is . or empty we dont do anything, next iteration
            elif x == "." or not x:
                continue

            # if none of the above condition execute, its a legitimate directory name
            else:
                stack.append(x)

        # stitch stack together
        resStr = "/" + "/".join(stack)
        return resStr

"""
this problem is perfectly suited for a stack to be used.
we see that we are checking a string, which could be done using any data structure in theory.
what makes this problem so alluring for a stack is the layered nature of a directory, especially when dealing with "..".
we are able to add what we want to the stack, pop when we need to move up a directory, and stitch our final product.
we start by initializing our stack object.
we then split our input string using "/" as a delimiter so as to isolate the specific directories.
for each element in our split string, we check to see if its "..", if this is the case we know this represents the parent directory.
when this is the case, we check to see if the stack is not null, and if it isnt we pop from the stack.
this brings is back a level to the parent directory in question.
next we check for ".", which represents the current directory.
if a . is found, we do nothing and move to the next element since this dot is redundant in the simplified path.
if neither of these conditions execute then we know we have found a valid directory and push it to the stack.
by the end we stitch together the contents of our stack and return the new string.
this solution runs in O(n) linear time.
"""