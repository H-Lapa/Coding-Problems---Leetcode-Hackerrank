# thought bubble

#look at first and last element of each row 

# if number is in that range perform a binary search

# if the target is there return true else false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:

            #Condition to search
            if target >= row[0] and target <= row[-1]:

                #searching

                pos = 0

                while len(row) > 1:

                    mid = len(row) // 2

                    if row[mid] == target:
                        print("early true")
                        return True

                    if row[mid] > target:
                        row = row[:mid]
                    else:
                        row = row[mid:]
                    

                return row[0] == target


        