def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao GitHub."

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    mensagem = saudacao(nome)
    print(mensagem)
