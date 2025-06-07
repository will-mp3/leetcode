"""
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.
"""

class Solution:
    def clearStars(self, s: str) -> str:
        
        nStr = []
        cnt = [ 0 for _ in range(26) ] # [character index, count]

        def remove_min(string):
            # find min char using index based count array
            for i in range(26):
                if cnt[i]:
                    min = chr(ord('a') + i) # decode indexes 0 - 25 using unicode equivalent
                    cnt[i] -= 1
                    break

            # traverse new string backwards, removing first instance of min char
            for i in range(len(string) - 1, -1, -1):
                if string[i] == min:
                    del string[i]
                    return

        for i, char in enumerate(s):

            # if star is found, call helper function on current string built
            if char == "*":
                remove_min(nStr)
                continue

            # if not a star: add char to new string, get character index based on unicode value, increment count of said index
            nStr.append(char)
            charIdx = ord(char) - ord('a')
            cnt[charIdx] += 1

        return ''.join(nStr)

"""

"""