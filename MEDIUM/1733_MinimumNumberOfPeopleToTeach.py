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

"""