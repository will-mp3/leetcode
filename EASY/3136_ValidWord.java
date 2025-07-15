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
 
 */