class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        result_list = []
        carry = 0
        result = digits[n-1] + 1
        if(result >= 10):
            result = result - 10
            carry +=1
        result_list.append(result)
        for i in range(n -2, -1, -1):
            result = digits[i] + carry
            if(result >= 10):
                result = result - 10
                carry = 1
            elif(result < 10):
                carry = 0
            result_list.append(result)

        print(carry)
        if ( carry == 1):
            result_list.append(1)
        return result_list[::-1]
            
            