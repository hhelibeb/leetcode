/*Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.

Subscribe to see which companies asked this question
*/
public class Solution {
    public int[] twoSum(int[] nums, int target) 
    {
        	 int[] nums2=new int[nums.length];
	        for(int m=0;m<nums.length;m++)
	        {
	            nums2[m]=nums[m];
	        }
	        Arrays.sort(nums);
	        int a=0;
	        int b=nums.length-1;
	        for(int j=0;j<nums.length;j++)
	        {
	            int sum=nums[a]+nums[b];
	            if(sum>target)
	            {	          
	            	b--;	          
	            }
	            else if(sum<target)
	            {
	            	a++;
	            }
	            else if(sum==target)
	            {
	                break;
	            }
	        }
	        int c=0;int d=0;
	        for(int n=0;n<nums2.length;n++)
	        {
	            if(nums2[n]==nums[a])
	            {c=n;break;}          
	        }
	        for(int n=0;n<nums2.length;n++)
	        {
	            if(nums2[n]==nums[b])
	            {d=n;}          
	        }
	        int ch2[]=new int[]{c,d};
	        Arrays.sort(ch2);
	        return ch2;
    }
}
