# Testando

import reader
import writedb
import insert
import show
import update
import drop

file = 'categorias.csv'

# cat = reader.read(file)
# writedb.write(cat, 'categories')
show.show('products', {})
update.update('products', {"Name": "Gin Tônica"}, {"Name": "Ciroc", "Description": "Bebida de gente rica"})
show.show('products')
# drop.delete('categories', 'Móveis')
# show.show('categories')