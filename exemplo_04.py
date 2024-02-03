# Ferramentas de controle de fluxo
# Assim como a instrução while que acabou de ser apresentada, 
# o Python usa mais algumas que encontraremos neste capítulo.

# Comandos if

# x = int(input("Digite um número inteiro: "))

# if x < 0:
#     print('Número menor do que zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Um')
# else:
#     print('Mais do que um')

# Comandos for
    
# words = ["cat", "windows", "defenestrate"]

# for word in words:
#     print(word, len(word))

# users
    
# users = { 
#     "Hans": "active",
#     "Luciano": "inactive",
#     "Rafael": "active",
# }

# for user, status in users.copy().items():
#     if status == "inactive":
#         del users[user]

# active_users = {}
# for user, status in users.items():
#     if status == "active":
#         active_users[user] = status

# print(active_users)

# A função Range

# for n in range (2,10):
#     for x in range (2, n):
#         if n % x == 0:
#             print(n, 'igual', x, '*', n//x)
#             break
#     else:
#         print(n, 'é um número primo')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Número par", num)
#         continue
#     print("número ímpar", num)


# while True:
#     try: 
#         x = input("Digite um número inteiro: ")

#         x = int(x)

#         if x < 0:
#             print('Número menor do que zero')
#         elif x == 0:
#             print('Zero')
#         elif x == 1:
#             print('Um')
#         else:
#             print('Mais do que um')
    
#     except ValueError as e:
#         print("Isso não é um número inteiro", x,e)

# Comando Pass

# Instruções match

# def categoria_de_produto(id):
#     match id:
#         case 1:
#             print("eletronico")
#         case 2:
#             print("móveis")
#         case 3:
#             print("construção")
#         case _:
#             print("Algo diferente")
            

# var = categoria_de_produto(1)
# print(var)


x = input("Digite x: ")
y = input("Digite y: ")
point = (0 , 0)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
