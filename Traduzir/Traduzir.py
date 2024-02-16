from translate import Translator


traduzir = Translator(from_lang="pt-br",to_lang="en")

resu = traduzir.translate(input(str("Digite a fraze que queira traduzir: ")))

print(f"Sua tradução é: {resu}")
