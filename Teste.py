import re
import os
import pandas as pd
from Abrir_Arquivo import ler_pdf
import timeit

def PDF_Sem_Senha_70(arquivo,planLog,log_caminho,excel_caminho,caminho_arquivo):
            tempo = timeit.timeit('math.sqrt(25)', setup='import math', number=1000000)
            tempo = str(tempo)
            tempo = tempo[16:]
            texto_do_pdf = ler_pdf(f'{caminho_arquivo}\{arquivo}')
            # texto_do_pdf = ler_pdf(f'{salvar}\Chery - 29402 - 003403071802 - 2023-12-14.pdf')
            # Criar um DataFrame com uma coluna chamada 'Texto', onde cada linha do texto se torna uma entrada
            df = pd.DataFrame({'Texto': texto_do_pdf.split('\n')})
            codigo = df[0:10]
            codigo = codigo.to_string(index=False)
            codigo = re.findall(r'[0-9]{3}/[0-9]{9}', codigo)
            codigo = ''.join(codigo)
            codigo = codigo.replace('/', '')

            endereco1 = df[11:12]
            endereco1 = endereco1.to_string(index=False)
            endereco1 = endereco1.strip()
            endereco1 = endereco1.replace('Texto', '')
            endereco1 = endereco1.replace('\n', '')
            endereco1 = endereco1.replace('/', '')

            endereco2 = df[12:13]
            endereco2 = endereco2.to_string(index=False)
            endereco2 = endereco2.strip()
            endereco2 = endereco2.replace('Texto', '')
            endereco2 = endereco2.replace('\n', '')
            endereco2 = endereco2.replace('/', '')

            endereco3 = df[13:15]
            endereco3 = endereco3.to_string(index=False)
            endereco3 = endereco3.strip()
            endereco3 = endereco3.replace('Texto', '')
            endereco3 = endereco3.replace('\n', '')
            endereco3 = endereco3.replace('/', '')
            endereco3 = endereco3.replace('.','')
            padrao = re.findall(r'(\d{5}-\d{3})', endereco3)
            padrao2 = re.findall(r'([A-Za-z]+\b)', endereco3)
            cep = padrao
            cidade = padrao2
            # cidadeSeparada = [palavra[:-2] + '' for palavra in cidadeSeparada]
            endereco3 = ''.join(endereco3)
            cep = ''.join(cep)
            cidade = ' '.join(cidade)
            UF = cidade[len(cidade) - 2:]
            # cidade = ''.join(elemento[0] + ''  for elemento in padrao2)
            cidade = cidade[0:len(cidade) - 2]
            cidade = cidade.strip()


            data_vencimento = df[44:45]
            data_vencimento = data_vencimento.to_string(index=False)
            data_vencimento = data_vencimento.strip()
            data_vencimento = data_vencimento.replace('Texto', '')
            data_vencimento = data_vencimento.replace('\n', '')

            valor = df[8:9]
            valor = valor.to_string(index=False)
            valor = valor.strip()
            valor = valor.replace('Texto', '')
            valor = valor.replace('\n', '')

            CNPJ = df[0:5]
            CNPJ = CNPJ.to_string(index=False)
            CNPJ = re.findall(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}', CNPJ)
            CNPJ = ''.join(CNPJ)

            forma_pagamento = df[10:11]
            forma_pagamento = forma_pagamento.to_string(index=False)
            forma_pagamento = forma_pagamento.strip()
            forma_pagamento = forma_pagamento.replace('Texto', '')
            forma_pagamento = forma_pagamento.replace('\n', '')

            # Nessa parte do codigo temos um regex, esse regex procura a palavra "Claro net virtua"
            # O \b corresponde a onde os caracteres especificados estao no inicio ou no final de uma palavra(O "r" no inicio garante que a string esta sendo tratada como uma "string bruta").
            # O ''.join() transforma o resultado do regex(que é uma lista) em string.
            descricao1 = df[0:]
            descricao1 = descricao1.to_string(index=False)
            descricao1 = str(descricao1)
            descricao1 = re.findall(r'\bNET VIRTUA\b', descricao1)
            descricao1 = ''.join(descricao1)
            descricao1 = descricao1.replace('NET VIRTUANET VIRTUANET VIRTUANET VIRTUANET VIRTUANET VIRTUA', 'NET VIRTUA +')


            descricao2 = df[17:19]
            descricao2 = df.to_string(index=False)
            descricao2 = str(descricao2)
            descricao2 = re.findall(r'\b NET Fone\b', descricao2)
            descricao2 = ''.join(descricao2)
            descricao = descricao1 + descricao2
            print(descricao2)

            cliente = df[43:44]
            cliente = cliente.to_string(index=False)
            cliente = cliente.strip()
            cliente = cliente.replace('Texto', '')
            cliente = cliente.replace('\n', '')

            # O ''.join() transforma o resultado do regex(que é uma lista) em string.
            # A tag \d representa qualquer digito numérico de 0 a 9. em termo simples, ele corresponde a qualquer numero.
            # A tag + significa um ou mais. Quando colocado apos
            ide_debito = df[50:51]
            ide_debito = ide_debito.to_string(index=False)
            #ide_debito = re.findall(r'NET SERVICOS \d+', ide_debito)
            ide_debito = ide_debito.replace('Texto','')
            ide_debito = ''.join(ide_debito)

            mes_referencia = df[0:]
            mes_referencia = mes_referencia.to_string(index=False)
            mes_referencia = re.findall(
                r'\b(?:Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)\/\d{4}\b',
                mes_referencia)
            mes_referencia = mes_referencia[0]
            mes_referencia = ''.join(mes_referencia)

            codigomes = mes_referencia.replace('/', '')

            codigo_barras = df[0:]
            codigo_barras = codigo_barras.to_string(index=False)
            codigo_barras = re.findall(r'\b\d+-\d\b', codigo_barras)
            codigo_barras = ''.join(codigo_barras)

            razao = df[0:]
            razao = razao.to_string(index=False)
            razao = re.findall(r'(Claro.*?S\.A)', razao)
            razao = ''.join(razao)

            razao2 = df[108:109]
            razao2 = razao2.to_string(index=False)
            razao2 = re.findall(r'[C][L][A][R][O][ ][S][.][A][.]', razao2)
            razao2 = ''.join(razao2)
            #print(df[10:20])
            #print(arquivo)
            print('-----------------------------------------------------')
            #print(len(df))
            print('-----------------------------------------------------')
            print('Segunda Via')
            print('Finalizado')

            print('-----------------------------------------------------')
            #os.rename(f'{caminho}\{arquivo}',
                     # f'{salvar}\Segunda_via - {codigo} - {codigomes} - {data}-{tempo}.pdf')
            planLog.append(
            {'A': razao +razao2, 'B': endereco1, 'C': endereco2, 'D': cep, 'E':cidade +" "+ UF, 'F': codigo, 'G': data_vencimento,
            'H': valor, 'I': CNPJ, 'J': forma_pagamento, 'K': descricao, 'L': cliente , 'M':ide_debito, 'N':mes_referencia, 'O':codigo_barras})
            #log_caminho.save(r"C:\Users\governanca.ti\OneDrive - Hyundai Caoa do Brasil Ltda\Notas Telecom\Fatura_Claro\Excel\Layout_Claro.xlsx")
            log_caminho.save(excel_caminho)

