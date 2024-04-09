import pandas as pd
# Função para ler o arquivo e construir a matriz
def construir_matriz(arquivo_path):
    with open(arquivo_path, 'r') as arquivo:
        # Ler a primeira linha para obter o tamanho da matriz
        primeira_linha = arquivo.readline()
        # Processar a primeira linha para extrair o tamanho
        dimensoes = primeira_linha.strip().split(' ')
        xMatriz, yMatriz = int(dimensoes[0]), int(dimensoes[1])

        # Criar uma matriz vazia com as dimensões obtidas
        matriz = [[' ' for _ in range(yMatriz)] for _ in range(xMatriz)]

        # Processar cada linha restante para construir a matriz
        for i, linha in enumerate(arquivo):
            j = 0  # Índice da coluna na matriz
            k = 0  # Índice do caractere na linha
            while k < len(linha):
                char = linha[k]
                # Se for um dígito, verificar os dígitos consecutivos
                if char.isdigit():
                    numero = char
                    while k + 1 < len(linha) and linha[k + 1].isdigit():
                        numero += linha[k + 1]
                        k += 1
                    matriz[i][j] = int(numero)  # Converter para inteiro e adicionar na matriz
                elif char in ['/', '\\', '#', '-', ' ', '|']:
                    matriz[i][j] = char
                # Avançar os índices
                j += 1
                k += 1

    return matriz

arquivo_path = 'casos-cohen-noite\casoG50.txt'
"""df = pd.DataFrame(construir_matriz(arquivo_path))
nome_arquivo = 'dados.xlsx'
df.to_excel(nome_arquivo, index=False)"""


matriz_completa = construir_matriz(arquivo_path)
matriz_completa = matriz_completa[1:] # Remover a primeira linha vazia

def percorrer_matriz(matriz):
    total = 0
    x, y = 0, 0  # Começa no canto superior esquerdo
    direcao = 'direita'  # A direção inicial é para a direita
    xMatriz, yMatriz = len(matriz), len(matriz[0])  # Dimensões da matriz
    print (f'Dimensões da matriz: {xMatriz} x {yMatriz}')

    while True:
        elemento_atual = matriz[x][y]
        print(f'Posição atual: ({x}, {y}) ||| Elemento: {elemento_atual} ||| Direção: {direcao}')

        if elemento_atual == "#":
            print('Encontrado #, finalizando...')
            break

        # Se encontrar um número, soma ao total
        if isinstance(elemento_atual, int):
            total += elemento_atual
            print(f'Encontrado número: {elemento_atual} ||| Total acumulado: {total}')


        # Identifica o próximo movimento da trilha
        if direcao == 'direita':
            if matriz[x-1][y] == ' ' and matriz[x+1][y] == ' ':  # Se houver um espaço acima ou abaixo
                print("encerrando programa - vazio")
                break
            if elemento_atual == '\\' or elemento_atual == '/':
                if matriz[x-1][y] == ' ':
                    direcao = 'baixo'
                    x += 1
                elif matriz[x+1][y] == ' ':
                    direcao = 'cima'
                    x -= 1
            elif elemento_atual == '\\':
                direcao = 'baixo'
                x += 1
            elif elemento_atual == '/':
                direcao = 'cima'
                x -= 1
            else:
                y += 1
        elif direcao == 'esquerda':
            if matriz[x-1][y] == ' ' and matriz[x+1][y] == ' ':  # Se houver um espaço acima ou abaixo
                print("encerrando programa - vazio")
                break
            if elemento_atual == '\\' or elemento_atual == '/':
                if matriz[x-1][y] == ' ':
                    direcao = 'baixo'
                    x += 1
                elif matriz[x+1][y] == ' ':
                    direcao = 'cima'
                    x -= 1
            if elemento_atual == '\\':
                direcao = 'cima'
                x -= 1
            elif elemento_atual == '/':
                direcao = 'baixo'
                x += 1
            else:
                y -= 1
        elif direcao == 'baixo':
            if matriz[x][y-1] == ' ' and matriz[x][y+1] == ' ':  # Se houver um espaço acima ou abaixo
                print("encerrando programa - vazio")
                break
            if elemento_atual == '\\' or elemento_atual == '/':
                if matriz[x][y-1] == ' ':
                    direcao = 'direita'
                    y += 1
                elif matriz[x][y+1] == ' ':
                    direcao = 'esquerda'
                    y -= 1
            if elemento_atual == '\\':
                direcao = 'direita'
                y += 1
            elif elemento_atual == '/':
                direcao = 'esquerda'
                y -= 1
            else:
                x += 1
        elif direcao == 'cima':
            if matriz[x][y-1] == ' ' and matriz[x][y+1] == ' ':  # Se houver um espaço acima ou abaixo
                print("encerrando programa - vazio")
                break
            if elemento_atual == '\\' or elemento_atual == '/':
                if matriz[x][y-1] == ' ':
                    direcao = 'direita'
                    y += 1
                elif matriz[x][y+1] == ' ':
                    direcao = 'esquerda'
                    y -= 1
            if elemento_atual == '\\':
                direcao = 'esquerda'
                y -= 1
            elif elemento_atual == '/':
                direcao = 'direita'
                y += 1
            else:
                x -= 1


        # Verificar se saímos dos limites da matriz
        if x < 0 or x >= xMatriz or y < 0 or y >= yMatriz:
            print('Fora dos limites da matriz, finalizando...')
            break

    return total

total_recolhido = percorrer_matriz(matriz_completa)
print(f"Total: = {total_recolhido}")
