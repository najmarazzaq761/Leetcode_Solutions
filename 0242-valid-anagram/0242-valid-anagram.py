class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)

        if len(s) != len(t):
            return False
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i,0) + 1
        for j in t:
            if j in dict1:
                dict1[j] -= 1
                if dict1[j] == 0:
                    del dict1[j]
            else:
                return False        
        return not dict1