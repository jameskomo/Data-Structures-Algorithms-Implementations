def firstUniqChar(s):
        for key, value in enumerate(s):
            if s.count(value)==1:
                return s[key]
        return -1
print(firstUniqChar(s="leetcode"))
