class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backTrack(temp, bool_map):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return

            for i in range(len(nums)):
                if bool_map[i]:
                    continue
                
                bool_map[i] = True
                temp.append(nums[i])
                backTrack(temp,bool_map)
                temp.pop()
                bool_map[i] = False
            
        backTrack([],[False] * len(nums))
        return ans


                


