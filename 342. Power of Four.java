/* Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
*/
public class Solution {
    public boolean isPowerOfFour(int num) 
    {
       
       double n = 1;
       
       while(n<num)
       {
           n = n*4;
       }
       
       if((num-n)==0) return true;
      
       return false;
       
    }
}
