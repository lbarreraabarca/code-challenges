#
# PROBLEM DESCRIPTION
# In the k–partition problem, 
# we need to partition an array of positive 
# integers into k disjoint subsets that all have an equal sum, 
# and they completely cover the set.
#
# For example, consider set S = { 7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4 }.
# 
# S can be partitioned into two partitions, each having a sum of 30.
# S1 = { 5, 3, 8, 4, 6, 4 }
# S2 = { 7, 3, 5, 12, 2, 1 }

import random

def solver(M: list, A: list, numPartitions: int, sumConstraint: int, result: list) -> list:
    if len(result) == numPartitions:
        return result
    if sum(A) == sumConstraint:
        result.append(A)
        print("I found a valid solution {} {} {} {} {}".format(M, A, numPartitions, sumConstraint, result))
        solver(M, [], numPartitions, sumConstraint, result)
    elif sum(A) < sumConstraint:
        selectedElem = random.choice(M)
        selectedIndex = M.index(selectedElem)
        if sum(A) + selectedElem <= sumConstraint:
            M.pop(selectedIndex)
            A.append(selectedElem)
            solver(M, A, numPartitions, sumConstraint, result)
        else:
            if min(M) + sum(A) > sumConstraint:
                M.extend(A)
                A.clear()                
            solver(M, A, numPartitions, sumConstraint, result)

if __name__ == '__main__':
    S = [ 7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4 ]
    numPartitions = 5
    sumConstraint = 12
    result = []
    selectedElem =random.choice(S)
    selectedIndex = S.index(selectedElem)
    solver(S, [], numPartitions, sumConstraint, result)
    print(result)
