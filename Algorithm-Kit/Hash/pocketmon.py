def solution(nums):

    poket = set(nums)

    if len(poket) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(poket)
    return answer