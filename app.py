print("Olá mundo")
print("Versionamento de Releases em Python usando Git Tag")
print("O que é Git Tag?")
print("Marca um commit especifico, usado para releases, tipos: Lightweight e Annotated")
print("Semantic Versioning:")
print("Formato: MAJOR.MINOR.PATCH")
print("Quando mudar cada numero:")
print("MAJOR: Mudanças incompativeis")
print("MINOR: Novas funções compatíveis")
print("PATCH: Correções de bugs")

def saudacao(nome, idioma="pt"):
    if idioma == "pt":
        print(f"Olá, {nome}!")
    elif idioma == "en":
        print(f"Hello, {nome}!")

saudacao("Ana", "en")
