dic_vogais = {"a": 0,
              "e": 0,
              "i": 0,
              "o": 0,
              "u": 0}

def conta_vogais(msg):
    for c in msg:
        if c in "aeiou":
            dic_vogais[c] += 1
    



conta_vogais("eu quero saber, tu joga lol?")
for c in dic_vogais:
        print(c, dic_vogais[c])