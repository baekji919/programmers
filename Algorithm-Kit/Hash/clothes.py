def solution(clothes):
    answer = 1

    cl = {}
    for val, key in clothes:
        if key not in cl.keys():
            cl[key] = [val]
        else:
            cl[key] += [val]

    for k, v in cl.items():
        answer *= (len(v) +1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))