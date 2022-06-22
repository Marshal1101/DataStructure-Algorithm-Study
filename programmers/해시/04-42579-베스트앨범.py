from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [800, 600, 800, 800, 2500]	

def solution(genres, plays):
    answer = []
    
    length = len(plays)
    
    genre_total_plays = defaultdict(int)
    genre_play_idx = defaultdict(list)
    for i in range(length) :
        genre_play_idx[genres[i]].append((plays[i], i))
        genre_total_plays[genres[i]] += plays[i]
    
    # print(genre_play_idx)
    # print(genre_total_plays)
    total_res = []
    for key, value in genre_total_plays.items() :
        total_res.append((value, key))

    total_res.sort(reverse=True)
    for play, genre in total_res :
        temp = list(genre_play_idx[genre])
        temp.sort(key=lambda x: (x[0], -x[1]))
        for _ in range(2) :
            if temp :
                p, idx = temp.pop()
                answer.append(idx)

    return answer

print(solution(genres, plays))