# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        
        #while loop - what are we relying on to tell if the students are compatible or not?

        count = 0

        while students and count < len(students):
        
            # count works as an index, to see if no one from the students has taken the sandwich
            # if they havent then we know that the students are incompatible with the sandwiches
            # and we can return the length of the students list
            
            if students[0] == sandwiches[0]:
                #remove from both lists, when preference match
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                #sending a student to the back of the line
                student = students.pop(0)
                students.append(student)
                count += 1

            #print("students: ", students)
            #print("sandwiches: ", sandwiches)


        #print(students)
        return len(students)