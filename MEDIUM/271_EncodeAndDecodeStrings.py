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
this solution requires two function definitions, the main goal is to find a way to encode strings to be decoded later.
the principle we follow is we need to have a way to know how many letters are in each string, 
but we also have to account for potential integers and symbols in those strings.
to accomplish this we encode our strings using a combination key of both integers and sumbols.
we use a pound symbol as our delimiter, which follows our integer character count.
encoding strings this way is easy, simple string concatenation, however decoding is more tricky.
to decode, we go through our now encoded string character by character, i is our start point and j is our manipulated pointer.
when we come across our delimiter, we know that the values between our start, i, and our position, j, contains the integer value.
we take this value and convert it to an int and then take that many characters and insert them as a string into our array.
example: 10#ridiculous - i would be at 1 and j would be at #, so our integer is 10.
we then update i to be at the end of this now decoded string and continue.
"""