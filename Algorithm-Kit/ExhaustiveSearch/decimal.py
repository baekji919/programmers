from itertools import permutations
def solution(numbers):
    answer = 0
    print(list(numbers))

    li = permutations(list(numbers))
    print(list(li))
    return answer

print(solution("17")) #result : 3
#print(solution("011")) # result : 2