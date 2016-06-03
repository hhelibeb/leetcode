/* Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Subscribe to see which companies asked this question
*/
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k)
    {
      HashMap<String,Integer> hashMap=new HashMap<String,Integer>();
		List<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < nums.length; i++)
		{			
			String string = String.valueOf(nums[i]);
			if (!hashMap.containsKey(string))
			{
				hashMap.put(string, 1);
			}
			else
			{
				Integer num = hashMap.get(string) + 1;
				hashMap.remove(string);
				hashMap.put(string, num);
			}			
		}
		List<Map.Entry<String,Integer>> list2=new ArrayList<>();  
        list2.addAll(hashMap.entrySet());  
        ValueComparator vc=new ValueComparator();  
        Collections.sort(list2,vc); 
        for (int i = 0; i < k; i++)
		{
			list.add(Integer.parseInt(list2.get(i).getKey()) );
		}
		return list;
	}
   private static class ValueComparator implements Comparator<Map.Entry<String,Integer>>  
    {  
        public int compare(Map.Entry<String,Integer> m,Map.Entry<String,Integer> n)  
        {  
            return n.getValue()-m.getValue();  
        }  
    }  
}
