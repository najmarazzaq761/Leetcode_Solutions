class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t={}
        map_t_s={}
        for ch_s, ch_t in zip(s,t):
            if (ch_s in map_s_t and map_s_t[ch_s]!=ch_t) or (ch_t in map_t_s and map_t_s[ch_t]!= ch_s):
                return False
            map_s_t[ch_s]=ch_t
            map_t_s[ch_t]=ch_s
        return True