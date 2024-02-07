class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colours = [0, 0, 0]

        # assigning quantity of each colour
        for num in nums:
            colours[num] += 1

        p = 0

        #loops through the index, which also represents the colour
        for i in range(len(colours)):
            quantity = colours[i]

            for x in range(quantity):
                nums[p] = i
                p += 1
                




        