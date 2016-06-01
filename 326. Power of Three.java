/* Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
*/
public boolean isPowerOfThree(int n) 
{
    if(n==0) return false;
    return n == Math.pow(3, Math.round(Math.log(n)/Math.log(3)));
}
