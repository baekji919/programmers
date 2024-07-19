def solution(arr, queries):
    answer = []
    for i in queries:
        temp = []
        for j in range(i[0], i[1]+1):
            if arr[j] > i[2]:
                temp.append(arr[j])
        if temp != []:
            answer.append(min(temp))
        else:
            answer.append(-1)

    return answer