import movieposters as mp

link = mp.get_poster(title='breakfast club')
# link = mp.get_poster(id='tt0088847')  # can also be found using movie's id
# link = mp.get_poster(id=88847)

print(link)
