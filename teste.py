# Função para ler o arquivo e construir a matriz
def ler_arquivo_e_construir_matriz(arquivo_path):
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
                elif char in ['/', '\\', '#', '-', ' ']:
                    matriz[i][j] = char
                # Avançar os índices
                j += 1
                k += 1

    return matriz

# Caminho do arquivo
arquivo_path = 'casos-cohen-noite\casoG50.txt'

# Chamada da função
matriz_completa = ler_arquivo_e_construir_matriz(arquivo_path)
print (matriz_completa) # Exibir a matriz completa para verificar a conversão