from datasets import load_dataset
import pandas as pd
import os

# Caminho de saída para o arquivo CSV
output_csv = r"C:\Users\eyluc\Documents\ESTUDO -- 'data scientist'\Eydatascience\Estudos\Datasets\csv\agricultural_dataset.csv"

# Carregar o dataset
dataset = load_dataset("Solshine/Reflection-Tuning-Natural-Farming_Agricultural-Dataset")

# Verificar as chaves (splits) do dataset
print("Dataset Keys (Splits):", dataset.keys())

# Verificar os recursos do primeiro split (se disponível)
if len(dataset) > 0:
    first_split = list(dataset.keys())[0]  # Obter o nome do primeiro split
    print(f"Features of '{first_split}' split:", dataset[first_split].features)
    
    # Criar o DataFrame a partir do primeiro split
    df = pd.DataFrame(dataset[first_split])  
    
    # Garantir que o diretório de saída exista
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    # Salvar como CSV
    df.to_csv(output_csv, index=False)
    print(f"Dataset baixado e salvo como {output_csv}")
else:
    print("Dataset está vazio. Verifique o nome ou a configuração do dataset.")
