import collections

def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] !=0:
            answer.append((100 - (progresses[i]))//speeds[i] +1)
        else:
            answer.append((100 - (progresses[i]))//speeds[i])
    print(answer)
    for i in range(len(answer)-1):
        if answer[i] > answer[i+1]:
            answer[i+1] = answer[i]

    counter = collections.Counter(answer)
    return list(counter.values())

print(solution([93, 30, 55], [1, 30, 5])) # resutl : [2, 1]
print(solution([95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1])) # result : [1, 3, 2]