def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    r1, r2, r3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == p1[i%len(p1)]: r1 +=1
        if answers[i] == p2[i%len(p2)]: r2 +=1
        if answers[i] == p3[i%len(p3)]: r3 +=1

    if r1 == max(r1, r2, r3):
        answer.append(1)
    if r2 == max(r1, r2, r3):
        answer.append(2)
    if r3 == max(r1, r2, r3):
        answer.append(3)
    return answer

print(solution([1,2,3,4,5])) # result : [1]
print(solution([1,3,2,4,2])) # result : [1, 2, 3]
