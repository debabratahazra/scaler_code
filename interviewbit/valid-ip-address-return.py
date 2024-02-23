''' Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)'''


""" class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        ipadd = []
        if len(A) == 12:
            # divide 3x4 parts
            ipadd.append(A[:3]+'.'+A[3:6]+'.'+A[6:9]+'.'+A[9:])
            return ipadd
        elif len(A) < 12:
            result = []
            findIP(0, [], result)
            return result

    def findIP(start, path, result):
        if len(path) == 4:
            if start == len(s):
                result.append('.'.join(path))
                print(result)
            return
        for i in range(start, min(start+3, len(s))):
            if i != start and s[start] == '0':
                break
            segment = s[start:i+1]
            if int(segment) <= 255:
                path.append(segment)
                findIP(i+1, path, result)
                path.pop()


s = Solution()
A = "255255111135"
print(s.restoreIpAddresses(A)) """


def restoreIpAddresses(s):
    def dfs(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append('.'.join(path))
            return
        for i in range(start, min(start+3, len(s))):
            if i != start and s[start] == '0':
                break
            segment = s[start:i+1]
            if int(segment) <= 255:
                path.append(segment)
                dfs(i+1, path)
                path.pop()

    result = []
    dfs(0, [])
    return result


print(restoreIpAddresses("25525511135"))
