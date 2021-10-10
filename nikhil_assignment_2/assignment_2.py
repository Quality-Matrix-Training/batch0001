def leastwatched_and_mostwatched_films():
    
    import json

    f = open('repeat_imdb.json', mode='r')
    q = f.read()
    q1 = json.loads(q)
    l = []
    l1 = []
    d = {}


    for i in range(0, len(q1)):
        if q1[i]['name'] == 'The Wizard of Oz' or q1[i]['name'] == 'Batman':
            l.append(q1[i]['name'])
            l.append(q1[i]['imdb_score'])
            l1.append(l)
            l = []


    for j in range(0, len(q1)):
        d[q1[j]['name']] = q1[j]['imdb_score']


    for k1, k2 in l1:
        if d[k1] != k2:
            d[k1.lower()] = k2


    w = d.items()
    w1 = sorted(w, key=lambda x:x[1])
    w2 = sorted(w, key=lambda x:x[1], reverse=True)

    print("The least watched movie is:",w1[0][0])

    print("\nThe 10 most watched movies are:")
    for k in range(0, len(w2)):
        if k > 9:
            break
        else:
            print(w2[k][0])
            
            
def most_popular_director_in_top100_movies():
    import json

    f = open('repeat_imdb.json', mode='r')
    q = f.read()
    q1 = json.loads(q)

    l = []
    l1 = []
    d = {}
    d1 = {}

    for i in range(0, len(q1)):
        if q1[i]['name'] == 'The Wizard of Oz' or q1[i]['name'] == 'Batman':
            l.append(q1[i]['name'])
            l.append(q1[i]['imdb_score'])
            l1.append(l)
            l = []


    for j in range(0, len(q1)):
        d[q1[j]['name']] = q1[j]['imdb_score']

    for k1, k2 in l1:
        if d[k1] != k2:
            d[k1.lower()] = k2


    w = d.items()
    w1 = sorted(w, key=lambda x:x[1], reverse=True)

    for i in range(0, len(w1)):
        if i > 99:
            break
        else:
            e1, e2 = w1[i]
            for j in range(0, len(q1)):
                if e1 == 'the wizard of oz':
                    e1 = 'The Wizard of Oz'
                    if q1[j]['name'] == e1 and q1[j]['imdb_score'] == e2:
                        if q1[j]['director'] not in d1:
                            d1[q1[j]['director']] = [q1[j]['99popularity']]
                        else:
                            d1[q1[j]['director']].append(q1[j]['99popularity'])


                elif e1 == 'batman':
                    e1 = 'Batman'
                    if q1[j]['name'] == e1 and q1[j]['imdb_score'] == e2:
                        if q1[j]['director'] not in d1:
                            d1[q1[j]['director']] = [q1[j]['99popularity']]
                        else:
                            d1[q1[j]['director']].append(q1[j]['99popularity'])

                else:

                    if q1[j]['name'] == e1:
                        if q1[j]['director'] not in d1:
                            d1[q1[j]['director']] = [q1[j]['99popularity']]
                        else:
                            d1[q1[j]['director']].append(q1[j]['99popularity'])



    w = d1.items()
    w1 = sorted(w, key=lambda x:sum(x[1])/len(x[1]), reverse=True)
    print("The most poplular director in top 100 films is:",w1[0][0])
    f.close()

    
def director_with_most_no_of_films():
    
    import json

    f = open('repeat_imdb.json', mode = 'r')
    q = f.read()
    q1 = json.loads(q)
    d = {}

    for i in range(0, len(q1)):
        if q1[i]['director'] not in d:
            d[q1[i]['director']] = 1
        else:
            d[q1[i]['director']] += 1

    w = d.items()
    w1 = sorted(w, key=lambda x:x[1], reverse=True)
    print("The director with most no of films is:",w1[0][0])

    f.close()
    

def most_watched_genre():
    
    import json

    f = open('repeat_imdb.json', mode='r')
    q = f.read()
    q1 = json.loads(q)
    l = []
    d = {}

    for i in range(0, len(q1)):
        e = q1[i]['genre']
        for j in range(0, len(e)):
            if e[j].strip(' ') not in d:
                d[e[j].strip(' ')] = 1
            else:
                d[e[j].strip(' ')] += 1

    w = d.items()
    w1 = sorted(w, key=lambda x:x[1], reverse=True)
    print("The most watched genre is:",w1[0][0])
    f.close()
    
    
'''   
Uncomment the below function calls one after the other to invoke their definitions and get the 
answers for the queries.

'''
# leastwatched_and_mostwatched_films()
# most_popular_director_in_top100_movies()
# director_with_most_no_of_films()
# most_watched_genre()

