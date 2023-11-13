#https://leetcode.com/problems/sort-an-array/
#merge sort

class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1
        
        while j < len(right):
            result.append(right[j])
            j += 1

        return result

# # new attempt

# # #my recursive way
# # def merge (arr1, arr2):
# #     newArr = []

# #     while arr1 and arr2:

# #         if arr1[0] <= arr2[0]:
# #             #if arr1 <= arr2, append arr1 element
# #             newArr.append(arr1.pop(0))
# #         else:
# #             #if arr1 > arr2, append arr2 element
# #             newArr.append(arr2.pop(0))

# #     #if an array is empty append it to the end of the new array
# #     if not arr1:
# #         newArr += arr2
# #     else:
# #         newArr += arr1

# #     return newArr

# # def mergeSort(arr):
# #     if len(arr) <= 1:
# #         return arr

# #     mid = len(arr) // 2
# #     right = mergeSort(arr[mid:])
# #     left = mergeSort(arr[:mid])
    
# #     return merge(left, right)


# # # print(merge([1, 2, 3, 4], [1, 2, 3]))
# # # print(merge([1, 7, 3, 4, 2], [5, 8, 3, 4, 9]))


# #create a merge, which uses pointers to compare the two arrays
# def merge(arr1, arr2):
#     newArr = []
#     i = 0
#     j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             newArr.append(arr1[i])
#             i += 1
#         else:
#             newArr.append(arr2[j])
#             j += 1

#     if i < len(arr1):
#         newArr += arr1[i:]
#     else:
#         newArr += arr2[j:]

#     return newArr



# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])

#     return merge(left, right)



# print(mergeSort([1, 7, 3, 4, 2, 5, 8, 3, 4, 9]))

