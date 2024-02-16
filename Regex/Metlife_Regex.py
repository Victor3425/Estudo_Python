import re 

cnpj = "RUA ITUPAVA 910  TERREO 80045305 16.794.464/0046-09"
texto = """{1: 'Demonstrativo de Comissões\nData Pagamento: 13/02/2023 Cod SUSEP\n00.00.02.1.211867.9\nCNPJ / CPF\nCAOA CORRETORA DE SEGUROS LTDA41.766.250/0001-14\nAVENIDA IBIRAPUERA 2822 SALA 05\nSAO PAULO - SP - 04028-002\nApólice /\nCertificadoEmpresa Endoss\noParcela Tipo\nComissãoVigência %\nComissãoBase\nCálculoPrêmio\nLiquido (R$)Valor Bruto\nComissão (R$)\nProdução\n718 Vida Grupo Corporate 93 Vida em Grupo\n79455006\n1368387.00\n006CONVEF ADMINISTRADORA DE\nCONSORCIOS LTDA589 56(C) Corretagem 11/2022 3,00 573,66 573,66 17,21\n79455004\n1368385.00\n004CAOA MONTADORA DE VEICULOS\nLTDA  - ANAPOLIS606 57(C) Corretagem 12/2022 3,00 16.133,11 16.133,11 483,99\nSub-Total: 501,20\nSub-Total (Produção) : 501,20\nSub-Total Produção: 16.706,77 501,20\n0,00 IRRF\n10,02 ISS\n0,00 INSS\n0,00 CSLL/PIS/COFINS\n491,18 Sub-Total sem impostos\n0,00 Adiantamentos\n491,18 TOTAL\nRecebi da METROPOLITAN LIFE SEGUROS E PREVIDENCIA PRIVADA SA CNPJ 02.102.498/0001-29  a importância acima especificada, através\nde DOC eletrônico na conta corrente 13065987-5 , do banco 33-SANTANDER 033, agência 2006-\nInformação sujeita a confirmação bancária.\n15/02/2023 10:33:08', 2: 'Demonstrativo de Comissões\nRESUMO GERAL:\nProdução: 501,20\n0,00 IRRF\n10,02 ISS\n0,00 INSS\n0,00 CSLL/PIS/COFINS\n491,18 Sub-Total sem impostos\n0,00 Adiantamentos\n491,18 TOTAL\n15/02/2023 10:33:08'}"""
texto2 = """Como calcular porcentagem de um valor no ExcelSelecione uma célula, digite "=", insira o valor inicial (ou o nome da célula), o sinal de "Multiplicação" (*), o valor da porcentagem, seguido de seu símbolo (%). Na prática, para calcular 20% de 200, ficará "=B2*20%". Aperte "Enter" para visualizar o valor final."""
texto3 = """Como calcular porcentagem de um valor no ExcelSelecione uma célula, digite "=", insira o valor inicial (ou o nome da célula), o sinal de 23342.456/233223 "Multiplicação" (*), o valor da porcentagem, 10908098 seguido de seu símbolo (%). Na prática, 234.345.22109 para calcular 20% de 200, ficará "=B2*20%". Aperte "Enter" para visualizar o valor final."""




pd = re.findall(r"[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0-9]{4}[-][0-9]{2}",cnpj)
#print(pd)

pd4 = re.findall(r"[0-9]{5}[.][0-9]{3}[/][0-9]{6}",texto3)
#print(pd4)

pd6 = re.findall(r"[0-9]{8}",texto3)
#print(pd6)

pd7 = re.findall(r"[0-9]{3}[.][0-9]{3}[.][0-9]{5}",texto3)
#print(pd7)

pd10 = pd4,pd6,pd7
print(pd10)

pd5 = re.findall(r"[a-z]{2}[a-z]{1}[a-z]{4}[a-z]{2}[a-z]{6}",texto2)
#print(pd5)

pd1 = re.compile(r"([0-9]{8}[\n][0-9]{7})[.]\d{0,2}[\n]\d{3}")
resu = pd1.search(texto)

if resu:
    teste = resu.group()
    
pd2 = re.findall(r"[0-9]{8}[\n][0-9]{7}[.]\d{0,2}[\n]\d{3}", texto)
#print(pd2)

pd3 = re.findall(r"[A-Z]{}[' ']+",texto)
#print(pd3)
 



#pd3 = re.findall(r"[A-Z][0-9]{3}[' ']\d{2}",texto)
#print(pd3)

#pd4 = re.findall(r"[' '][0-9]{2}[/]\d{4}[' ']",texto)
#print(pd4)

#pd5 = re.findall(r"[' '][0-9]{1}[,]\d{2}[' ']",texto)
#print(pd5)

#pd6 = re.findall(r"[' '][0-9]{0,9}[.]\d{0,9}[,]\d{2}[' ']", texto)
#print(pd6)

#pd = re.findall(r"[0-9]{3}[\n]\d{2}[0-9]{2}[/]\d{4}[\n]{1}[,]\d{2}[\n]{3}[,]\d{2}")








