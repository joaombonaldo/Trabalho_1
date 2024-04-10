import main 
caminho_do_arquivo = 'casos-cohen-noite/casoG2000.txt' 
matriz = main.criar_matriz_de_arquivo(caminho_do_arquivo)
total_recolhido = main.percorrer_matriz(matriz)
print(f"Total: = {total_recolhido}")