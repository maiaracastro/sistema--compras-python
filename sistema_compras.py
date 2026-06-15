# Variável para armazenar o valor total das compras
total = 0

# Laço para cadastrar vários produtos
while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input(f"Digite a quantidade de '{produto}': "))
    total += (preco * quantidade)
    continuar = input("Deseja adicionar mais itens? (s/n): ").lower()
    if continuar != "s":
        break

print("\n--- RESUMO DA COMPRA ---")
print(f"Total sem desconto: R$ {total:.2f}")

if total > 100:
    desconto = total * 0.10
    total_final = total - desconto
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_final:.2f}")
else:
    print("Nenhum desconto aplicado.")
    print(f"Total a pagar: R$ {total:.2f}")
