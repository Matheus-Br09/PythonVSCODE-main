def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif 16 <= idade < 18 or idade >= 65:
        return f"Com {idade} anos: OPCIONAL"
    else:
        return f"Com {idade} anos: OBRIGATÓRIO"    


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))