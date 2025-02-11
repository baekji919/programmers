import collections

# def solution(n, wires):
#     answer = -1
#     num = []
#     for i in range(len(wires)):
#         num.append(wires[i][0])
#         num.append(wires[i][1])
#     print(num)
#
#     counter = collections.Counter(num).most_common()
#     print(counter)
#     return answer
#
# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) ## result : 3
#print(solution(4, [[1,2],[2,3],[3,4]])) # result : 0
#print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) # result : 1