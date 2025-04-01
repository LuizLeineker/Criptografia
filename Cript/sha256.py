string = input("Informe uma string: ")
char = list(string)


## while até 256, até quando tiver o digitos inseridor ele armazena em uma lista esses digitios
# dps que a palavra acabar armazena 1 e depois 00 até o final
# cada letra é referente a 8 bits, quando acabar a palavra preenche com 10000000
# os bits final eu num lembro
# segundo o site é isso ai Append the original message length (100000, 32 in decimal) at the end of the message block as a 64-bit big-endian integer
# Bits `0` são adicionados até que o comprimento seja 448 bits módulo 512.
# Os últimos 64 bits armazenam o tamanho original da mensagem em bits

