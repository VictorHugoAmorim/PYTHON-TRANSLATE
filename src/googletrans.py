from translate import Translator

s = Translator(from_lang="english", to_lang="Portuguese")
texto = input("Digite o texto a ser traduzido:\n")
res= s.translate(texto)

print(f'Inglês: "{texto.upper()}"\nPortuguês: "{res}"')
