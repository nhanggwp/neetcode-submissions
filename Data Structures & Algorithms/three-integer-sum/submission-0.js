class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) { let return_arr = [];
    let numbers = nums.sort((a, b) => a - b)
    for (let i = 0; i < numbers.length; i++) {
        if (i > 0 && numbers[i] === numbers[i - 1]) continue;
        let target = - numbers[i];
        let l = i+1;
        let r = numbers.length - 1;
        while (l < r) {
            if (numbers[l] + numbers[r] == target) {
                return_arr.push([numbers[i], numbers[l], numbers[r]]);

                l++;
                r--;

                while (l < r && numbers[l] === numbers[l - 1]) l++;
                while (l < r && numbers[r] === numbers[r + 1]) r--;
            }
            else if (numbers[l] + numbers[r] < target) {
                l = l + 1;
            }
            else if (numbers[l] + numbers[r] > target) {
                r = r - 1;
            }
        }}
    return return_arr;
}
}
