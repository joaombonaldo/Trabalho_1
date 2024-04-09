# Vamos começar lendo o conteúdo do arquivo e transformando os dados em uma matriz 50x50.
# O arquivo contém caracteres especiais que devem ser ignorados, mantendo apenas os números e espaços.

# Primeiro, leremos o arquivo para entender como os dados estão organizados.
arquivo_path = 'casos-cohen-noite\casoG50.txt'

# Abrir o arquivo e ler as linhas
with open(arquivo_path, 'r') as arquivo:
    linhas = arquivo.readlines()

# As primeiras linhas contêm informações sobre o tamanho da matriz, que já sabemos ser 50x50.
# Podemos ignorar essa linha e focar na construção da matriz a partir do conteúdo restante.
# Criaremos uma matriz 50x50 inicialmente preenchida com zeros, e então substituiremos os zeros pelos números encontrados.

# Recriar a matriz 50x50 inicialmente preenchida com espaços, em vez de zeros, para refletir a ausência de informação.
matriz_completa = [[' ' for _ in range(50)] for _ in range(50)]

# Processar cada linha do arquivo novamente, desta vez incluindo caracteres especiais e números.
for i, linha in enumerate(linhas[1:]):  # Ignorar a primeira linha com as dimensões
    for j, char in enumerate(linha):
        if char.isdigit():
            # Verificar se é um número de dois dígitos
            if j + 1 < len(linha) and linha[j+1].isdigit():
                matriz_completa[i][j] = char + linha[j+1]  # Concatenar dois dígitos
                matriz_completa[i][j+1] = ' '  # Marcar o próximo espaço como vazio para evitar duplicação
            elif matriz_completa[i][j] != ' ':  # Se o espaço atual não foi marcado como parte de um número de dois dígitos
                matriz_completa[i][j] = char
        elif char in ['/', '\\', '#', '|', '-', ' ']:  # Incluir caracteres especiais e espaço
            matriz_completa[i][j] = char

# Devido à inclusão de números de dois dígitos, pode haver espaços extras marcados. Vamos limpar esses espaços.
matriz_completa = [[' ' if cell == '' else cell for cell in row] for row in matriz_completa]
matriz_completa = matriz_completa[1:] # Remover a primeira linha vazia
print (matriz_completa) # Exibir a matriz completa para verificar a conversão



