import collections
def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    ## collections.Counter 사용 방법
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys())[0])

    ## 리스트로 풀기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

