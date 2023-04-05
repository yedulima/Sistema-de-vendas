import conect as con
import os

conexao = con.Connection()

clear = 'clear'

def apagar():
    os.system(clear)

def transformar(indice):
    try:
        indice = int(indice)
        return indice
    except:
        return "Deve ser número"
        

def select_produtos():
    apagar()
    prod = conexao.query(f"SELECT * FROM produtos")
    print(f"{'Lista de produtos': ^24}\n")
    print(f"{'Id': ^5}{'PRODUTO': ^11}{'PREÇO': ^10}\n------------------------")
    for id, nome, preco in prod:
        print(f"{f'{id}': ^4}|{f'{nome}': ^11}| R${preco}")
    print()

def insert_produtos():
    produto = input("Produto: ").capitalize()
    preco = float(input("Preço do produto: "))
    
    ultimo_id = conexao.query("SELECT max(id) FROM produtos")
    
    conexao.execute(f"INSERT INTO produtos(id, nome, preco) VALUES({ultimo_id[0][0] + 1}, '{produto}', {preco})")

def delete_produtos():
    while True:
        apagar()
        select_produtos()
        id = input("Insira o id do produto: ")
        
        id = transformar(id)
        
        if type(id) == int:
            conexao.execute(f"DELETE FROM produtos WHERE id = {id}")
            break
        else:
            apagar()
            print(id)
            input()

insert_produtos()
delete_produtos()
select_produtos()