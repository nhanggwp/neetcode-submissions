class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
            
        dict = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in dict:
                dict[key] = [s]
            else:
                dict[key].append(s)
        
        return list(dict.values());