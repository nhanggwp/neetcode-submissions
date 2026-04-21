class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l = 0;
    let r = heights.length - 1;
    let maxArea = 0;
    // min(heght1, height2) * width 
    while (l < r) {
        let width = (r - l)
        maxArea = Math.max(Math.min(heights[l], heights[r]) * width, maxArea);
        if (heights[l] > heights[r]) {
            r--;
        }
        else if (heights[r] > heights[l]) {
            l++;
        }
        else {
            l++;
        }
    }
        return maxArea;
    }

}
