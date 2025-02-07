def solution(genres, plays):
    answer = []

    playDict = {}
    dict = {}
    for i in range(len(genres)):
        playDict[genres[i]] = playDict.get(genres[i], 0) + plays[i]
        dict[genres[i]] = dict.get(genres[i], []) + [(plays[i], i)]

    genreSort = sorted(playDict.items(), key=lambda x : x[1], reverse=True)
    for (genre, play) in genreSort:
        dict[genre] = sorted(dict[genre], key=lambda x : (-x[0], x[1]))

        answer += [idx for (play, idx) in dict[genre][:2]]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
## result : [4, 1, 3, 0]