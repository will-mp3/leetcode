/*
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 */

class Solution {
    public boolean isValid(String word) {
        boolean hasConsonant = false;
        boolean hasVowel = false;
        boolean allValid = true;

        for(char c : word.toCharArray()) {
            if(Character.isLetter(c) == false && Character.isDigit(c) == false){
                allValid = false;
            }

            if (Character.isLetter(c)) {
                c = Character.toLowerCase(c);
                if ("aeiou".indexOf(c) != -1) {
                    hasVowel = true;
                }
                else {
                    hasConsonant = true;
                }
            }

        }
        
        return hasConsonant && hasVowel && allValid && word.length() >= 3;
    }
}

/*
 this solution checks if the word is valid based on the given criteria.
It iterates through each character in the word, checking if it is a letter or digit,
and whether it contains at least one vowel and one consonant.
If the word meets all the conditions, it returns true; otherwise, it returns false.
The solution uses a single loop to check all conditions, making it efficient with a time complexity of O(n), where n is the length of the word.
 */