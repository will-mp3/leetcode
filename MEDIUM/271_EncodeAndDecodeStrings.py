"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).
"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for s in strs:
            # encode our string with the number of characters, a pound sign, and its contents
            res += str(len(s)) + "#" + s

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0
         
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # once we hit our delimiter get our encoded length value
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res

"""

"""