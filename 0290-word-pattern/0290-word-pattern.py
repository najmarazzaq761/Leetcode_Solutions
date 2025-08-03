class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words= s.split()
        if len(words)!=len(pattern):
            return False
        map_p_s={}
        map_s_p={}
        for ch_p, ch_s in zip(pattern,words):
            if (ch_p in map_p_s and map_p_s[ch_p]!= ch_s) or (ch_s in map_s_p and map_s_p[ch_s]!= ch_p):
                return False
            map_p_s[ch_p]=ch_s
            map_s_p[ch_s]=ch_p
        return True