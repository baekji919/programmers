from itertools import permutations

def solution(numbers):
    # 방법 1
    # number_list = list(map(''.join, permutations(list(map(str, numbers)))))
    #
    # return max(number_list)

    ## 방법 2
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x: x*3 , reverse=True)

    return str(int(''.join(numbers)))



print(solution([6, 10, 2]))
# result : "6210"
print(solution([3, 30, 34, 5, 9]))
# result : "9534330"