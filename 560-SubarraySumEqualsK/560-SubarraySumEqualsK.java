// Last updated: 12/07/2025, 13:28:53
import java.util.HashMap; // Import the HashMap class

class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap <Integer, Integer> map = new HashMap <> (); 
        map.put(0,1); 

        int sum = 0; 
        int count = 0; 

        for (int i = 0; i < nums.length; i++) { 
            sum += nums[i]; 
            int sumMinusK = sum - k; 

            if (map.containsKey(sum - k)){ 
                count +=  map.get(sum -k); 
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1); 
        }
        return count; 



        
    }
}