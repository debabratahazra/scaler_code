''' 
Compare two version numbers version1 and version2.
If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences. For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Note: Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        version1 = list(map(int, A.split('.')))
        version2 = list(map(int, B.split('.')))

        length = max(len(version1), len(version2))

        for i in range(length):
            num1 = version1[i] if i < len(version1) else 0
            num2 = version2[i] if i < len(version2) else 0

            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1

        return 0


s = Solution()
A = "1.13"
B = "1.13.4"
print(s.compareVersion(A, B))
