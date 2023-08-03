# class Solution(object):
#     def countStudents(self, students, sandwiches):

#         #create queue and stack
#         queue = deque(students)
#         stack = sandwhiches

#         #loop

#             #if equal values
#                 #pop from both
#             #else
#                 # append and pop on queue

#             #check if we are stuck
#             #loop through the length of the arrays
#                 #check if values of students are equal to that of queue[0]
#                     #if true break the loop
#                 #else
#                     #exit the overall big loop

#         return len(queue)

from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        # Create queue and stack
        queue = deque(students)
        stack = sandwiches

        while len(queue) > 0:
            if queue[0] == stack[0]:
                queue.popleft()
                stack.pop(0)
            else:
                queue.append(queue.popleft())

            found_match = False
            for i in range(len(queue)):
                if queue[i] == stack[0]:
                    found_match = True
                    break

            if found_match == False:
                break

        return len(queue)
