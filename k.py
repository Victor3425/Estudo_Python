texto = [
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/9/',
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/998/',
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/999/',
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/1000/',
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/1001/',
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/1002/',
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/1143/',
'https://caoamontadora.sharepoint.com/sites/ChecklistInfra/Documentos Compartilhados/Anexos/1143/',
]

for a in texto:
    if len(a)>=92:
        print('93')
        print(a[90:])
    
    elif len(a) ==95:
        print('95')
        print(a[94:])  

    elif len(a) == 95:
        print('96')
        print(a[95:])      


