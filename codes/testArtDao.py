from ArtDao import artDao

art1 = {
    'id':2,
    'title': 'Scream',
    'author': 'Munk',
    'price': 500

}
art2 = {
    'id':2,
    'title': 'blue sky',
    'author': 'J.K.R',
    'price': 999

}

#returnValue = artDao.create(art)
returnValue = artDao.getAll()
print(returnValue)

returnValue = artDao.update(art2)
print(returnValue)

returnValue = artDao.findById(art2['id'])
print ("find By Id")
print(returnValue)

returnValue = artDao.delete(art2['id'])
print(returnValue)

returnValue = artDao.getAll()
print(returnValue)
