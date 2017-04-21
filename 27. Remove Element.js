/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {

    let temp = 0;
    
    for(let i = 0; i < nums.length; )
    {
        if(nums[nums.length-1] == val)
        {
            nums.pop()
        }
        else if(nums[i] == val)
        {
            temp = nums[nums.length-1];
            nums[nums.length-1] = nums[i];
            nums[i] = temp;
            nums.pop();
            i = i + 1;
        }
        else
        {
            i = i + 1;
        }
    }
};
