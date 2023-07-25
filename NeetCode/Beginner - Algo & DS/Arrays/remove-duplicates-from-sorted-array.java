// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
    public static int removeDuplicates(int[] nums) {
        int count = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] != nums[i + 1]) {
                nums[count] = nums[i];
                count++;
            }
        }

        // Copy the last element to the end (since it's not checked in the loop)
        if (nums.length > 0) {
            nums[count++] = nums[nums.length - 1];
        }

        return count;
    }
}
