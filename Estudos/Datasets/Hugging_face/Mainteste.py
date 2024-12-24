idorname = input('Digite o ID ou Nome do dataset: ')

def baixar_drive_dataset(idorname):
    if idorname.isdigit(): 
        print('É INTEIRO')
    else:
        print('É STRING')
baixar_drive_dataset(idorname)
