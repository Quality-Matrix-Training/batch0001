# opening json files and reading the data in it
import json

with open("imdb_movies.json", mode='r', newline='\n') as f:
    data = json.load(f)


# print(data)

# 1.Top director with maximum number of movies
def top_director_with_max_movies():
    d_mov = {}
    for i in range(0, len(data)):
        if data[i]['director'] not in d_mov:
            d_mov[data[i]['director']] = []

        d_mov[data[i]['director']].append(data[i]['name'])

    # print(d_mov)

    top_director = max(d_mov.items(), key=lambda x: len(x[1]))
    print("1.The top director with maximum movies is '{}'".format(top_director[0]))
    print()


# 2.Popular genre watched by the audiance:
def popular_genre_watched():
    gen_dict = {}

    for i in range(0, len(data)):
        e = data[i]['genre']
        for j in range(0, len(e)):
            f = e[j].strip()  # stripping any extra spaces for the strings
            if f not in gen_dict:
                gen_dict[f] = 1
            else:
                gen_dict[f] += 1

    # print(gen_dict)

    pop_gen = max(gen_dict.items(), key=lambda x: x[1])
    print("2.The most watched genre by the audiance is '{}'".format(pop_gen[0]))
    print()


# movies along with their imdb scores
imdb_movies = {}

for i in range(0, len(data)):
    x = data[i]['name']
    y = data[i]['imdb_score']
    if x not in imdb_movies:
        imdb_movies[x] = y


# print(imdb_movies)

# 3.Top 10 movies according to imdb score:
def top_imdb_movies():
    top_10_mov = []

    imdb_sort_rev = sorted(imdb_movies.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 10):
        top_10_mov.append(imdb_sort_rev[i])

    print("3.The top 10 imdb movies are {}".format(top_10_mov))
    print()


# 4.Least watched movie based on imdb score
def least_watched_movie():
    imdb_sort = sorted(imdb_movies.items(), key=lambda x: x[1])

    # print(imdb_sort)
    print("4.The least watched movie as per imdb score is '{}'".format(imdb_sort[0][0]))
    print()


# 5.Best director in the first hundred movies:
def best_director():
    first_100 = {}

    for i in range(0, 100):
        p = data[i]['director']
        q = data[i]['99popularity']
        if p not in first_100:
            first_100[p] = q

    best_director = max(first_100.items(), key=lambda x: x[1])
    print("5.Best director in the first hundred movies is '{}'".format(best_director[0]))
    print()


# 1.Top director with maximum number of movies
top_director_with_max_movies()
# 2.Popular genre watched by the audiance:
popular_genre_watched()
# 3.Top 10 movies according to imdb score:
top_imdb_movies()
# 4.Least watched movie based on imdb score
least_watched_movie()
# 5.Best director in the first hundred movies:
best_director()