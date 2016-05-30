/*Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Subscribe to see which companies asked this question
*/
public class Solution {
    public boolean isAnagram(String s, String t) 
    {
        char[] ch1= s.toCharArray();
        char[] ch2= t.toCharArray();
        Arrays.sort(ch1);
        Arrays.sort(ch2);
        String string1=new String(ch1);
        String string2=new String(ch2);
        return(string1.equals(string2));
    }
}
