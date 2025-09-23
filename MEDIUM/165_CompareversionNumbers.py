"""
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # The versions are equal
        return 0

"""
This code defines a solution to compare two version strings, `version1` and `version2`. The function `compareVersion` takes two strings as input and returns an integer indicating the comparison result: -1 if `version1` is less than `version2`, 1 if `version1` is greater than `version2`, and 0 if they are equal. The approach used in this solution can be broken down into the following steps:
1. Split both version strings by the dot '.' character to obtain lists of revision numbers, `nums1` and `nums2`.
2. Determine the lengths of both lists, `n1` and `n2`.
3. Iterate through the range of the maximum length of the two lists. For each index `i`, retrieve the corresponding revision number from each list, converting it to an integer. If one list is shorter, treat the missing revision as 0.
4. Compare the two revision numbers. If they are not equal, return 1 if the revision from `version1` is greater, or -1 if it is less.
5. If the loop completes without finding any differences, return 0, indicating that the two version strings are equal.
The time complexity of this solution is O(m + n), where m and n are the lengths of the two version strings, as it requires a single pass through the revisions of both versions. The space complexity is O(m + n) as well, due to the storage of the split revision lists.
"""