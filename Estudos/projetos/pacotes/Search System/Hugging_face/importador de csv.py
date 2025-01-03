from huggingface_hub import HfApi, login
from datasets import load_dataset, get_dataset_config_names
import pandas as pd
# Realiza login na Hugging Face com o token
login(token="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")
api = HfApi()
curtir_datasets = api.list_liked_repos().datasets

# Verificar se o usuário curtiu algum dataset
if curtir_datasets:
    print("Datasets curtidos:")
    for i, dataset in enumerate(curtir_datasets):
        print(f"{i + 1}. {dataset}")
else:
    print('Rpz...esqueceu de curtir?')

# Obter o ID ou nome do dataset
idorname = input('Digite o ID ou Nome do dataset: ')

def baixar_computador(idorname):
    if idorname.isdigit():
        id = int(idorname)
        dataset = load_dataset(curtir_datasets[id - 1], cache_dir="C:/Users/eyluc/Documents/ESTUDO -- 'data scientist'/Eydatascience/Estudos/Datasets")
        print(f"Dataset '{curtir_datasets[id - 1]}' baixado com sucesso.")
    else:
        print("Por favor, insira um número válido.")



s = get_dataset_config_names(curtir_datasets[int(idorname) - 1])
print(curtir_datasets[int(idorname) - 1])
if len(s) > 1 : 
    for index, nameconfig in enumerate(s, 1): 
        #d = load_dataset(curtir_datasets[int(idorname) - 1], nameconfig) - ({len(d["train"])})
        print(f'{index} - {nameconfig} ')
else: 
    if s: 
        print('possui apenas uma split: train')