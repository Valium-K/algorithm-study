from functools import cmp_to_key
def cmp_play_or_else_index(a, b):
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        if a[1] < b[1]:
            return -1
        else:
            return 1

def solution(genres, plays):
    output = []
    albums = dict()
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in albums:
            albums[g].append((p, i))
        else:
            albums[g] = [(p, i)]

    most_played_genre = dict()
    for genre, play in albums.items():
        most_played_genre[genre] = sum(map(lambda x: x[0], play))
    most_played_genre = sorted(most_played_genre.items(), key=lambda x: x[1], reverse=True)

    for genre, total_plays in most_played_genre:
        ps = albums[genre]

        ps.sort(key=cmp_to_key(cmp_play_or_else_index))

        if len(ps) == 1:
            output.append(ps[0][1])
        elif len(ps) >= 2:
            output.append(ps[0][1])
            output.append(ps[1][1])

    return output


if __name__ == '__main__':
    solution(["classic", "pop", "classic", "classic", "pop"] ,	[500, 600, 150, 800, 2500])