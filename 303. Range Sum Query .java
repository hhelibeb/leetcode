/*303. Range Sum Query - Immutable*/
/*Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.
*/
public class NumArray 
{
    private int[] nums;
    private int[] sums;
public NumArray(int[] nums)
{
    this.nums = nums;
    if(nums==null)
    {
        return;
    } 
    int len = nums.length;
    sums = new int[len];
    if(nums.length==0) sums=null; 
    else 
    {
        sums[0] = nums[0];
    for(int i=1;i<len;i++
    ) {
        sums[i] = nums[i]+sums[i-1];
     }
    }
}

public int sumRange(int i, int j) 
{
    if(i==0) 
    {
        return sums[j];
    } else 
    {
        return sums[j]-sums[i-1];
    }  
}
}
