itens = []

i = 0
for i in range(3):
    item = input()
    itens.append(item)

print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")