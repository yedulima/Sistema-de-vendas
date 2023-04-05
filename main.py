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
        
class produtos:
    def select_produtos():
        
        apagar()
        prod = conexao.query(f"SELECT * FROM produtos")
        print(f"{'Lista de produtos': ^24}\n")
        print(f"{'Id': ^5}{'PRODUTO': ^11}{'PREÇO': ^10}\n------------------------")
        for id, nome, preco in prod:
            preco = "{:.2f}".format(preco)
            print(f"{f'{id}': ^4}|{f'{nome}': ^11}| R${preco}")
        print()

    def insert_produtos():
        
        produto = input("Produto: ").capitalize()
        preco = float(input("Preço do produto: "))
        
        ultimo_id = conexao.query("SELECT max(id) FROM produtos")
        
        conexao.execute(f"INSERT INTO produtos(id, nome, preco) VALUES({ultimo_id[0][0] + 1}, '{produto}', {preco})")

    def delete_produtos():
        
        running = True
        
        while running:
            
            apagar()
            produtos.select_produtos()
            id = input("Insira o id do produto: ")
            
            id = transformar(id)
            
            if type(id) == int:
                
                conexao.execute(f"DELETE FROM produtos WHERE id = {id}")
                
                while True:
                    
                    apagar()
                    perg = input("Deseja apagar mais algum produto? (S/N)\n>>>").upper()
                    
                    if perg == 'S':
                        break
                    elif perg == 'N':
                        running = False
                        break
                    else:
                        print("Refaça sua escolha")
            else:
                
                apagar()
                print(id)
                input()

    def update_produtos():
        
        while True:
            
            apagar()
            produtos.select_produtos()
            id = input("Insira o id do produto: ")
            
            id = transformar(id)
            
            if type(id) == int:
                
                produto = input("Insira um novo nome para ele: ").capitalize()
                preco = float(input("Insira um novo preço para ele: "))
                
                conexao.execute(f"UPDATE produtos SET nome = '{produto}', preco = {preco} WHERE id = {id}")
                
                break
            else:
                
                apagar()
                print(id)
                input()

while True:
    print("Teste de funcionamento de ")
