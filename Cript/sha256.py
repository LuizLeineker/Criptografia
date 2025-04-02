## while até 256, até quando tiver o digitos inseridor ele armazena em uma lista esses digitios
# dps que a palavra acaba armazena 1 e depois 00 até o final
# cada letra é referente a 8 bits, quando acabar a palavra preenche com 10000000
# os bits final eu num lembro
# segundo o site é isso ai Append the original message length (100000, 32 in decimal) at the end of the message block as a 64-bit big-endian integer
# Bits `0` são adicionados até que o comprimento seja 448 bits módulo 512.
# Os últimos 64 bits armazenam o tamanho original da mensagem em bits

bits = []       # SALVA OS BITS INICIAL DA STRING
padding = []    # SALVA OS BITS DE 0 A 448
tamanho = []
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

string = input("Informe uma string: ")
char = list(string)

for i in char:
    number = ord(i)
    for k in range(8):
        a = number % 2
        number = number / 2
        bits.append(int(a))

bits.reverse()
i = 0

## DO BITS 0 ATÉ O 448
while i in range(448):
    if i == len(bits):
        padding.append(1)
    elif i < len(bits):
        padding.append(bits[i])
    else:
        padding.append(0)
    i+= 1

i = 0

palavra = len(char) * 8

## TRASFORMA O TAMANHO DA PALAVRA EM BITS
for i in range(8):
    a = palavra % 2
    palavra = palavra / 2
    tamanho.append(int(a))
    i+= 1
tamanho.reverse()

i = 0
## JUNTA O TAMANHO DA PALAVRA MAIS OS 448
while i in range(64):
    if i < len(tamanho):
        padding.append(tamanho[i])
    else:
        padding.append(0)
    i += 1

#print(padding)
#print(len(padding))

## 16 PALAVRAS DE 32 BITS, 16 * 32 = 512
## TEMOS 64 PARES DE 8 BITS
# 3 - Parte
# OLHAR NO SITE LA PARA TER UMA BOA BASE
# NA PARTE 3 ROTACIONAR OS BITS, ORIGINAL: 00000000000000000000000000000000, ROTATE 7 PEGARIA OS 7 BITS DO FINAL COLOCARIA NO COMECO
# COM 18 É MESMA COISA PEGARIA OS 18 BITS FINAL E TRAZER PARA COMEÇO ( COM BASE ISSO NO ORIGINAL, PEGA OS 18 DO FINAL DO ORIGINAL PARA O COMECO)
## 64 palavras de 32,  sendo as 16 primeiras do bloco de 512
# w16 = w0 + σ0 + w9 + σ1
# w17 = w1 + σ0 + w10 + σ1
## Você começa com as 16 palavras iniciais (W[0] até W[15]) do bloco de 512 bits.
## As palavras seguintes (W[16] até W[63]) são expandidas usando a fórmula fornecida, que envolve as operações σ₀ e σ₁, além de algumas palavras anteriores
# 4 - Parte


## PENSAR NUMA LOGICA 