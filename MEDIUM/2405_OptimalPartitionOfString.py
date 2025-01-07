"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
"""

class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        lastSeen = [-1] * 26
        subStart = 0

        for i in range(len(s)):
            # check if we have already included this character, if most recent position is in the bounds of current substring
            if lastSeen[ord(s[i]) - ord('a')] >= subStart: # ord(s[i]) - ord('a') gets us the index of this character
                count += 1
                subStart = i
            # update last seen position
            lastSeen[ord(s[i]) - ord('a')] = i

        return count

"""
to solve this problem we take a greedy approach using the ord() method python supplies.
the ord() method takes a single Unicode character as input and returns its corresponding integer Unicode code point.
for example, ord('a') = 97.
our approach iterates through the given string s, creating a substring of the characters.
we keep track of which characters we have seen, and once a character we've seen in the current substring appears, we start a new one.
we start by initializing count to 1, our lastseen array to length of 26 (for each letter), and the starting index of our substring to 0.
we iterate through the string, first checking if we have seen the current character in our current substring.
this is where we use the ord method, we take the ord(s[i]) - the current character - and subtract ord('a') from it.
this gives us its index in our 26 length array, for example if s[i] == d then ord(s[i]) == 100, subtract ord('a') and you get 3.
if the index value stored at this index (ord(s[i]) - ord('a')) is greater than or equal to that of our substring start, 
we know that we've already seen this character in this substring.
if this is the case, increment count by 1 and update subStart to i to signify a new substring.
regardless of this condition we update the last seen position of this current character to index i.
once the loop completes we return count.
this solution runs in O(n) linear time.
"""