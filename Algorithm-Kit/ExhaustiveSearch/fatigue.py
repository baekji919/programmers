from itertools import permutations
def solution(k, dungeons):
    li = list(permutations(dungeons))

    cnt = []
    for x in range(len(li)):
        sum = 0
        k2 = k
        for i in li[x]:
            if k2 >= i[0]:
                sum += 1
                k2 -= i[1]
        cnt.append(sum)

    answer = max(cnt)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]])) ## result = 3