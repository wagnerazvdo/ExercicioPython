def main():
    quantidadeXerox = int(input('Digite a quantidade de folhas: '))
    if quantidadeXerox <= 100:
        valorXerox = 0.25
    else:
        valorXerox = 0.2

    print(f'O valor a ser pago é de R$: {quantidadeXerox * valorXerox}')


main()
