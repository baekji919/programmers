def solution(sizes):
    w, h = [], []
    for i in sizes:
        w.append(min(i))
        h.append(max(i))
    return max(w) * max(h)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # result : 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # result : 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # result : 133
