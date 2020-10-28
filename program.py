import reader
import writedb
import insert
import show
import drop

fields = ["Name", "Description", "Value", "Categories"]

while(1):
    print('''Options:
    [0] - Create Product
    [1] - Read Product
    [2] - Update Product
    [3] - Delete Product
    [4] - Exit''')
    opt = input("What option would you like to do:")
    if(int(opt) == 0):
        print("selecionou criar")
        insert.create()
    elif(int(opt) == 1):
        print("selecionou ler")
    elif(int(opt) == 2):
        print("selecionou editar")
    elif(int(opt) == 3):
        print("selecionou excluir")
    elif(int(opt) == 4):
        print("bye")
        break