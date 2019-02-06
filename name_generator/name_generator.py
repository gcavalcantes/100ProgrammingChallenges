# Programa para gerar nomes
import random

# Lista de nomes masculinos
nomes_masculinos = {0: "Adão", 1: "Adélio", 2: "Agamenon", 3: "Bernardo",
                    4: "Carlos", 5: "Daniel", 6: "Danilo", 7: "Eduardo", 8: "Fábio", 9: "Felipe", 10: "Gabriel",
                    11: "Iago", 12: "Lucas", 13: "Thiago"}

# Lista de nomes femininos
nomes_femininos = {0: "Alana", 1: "Amanda", 2: "Ana", 3: "Beatriz",
                   4: "Bárbara", 5: "Carolina", 6: "Emilia", 7: "Ainara", 8: "Patricia", 9: "Daniela",
                   10: "Sophia", 11: "Julia", 12: "Jade", 13: "Thais"}

# Lista de sobrenomes
sobrenomes = {0: "Amaral", 1: "Cavalcanti", 2: "Pimentel", 3: "Bacci", 4: "Pereira",
              5: "Cuerci", 6: "Lima", 7: "Ramos", 8: "Davares", 9: "Ferreira", 10: "Almeida",
              11: "Picon", 12: "Barbosa", 13: "Duque"}

lista_nomes = {}


# Função para gerar um nome
def gen_nome():
    pergunta_nome = input("Quantos nomes você deseja gerar? ")
    pergunta_genero = input("Qual gênero você deseja ver? ('m' para masculino e 'f' para feminino) ")
    print(pergunta_nome)
    print(pergunta_genero)
    if pergunta_nome == "m":
        for contador in pergunta_nome:
            gerar_nome = random.randint.randrange(0, 13)
            gerar_sobrenome = random.randint.randrange(0, 13)

            nome_resultado = str("Nome: " + nomes_masculinos[gerar_nome] + " " +
                                 sobrenomes[gerar_sobrenome] + ". \n")
            print(nome_resultado)
            lista_nomes[contador] = nome_resultado
            contador += 1

    elif pergunta_nome == "f":
        for contador in pergunta_nome:
            gerar_nome = random.randint.randrange(0, 13)
            gerar_sobrenome = random.randint.randrange(0, 13)

            nome_resultado = str("Nome: " + nomes_femininos[gerar_nome] + " " +
                                 sobrenomes[gerar_sobrenome] + ". \n")
            print(nome_resultado)
            lista_nomes[contador] = nome_resultado
            contador += 1

    return lista_nomes


print(
    "============================================== \nPrograma para gerar nomes aletórios. v1.0 "
    "\n==============================================")
print(gen_nome())
