notas = {}
continuar = True

while continuar:
    nota = float(input("Digite a nota: "))
    notas[len(notas) + 1] = nota

    resposta = input("Deseja adicionar mais notas? (S/N): ")
    if resposta in "Nn":
        break

media = sum(notas.values()) / len(notas)
print("A média das notas é:", media)