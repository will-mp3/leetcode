"""
On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
"""

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        users_to_teach = set()

        # Step 1: Identify users who can't communicate
        for user1, user2 in friendships:
            user1 -= 1  # Convert to 0-based index
            user2 -= 1
            can_communicate = False

            for lang1 in languages[user1]:
                if lang1 in languages[user2]:
                    can_communicate = True
                    break

            if not can_communicate:
                users_to_teach.add(user1)
                users_to_teach.add(user2)

        # Step 2: Try teaching each language
        min_users_to_teach = len(languages) + 1

        for language in range(1, n + 1):
            count = 0
            for user in users_to_teach:
                if language not in languages[user]:
                    count += 1
            min_users_to_teach = min(min_users_to_teach, count)

        return min_users_to_teach

"""
This code defines a solution to determine the minimum number of users that need to be taught a new language so that all friends in a social network can communicate with each other. 
The function `minimumTeachings` takes three parameters: an integer `n` representing the number of languages, a list of lists `languages` where each sublist contains the languages known by each user, and a list of lists `friendships` where each sublist contains a pair of users who are friends.
The approach used in this solution can be broken down into two main steps:
1. Identify Users Who Can't Communicate: The code iterates through each friendship pair and checks if the two users in the pair share at least one common language. 
If they do not, both users are added to a set called `users_to_teach`, which keeps track of all users who need to learn a new language in order to communicate with their friends.
2. Try Teaching Each Language: The code then iterates through each language from 1 to n. For each language, it counts how many users in the `users_to_teach` set do not know that language. 
This count represents the number of users that would need to be taught that particular language. The minimum count across all languages is tracked using the variable `min_users_to_teach`.
Finally, the function returns the minimum number of users that need to be taught a language so that all friends can communicate.
The time complexity of this solution is O(f * l + n * u), where f is the number of friendships, l is the average number of languages known per user, n is the number of languages, and u is the number of users who need to be taught. 
The space complexity is O(u), where u is the number of users who need to be taught, due to the storage of the `users_to_teach` set.
"""