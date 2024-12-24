from huggingface_hub import HfApi, login
from datasets import load_dataset
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

import os

login(token="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")
api = HfApi()
curtir_datasets = api.list_liked_repos().datasets

# Verificar se eu curtir kkkkk ou esqueci
if curtir_datasets:
    print("Datasets curtidos:")
    for i, dataset in enumerate(curtir_datasets):
        print(f"{i + 1}. {dataset}")
else:
    print('Rpz...esqueceu de curtir?')

idorname = input('Digite o ID ou Nome do dataset: ')



def baixar_drive_dataset(idorname):
    if idorname.isdigit(): 
        id = int(idorname)
        selecao_dataset = curtir_datasets[id - 1]
        print(f"\nBaixando o dataset '{selecao_dataset}'...")
        
        # Carregar o dataset
        dataset = load_dataset(selecao_dataset)
        
        # Converter a divisão 'train' para DataFrame (ou outra divisão, como 'test' ou 'validation')
        df = pd.DataFrame(dataset['train'])  # Aqui escolhemos a divisão 'train'
        
        # Definir o caminho para o arquivo CSV
        file_path = f"dataset_{selecao_dataset}.csv"
        
        # Verificar se o diretório existe, caso contrário, criar
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        
        # Salvar como CSV
        df.to_csv(file_path, index=False)

        # Autenticação no Google Drive
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()  # Abre o navegador para autenticação
        drive = GoogleDrive(gauth)
        file = drive.CreateFile({"title": f"dataset_{selecao_dataset}.csv"})
        file.SetContentFile(file_path)
        file.Upload()
        print(f"Dataset enviado para o Google Drive: {file['title']}")
        
    else:
        print('Entrada inválida.')

baixar_drive_dataset(idorname)