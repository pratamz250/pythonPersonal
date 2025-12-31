import json

with open("dados.json", "r", encoding="utf-8") as f:
    dadosLidos = json.load(f)

print(dadosLidos)
print(dadosLidos["profissao"])
print(type(dadosLidos))

dadosLidos["idade"] = 20

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dadosLidos, f, indent=4, ensure_ascii=False)

with open("dados2.json", "r", encoding="utf-8") as f2:
    dados2 = json.load(f2)

print(dados2)
