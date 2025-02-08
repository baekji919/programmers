def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    print(citations)

    #return max(map(min, enumerate(citations, start= 1)))
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return (len(citations))

print(solution([3, 0, 6, 1, 5]))
# result : 3
print(solution([3, 0, 6, 1, 5, 12, 10]))
# result : 3