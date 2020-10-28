import reader
import writedb
import insert
import show

file = 'categorias.csv'

cat = reader.read(file)
writedb.write(cat, 'categories')
show.show('categories')        