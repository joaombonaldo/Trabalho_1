def criar_matriz_de_arquivo(caminho_do_arquivo):
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

# Usar a função para ler um dos arquivos e imprimir a matriz resultante
caminho_do_arquivo = 'casos-cohen-noite/casoG50.txt'  # Exemplo com o primeiro arquivo
matriz = criar_matriz_de_arquivo(caminho_do_arquivo)
for linha in matriz:
    print(''.join(linha))
