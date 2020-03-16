from fenwicktree_rangequery_pointupdate import FenwickTreeRangeQueryPointUpdate


# Problem:
#   You are given an empty array. Process Q queries of the following problems:
#   [1, v, i]: insert 'v' at position 'i'
#   [2, i, j]: find the count of numbers in the range [i, j] in the array.
#   Return an integer array denoting the answer of each query
# 
# Constraints:
#   1 <= Q <= 2*10^5
#   1 <= v <= 10^9
#   1 <= i <= j <= 10^9
#
# Input:
#   Q = [
#         [1, 2, 1]
#         [1, 5, 3] 
#         [2, 1, 10] 
#         [1, 5, 5] 
#         [2, 2, 5]
#        ]
# Output:
#   [2, 3]
#
# Approach:
# 1- Using a Fenwick Tree, we are going to create a tree
# of the length of the maximum range of 'v': 10^9, where
# each element is initialized to zero.
# For each insertion operation we are going to set the value
# at that point to one, (log 10^9) operation
# For each count we are going to calculate the range sum of
# the interval [i, j], (log 10^9) operation
# Time complexity: len(Q) * log 10^9
# Space complexity: 10^9
# If we take 8 bytes for each array element that would be
# about 8 giga bytes of memory without compression

# BEWARE: Fenwick Tree is One-Based!

Q = [
    [1, 2, 1],
    [1, 5, 3],
    [2, 1, 10], 
    [1, 5, 5],
    [2, 2, 5],
    [1, 5, 2],
    [2, 2, 5]
    ]
res = []
ft = FenwickTreeRangeQueryPointUpdate((10**2)+1)
for op, *operands in Q:
    if op == 1:
        val, index = operands
        ft.set(index+1, 1)
    else:
        left, right = operands
        res.append(ft.range_sum(left+1, right+1))

print(res) # prints [2, 2, 3]