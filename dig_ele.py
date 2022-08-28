def conv_bin_to_dec(bin_num):                                               #Essa função converte o valor informado em binário para decimal
    print(bin_num)

    if(str.isdecimal(bin_num)):                                             #Vefirica se algum caracter informado pelo usuário não é decimal
        split_bin_num = list(bin_num)                                       #Converte o número informado pelo usuário em uma matriz de uma linha com "bin_num_len" colunas
        inv_split_bin_num = inverter(split_bin_num)                         #Inverte a ordem dos números dispostos na matriz
        bin_num_len = len(split_bin_num)                                    #Verifica a quantidade de colunas existentes na matriz

        dec = 0                                                             #Inicializa o dec (número convertido para decimal)

        for i in range (bin_num_len):                                       #Loop que realiza a conversão de binário para decimal
            dec_num = int(inv_split_bin_num[i]) * pow(2, i)
            dec = dec + dec_num
    else:
        print("... Erro de processamento ...")
    return dec                                                              #Retorna o dec final

def inverter(txt):                                                          #Função que realiza a inversão da matriz
    return txt[::-1]

def main():

    bin_num = input("Informe um número em binário: ")
    dec = conv_bin_to_dec(bin_num)

    print("Dec: ", dec)

main()