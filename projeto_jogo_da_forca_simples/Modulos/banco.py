import sqlite3

# Programa principal

def recebervalores(dados_banco):
    for index in range(0 ,len(dados_banco)):
        for posicao , valor in enumerate(dados_banco[index]):
            if posicao == 0:
                palavra = valor

            else:
                dica = valor
        add_dados(palavra = palavra , dica = dica)
    banco.close()

def add_dados(palavra , dica):
    try:
        cursor.execute(f'INSERT INTO palavras VALUES ("{palavra}","{dica}")')
        banco.commit()
    except sqlite3.Error as error:
        print(error)
    else:
        print('Deu certo')


def banco_de_dados():
    cursor.execute('SELECT * FROM palavras')
    return cursor.fetchall()

banco = sqlite3.connect('Palavras.db')

cursor = banco.cursor()

"""try:
    cursor.execute('CREATE TABLE palavras (palavra text , dica text)')
except sqlite3.Error:
    print('algo deu errado')
else:
    print('deu certo')"""





if __name__ == '__main__':
    print()
