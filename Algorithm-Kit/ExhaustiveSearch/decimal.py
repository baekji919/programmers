import math
from itertools import permutations
def solution(numbers):
    answer = 0

    li = []
    for i in range(1, len(numbers)+1):
        li += map(int, map(''.join, permutations(list(numbers), i)))

    # for num in set(li):
    #     if num != 0 or num != 1:
    #         cnt = 0
    #         for x in range(2, num+1):
    #             if num % x == 0:
    #                 cnt += 1
    #         if cnt == 1:
    #             answer += 1

    answer += sum(1 for num in set(li) if num > 1 and all(num % x != 0 for x in range(2, num)))

    return answer

print(solution("17")) #result : 3
print(solution("011")) # result : 2