def solution(brown, yellow):
    sum = brown + yellow
    li = []
    for i in range(1, sum):
        if sum % i == 0:
            li.append([i, sum//i])

    for x in li:
        if x[0] >= x[1] and x[0]*x[1] == sum and (x[0]-2)*(x[1]-2) == yellow:
            return x

#print(solution(10,2)) # result = [4, 3]
print(solution(8, 1)) # result = [3, 3]
print(solution(24, 24)) # result = [8, 6]