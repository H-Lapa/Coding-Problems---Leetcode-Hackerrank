
#solution shown to me
# time complexity : O(nlogk)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]


# my solution
#quick sort / select solution
# time complexity : O(n^2) - worst case 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k

        def quickSelect(l, r):

            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p > k: 
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return nums[p]


        return quickSelect(0, len(nums) - 1)