"""
https://www.coursera.org/learn/algorithmic-toolbox/resources/3r3Mv
Find the maximum product of two distinct numbers
in a sequence of non-negative integers.
Input:
3
1 2 3
Output:
6
"""
import random
"""
There are two solutions
- Sort the array and get the first 2 elements - O(nlogn)
- Get the biggest number in a loop and in a 2nd loop get biggest-1 - O(n)
"""


def max_pairwise_product(numbers):
    max1 = 0
    index1 = 0
    for index, num in enumerate(numbers):
        if num > max1:
            max1 = num
            index1 = index

    max2 = 0
    index2 = 0
    for index, num in enumerate(numbers):
        if (num > max2) and (index1 != index):
            max2 = num
            index2 = index
    return numbers[index2] * numbers[index1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]

    # my stress test
    #input_numbers = [random.randint(0, 10) for n in range(3)]
    print(input_numbers)
    print(max_pairwise_product(input_numbers))
