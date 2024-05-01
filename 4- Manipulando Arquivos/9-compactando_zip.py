# 9 - Compactando Arquivos em Zip

#1. Nessa aula vamos aprender manipular arquivos dentro de diretórios.
#2. Vamos utilizar três módulos builtin que vão nos ajudar a buscar dados dentro de um diretório de trabalho, para que consigamos listar arquivos e compactar arquivos.

import glob, os 
import zipfile

os.getcwd() # Diretório atual de trabalho

# 1 - Lista todos os arquivos .txt
for file in glob.glob("*.txt"):
    print(file)
        
# 2 - Lista todos os arquivos .csv
for file in glob.glob("*.csv"):
    print(file)
    
# 3 - Compactando arquivos .txt
with zipfile.ZipFile('names.zip', 'w') as f:
    for file in glob.glob('*.txt'):
        f.write(file)
        
# 4 - Compactando arquivos .csv
with zipfile.ZipFile('languagens.zip', 'w') as f:
    for file in glob.glob('*.csv'):
        f.write(file)
        
# 5 - Compactando todos os arquivos
with zipfile.ZipFile('code.zip', 'w') as f:
    for file in glob.glob('*'):
        f.write(file)