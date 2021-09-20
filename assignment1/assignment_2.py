def top_ten_and_least_watched_movie_according_to_imdb():
    import json

    d = {}

    f = open("assignment.json", "r")

    q = json.load(f)

    for i in range(0, len(q)):
        d[q[i]['name']] = q[i]['imdb_score']

    # print(d)

    q1 = list(d.items())
    q2 = sorted(q1, key=lambda x: x[1], reverse=True)
    # print(q2)

    print("The top 10 movies are: \n")
    for i in range(0, len(q2)):
        if i > 9:
            break
        else:
            print(q2[i][0])

    print("\nThe least watched movie is:", end=' ')
    s1, s2 = min(q1, key=lambda x: x[1])
    print(s1)

    f.close()


def most_popular_director_in_top_100_movies():
    import json

    d1 = {}

    f = open("assignment.json", "r")

    q = json.load(f)

    for i in range(0, len(q)):
        if i > 99:
            break
        else:
            d1[q[i]['director']] = q[i]['99popularity']

    # print(d1)

    s = d1.items()
    s1 = sorted(s, key=lambda x: x[1], reverse=True)

    print("The most popular director in 1st 100 movies is:", end=' ')
    print(s1[0][0])

    f.close()


def director_with_most_no_of_films():
    import json

    d = {}

    f = open("assignment.json", "r")

    q = json.load(f)

    # print(q[0])

    for i in range(0, len(q)):
        if q[i]['director'] not in d:
            d[q[i]['director']] = 1
        else:
            d[q[i]['director']] += 1

    # print(d)
    x = d.items()
    x1 = sorted(x, key=lambda x: x[1], reverse=True)

    print("The director with most no of films is:", end=' ')
    print(x1[0][0])

    f.close()


def most_watched_genre():
    import json

    d = {}
    list1 = []

    f = open("assignment.json", "r")

    q = json.load(f)

    for i in range(0, len(q)):
        h = q[i]['genre']
        for j in range(0, len(h)):
            if h[j].strip(' ') not in d:
                d[h[j].strip(' ')] = 1
            else:
                d[h[j].strip(' ')] += 1

    # print(d)

    q1 = d.items()
    q2 = sorted(q1, key=lambda x: x[1], reverse=True)

    print("The most watched genre is:", end='')
    print(q2[0][0])

    f.close()


'''
Uncomment each one of the following to know the answers to the queries.

'''

# top_ten_and_least_watched_movie_according_to_imdb()

# most_popular_director_in_top_100_movies()

# director_with_most_number_of_films()

# most_watched_genre()

