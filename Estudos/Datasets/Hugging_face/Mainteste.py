idorname = input('Digite o ID ou Nome do dataset: ')

def baixar_drive_dataset(idorname):
    if idorname.isdigit(): 
        print('É INTEIRO')
    else:
        print('É STRING')
baixar_drive_dataset(idorname)



def baixar_drive_dataset(idorname):
    if idorname.isdigit():  # Baixando pelo ID
        id = int(idorname)
        selecao_dataset = curtir_datasets[id - 1]
        print(f"\nBaixando o dataset '{selecao_dataset}'...")

        # Carregar o dataset via Hugging Face
        dataset = load_dataset(selecao_dataset)
        df = pd.DataFrame(dataset['train'])

        # Gerar o CSV em memória (sem salvar no computador)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)  # Voltar ao início do buffer para leitura

        # Salvar o CSV temporariamente no disco
        temp_file = f"dataset_{selecao_dataset}.csv"
        with open(temp_file, 'w') as f:
            f.write(csv_buffer.getvalue())
        
        print(f"Dataset salvo temporariamente como {temp_file}.")

        # Usar Google Drive CLI para fazer upload
        print("Iniciando upload para o Google Drive...")

        # Comando para o upload usando Google Drive CLI
        try:
            subprocess.run(["drive", "upload", temp_file], check=True)
            print(f"Dataset '{selecao_dataset}' enviado para o Google Drive.")
        except subprocess.CalledProcessError:
            print("Erro ao enviar o arquivo para o Google Drive.")

        # Remover o arquivo temporário após o upload
        os.remove(temp_file)
        print(f"Arquivo temporário '{temp_file}' removido.")

    else:
        print('Entrada inválida.')

# Chamar a função com o ID ou nome do dataset
baixar_drive_dataset(idorname)