class Solution:
    def checkPermuation(self,s1,s2):
        if len(s1) != len(s2):
            return False
        
        mp = {}

        for i in range(len(s1)):
            mp[s1[i]] = mp.get(s1[i],0) + 1
        
        for i in range(len(s2)):
            if s2[i] not in mp:
                return False 
            mp[s2[i]] = mp.get(s2[i]) - 1 
            if mp[s2[i]] < 0: 
                return False
        
        return True
            

    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        length_s2 = len(s2)
        if length_s1 > length_s2:
            return False
        
        l = 0
        for r in range(length_s2):
            if(r - l + 1 == length_s1):
                if(self.checkPermuation(s2[l:r+1],s1)):
                    return True
                l = l + 1 

        return False


        