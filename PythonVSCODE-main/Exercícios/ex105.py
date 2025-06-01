
def notas(*num, sit=False):
    """-> Função para analisar notas e situações de vários alunos
    :param num: Números de um ou mais alunos (aceita várias)
    :param sit: Opcional, Mostra a situação da turma (Boa, Razoável ou Ruim )
    :return: dicionário com várias informações sobre a turma
    """

    maior = menor = media = 0
    dic = {}
    
    for c in range(0, len(num)):
        media += num[c]
        if c == 0:
            maior = menor = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
            if num[c] < menor:
                menor = num[c] 

    dic["qtd_notas"] = len(num)
    dic["Maior"] = maior
    dic["Menor"] = menor
    dic["Média"] = media / len(num)

    if sit == True:
        dic["Situação"] = ""
        if dic["Média"] >= 7:
            dic["Situação"] = "BOA"
        elif 6 <= dic["Média"] < 7:
            dic["Situação"] = "RAZOÁVEL"
        else:
            dic["Situação"] = "RUIM"
    return dic


res = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(res)
help(notas)