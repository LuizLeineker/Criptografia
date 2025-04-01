def conversion(six: str) -> int:
    return int(six, 2)

asc = []    ## ARMAZENAR OS ASC DAS LETRAS
bits = []   ## ARMAZENA 8 BITS
six = []    ## ARMAZENA 6 BITS
extra = []  ## SERVE COM AUXILIAR
final = []  ## ARMAZENA A STRING FINAL
string = input("Informe uma string: ")
char = list(string)

char_map = {
    i: char for i, char in enumerate(
        [
            *map(chr, range(65, 91)),  # A-Z (0-25)
            *map(chr, range(97, 123)),  # a-z (26-51)
            *map(str, range(0, 10)),  # 0-9 (52-61)
            '+',  # 62
            '/'   # 63
        ]
    )
}



# Char para ASCII - Decimal para Bytes
for i in char:
    number = ord(i)
    asc.append(number)
    for k in range(8):
        a = number % 2
        number = number / 2
        bits.append(int(a))

bits.reverse()          #Inverter a ordem dos Bytes
extra = list(bits)      #O extra vai ser usado depois para devolver valores


i = 0
k = 0
## Pegar os 6 primeiros bits, k == 5 ele reseta K para pular 2 bits
while i < len(bits):
    six.append(bits[i])
    bits[i] = 7
    if k == 5:
        k = -1
        i += 2
    i += 1
    k += 1

i = 6
while i < len(bits):
    if bits[i] != 7:
        six.append(bits[i])
    i+= 1

# retorna o valor inicial para bits
bits = list(extra)
extra.clear()

i = 0
k = 0
while i < len(six):
    if k == 6:
        string = "".join(map(str, extra))
        final.append(conversion(string))
        extra.clear()
        k = 0
    extra.append(six[i])
    i+= 1
    k+= 1

# Print com seus respectivos valores:

print('+------------------------+')
print(f"CARACTERES: {char}")
print(f"ASCII: {asc}")
print('+-------- BYTE ----------+')
print(f"8 BITS: {bits}")
print(f"6 BITS: {six}")
print('+------------------------+')
print(f"END: {final}")
print(f"END: {final}")
print('+------------------------+')
#print(char_map)