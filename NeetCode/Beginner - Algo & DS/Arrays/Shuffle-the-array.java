// https://leetcode.com/problems/shuffle-the-array/
class Solution {
    public int[] shuffle(int[] nums, int n) {
        // n is the size of half the nums arr

        int[] temp = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            System.out.println(i % 2);
            if (i % 2 == 1) {
                temp[i] = nums[n];
                n += 1;
            } else {
                temp[i] = nums[i/2];
            }
        }

        return temp;

    }
}
