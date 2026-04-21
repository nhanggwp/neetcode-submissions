class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        length = len(s)
        max_cnt = 0
        l = 0
        max_len = 0
        for r in range(length):
            ch = s[r]
            mp[ch] = mp.get(ch,0) + 1
            max_cnt = max(max_cnt,mp[ch])
            if r - l + 1  - max_cnt > k:
                mp[s[l]] = mp.get(s[l]) -1 
                l = l + 1
                
            
            max_len = max(max_len, r - l + 1)

        return max_len