#Renaming all files in a directory

import subprocess

def main():
    res = subprocess.run(
            ["ls", "-m"],
            capture_output=True, 
            text=True)

    palavra = ""
    dirs = []

    for caractere in res.stdout:
        palavra += caractere

        if caractere == " " or caractere == "\n":
            palavraLimpa = palavra.replace(",", "").replace("\n", "").replace(" ", "")

            dirs.append(palavraLimpa)
            palavra = ""

    print(f"Qtde diretorios: {len(dirs)}")    
    for d in dirs:
        data = ""
        nome = ""

        for i in range(len(d)):
            if i <= 6:
                data += d[i]
            else:
                nome += d[i]

        #print(f"Data: {data} Nome: {nome}")
        dataLimpa = data.replace("-", "")
        nome += "-"

        novo = nome + dataLimpa
        res = subprocess.run(["git", "mv" , d, novo])

if __name__ == "__main__":
    main()
    print()
