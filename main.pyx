import time

def criar_matriz_de_arquivo(caminho_do_arquivo):
    print ("começou a construir a matriz")
    with open(caminho_do_arquivo, 'r') as arquivo:
        # Ler a primeira linha para obter as dimensões da matriz
        linhas, colunas = map(int, arquivo.readline().strip().split())
        matriz = [[' ' for _ in range(colunas)] for _ in range(linhas)]  # Usando espaço como valor padrão
        
        # Pular linhas vazias até encontrar a primeira linha de dados
        linha = arquivo.readline()
        while linha and not linha.strip():
            linha = arquivo.readline()
        
        # Processar os dados para formar a matriz
        row = 0
        while linha:
            if row >= linhas:  # Para evitar ler mais linhas do que o necessário
                break
            
            dados = linha[:colunas + 1]  # Leva em conta o caractere de nova linha ao cortar a linha
            for col, char in enumerate(dados):
                if col < colunas:  # Assegura que não excederemos o limite de colunas
                    matriz[row][col] = char if char.strip() else ' '  # Trata espaços em branco corretamente
            
            row += 1
            linha = arquivo.readline()

    return matriz


#########################################
def encontrar_inicio(matriz):
    print ("começou a encontrar o inicio")
    for i, linha in enumerate(matriz):
        if matriz[i][0] == '-':
            return i              
########################################
        
def percorrer_matriz(matriz):
    print ("começou a percorrer")
    total = 0
    x = encontrar_inicio(matriz)
    y = 0 
    direcao = 'direita'  # A direção inicial é para a direita
    xMatriz, yMatriz = len(matriz), len(matriz[0])  # Dimensões da matriz
    Cords = []
    straux = ''
    
    print ("começou a percorrer a matriz WHILE")
    while True:
        elemento_atual = matriz[x][y]
        #print(f'Posição atual: ({x}, {y}) ||| Elemento: {elemento_atual} ||| Direção: {direcao}')

        if elemento_atual == "#":
            print('Encontrado #, finalizando...')
            break
        
        # Se encontrar um número, soma ao total
        if elemento_atual.isnumeric():
            straux += elemento_atual
            # Verificar se o número já foi encontrado
            if [x,y] not in Cords:
                #print(f'Encontrado número: {elemento_atual} ||| Total acumulado: {total}')
                Cords.append([x,y])
        else:
            if straux is not '':
                total += int(straux)
                straux = ''
            


        # Identifica o próximo movimento da trilha  
        if direcao == 'direita':
            if elemento_atual == '\\':
                direcao = 'baixo'
                x += 1
            elif elemento_atual == '/':
                direcao = 'cima'
                x -= 1
            else:
                y += 1
        elif direcao == 'esquerda':
            if elemento_atual == '\\':
                direcao = 'cima'
                x -= 1
            elif elemento_atual == '/':
                direcao = 'baixo'
                x += 1
            else:
                y -= 1
        elif direcao == 'baixo':
            if elemento_atual == '\\':
                direcao = 'direita'
                y += 1
            elif elemento_atual == '/':
                direcao = 'esquerda'
                y -= 1
            else:
                x += 1
        elif direcao == 'cima':
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
    print (f'Dimensões da matriz: {xMatriz} x {yMatriz}')
    return total

inicio = time.time()
caminho_do_arquivo = 'casos-cohen-noite/casoG2000.txt'  # Exemplo com o primeiro arquivo
matriz = criar_matriz_de_arquivo(caminho_do_arquivo)
total_recolhido = percorrer_matriz(matriz)
print(f"Total: = {total_recolhido}")
fim = time.time()
print(f'Tempo de execução: {fim - inicio}')


