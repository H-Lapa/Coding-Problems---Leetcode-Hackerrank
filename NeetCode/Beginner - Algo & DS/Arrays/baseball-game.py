#my solution
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        scores = []

        for x in operations:
            print(scores)
            if x.isdigit() or x[0] == '-':
                scores.append(int(x))
            elif x == '+':
                scores.append((scores[-1] + scores[-2]))
            elif x == 'D':
                scores.append(scores[-1] * 2)
            elif x == 'C':   
                scores.pop()

        return sum(scores)

#optimal solution
# what changed? if statement waterfall is optimised for no digit check
# calculating the score during the for loop
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        total_score = 0
        last_scores = []

        for x in operations:
            if x == '+':
                score = sum(last_scores[-2:])
                total_score += score
                last_scores.append(score)
            elif x == 'D':
                score = 2 * last_scores[-1]
                total_score += score
                last_scores.append(score)
            elif x == 'C':   
                if last_scores:
                    total_score -= last_scores.pop()
            else:
                score = int(x)
                total_score += score
                last_scores.append(score)
    

        return total_score
