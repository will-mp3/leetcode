"""
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        letters = list(brokenLetters)

        res = len(words)
        for word in words:
            for letter in letters:
                if letter in word:
                    res -= 1
                    break
        
        return res

"""
This code defines a solution to determine the number of words in a given string that can be fully typed using a keyboard with certain broken letter keys. The function `canBeTypedWords` takes two parameters: a string `text` containing words separated by single spaces, and a string `brokenLetters` containing all distinct letter keys that are broken on the keyboard.
The approach used in this solution can be broken down into the following steps:
1. Split the input string `text` into a list of words using the `split(" ")` method.
2. Convert the string `brokenLetters` into a list of individual broken letters.
3. Initialize a variable `res` to the total number of words in the `words` list. This variable will be used to count the number of words that can be fully typed.
4. Iterate through each word in the `words` list. For each word, check if it contains any of the broken letters.
5. If a word contains any broken letter, decrement the `res` variable by 1 and break out of the inner loop to avoid further checks for that word.
6. After checking all words, return the value of `res`, which represents the number of words that can be fully typed without using any broken letters.
The time complexity of this solution is O(m * n), where m is the number of words and n is the average length of the words, as each word may need to be checked against all broken letters. The space complexity is O(k), where k is the number of broken letters, due to the storage of the `letters` list.
"""