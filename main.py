import reader
import writedb

file = 'categorias.csv'

cat = reader.read(file)
writedb.write(cat)