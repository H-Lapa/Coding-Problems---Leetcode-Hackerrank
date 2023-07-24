class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int last = nums.length;

        while (i < last) {
            if (nums[i] == val) {
                nums[i] = nums[last-1];
                last -= 1;
            }
            else {
                i += 1;
            }
        }

        return last;
    }
}