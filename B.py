import pdfplumber

def ler_pdf(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        # Itera pelas páginas do PDF
        for num_pagina in range(len(pdf.pages)):
            # Obtém uma página específica
            pagina = pdf.pages[num_pagina]
            
            # Extrai o texto da página
            texto = pagina.extract_text()
            
            # Imprime o texto da página
            print(f"Texto da Página {num_pagina + 1}:\n{texto}\n")

# Substitua 'caminho_do_seu_arquivo.pdf' pelo caminho do seu próprio arquivo PDF
caminho_pdf = 'Fatura Claro.pdf'
ler_pdf(caminho_pdf)
