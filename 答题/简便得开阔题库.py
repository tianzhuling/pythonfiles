import json

with open("辅助.txt", "rt", encoding="utf-8") as f:
    tres = f.read()
for res in tres.split("\n"):

    ti=res.split('\\')[0]
    answer=res.split('\\')[1]
    print(answer)
    dict=json.load(open("题库.json","rt",encoding="utf-8"))
    dict[ti]=int(answer)

    json.dump(dict,open("题库.json","wt",encoding="utf-8"))
