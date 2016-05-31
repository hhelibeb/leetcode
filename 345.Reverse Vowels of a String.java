/*Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Subscribe to see which companies asked this question

Your runtime beats 62.64% of javasubmissions.
*/
public class Solution {
    public String reverseVowels(String s) 
    {
        char[] ch=s.toCharArray();//用toCharArray转换成数组，从首尾两个方向遍历寻找元音字母，避免循环的嵌套
        int start=0;
        int end=ch.length-1;
        Boolean switch1=false;
        Boolean switch2=false;
        char[] vowels=new char[]{'a','e','i','o','u','A','E','I','O','U'};
        while(start<end)
        {
        	for (char v : vowels)
    		{
        		if(switch1) break;
    			if(v==ch[start])
    			{
    				switch1=true;
    				break;
    			}
    		}
        	for (char v : vowels)
    		{
        		if(switch2) break;
    			if (v==ch[end])
    			{
    				switch2=true;
    				break;
    			}
    		}
        	if (switch1&&switch2)
			{
				char temp=ch[start];
				ch[start]=ch[end];
				ch[end]=temp;
				switch1=false;
				switch2=false;
			}
        	if (switch1==false)
			{
				start++;
			}
        	if (switch2==false)
			{
				end--;
			}
      }
        return new String(ch);
    }
}
