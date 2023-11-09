A = ['Pedra', 'Papel', 'Tesoura']
B = [1, 2, 3]
print("1 para pedra, 2 para papel e 3 para tesoura")
u1 = int(input("Jogador 1 :"))
while u1 not in B:
    print("Inválido")
    u1 = int(input("Jogador 1 :"))
u2 = int(input("Jogador 2 :"))
while u2 not in B:
    print("Inválido")
    u2 = int(input("Jogador 2 :"))
if u1 == u2:
    print("Empate")
if u1 == B[0] and u2 == B[1]:
    print("Jogador 2 ganhou")
if u1 == B[0] and u2 == B[2]:
    print("Jogador 1 ganhou")
if u1 == B[1] and u2 == B[2]:
    print("Jogador 2 ganhou")
if u1 == B[1] and u2 == B[0]:
    print("Jogador 1 ganhou")
if u1 == B[2] and u2 == B[0]:
    print("Jogador 2 ganhou")
if u1 == B[2] and u2 == B[1]:
    print("Jogador 1 ganhou")

