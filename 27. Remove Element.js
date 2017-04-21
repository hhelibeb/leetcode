/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    
    for(let i = 0; i < nums.length; i++ )
    {
        if(nums[nums.length - 1] == val)
        {
            nums.pop()
            i--;
        }
        else if(nums[i] == val)
        {
            nums[i] = nums[nums.length - 1];
            nums.pop();
        }
        else
        {
            
        }
    }
};
