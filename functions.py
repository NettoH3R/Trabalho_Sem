from bd import *
from colorama import Back, Fore, Style

# Função que vai verifivar a qualidade dos componentes do celular
def config(prod):
    pRam = prod["ram"]
    pArm = prod["armazenamento"]
    pCam = prod["camera"]
    pBat = prod["bateria"]

    fedback = []

    # Verifica a ram do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, ram.shape[0]):
        for j in range(0, ram.shape[1]):
            if i <=  3:
                if ram[i][0] <= pRam < ram[i+1][0]:
                    fedback.append(ram[i][1])
                    break
            else:
                if ram[i][0] <= pRam:
                    fedback.append(ram[i][1])
                    break

# Verifica o armazenamento do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, armazenamento.shape[0]):
        for j in range(0, armazenamento.shape[1]):
            if i <=  3:
                if armazenamento[i][0] <= pArm < armazenamento[i+1][0]:
                    fedback.append(armazenamento[i][1])
                    break
            else:
                if armazenamento[i][0] <= pArm:
                    fedback.append(armazenamento[i][1])
                    break

# Verifica a camera do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, camera.shape[0]):
        for j in range(0, camera.shape[1]):
            if i <=  3:
                if camera[i][0] <= pCam < camera[i+1][0]:
                    fedback.append(camera[i][1])
                    break
            else:
                if camera[i][0] <= pCam:
                    fedback.append(camera[i][1])
                    break

# Verifica a bateria do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, bateria.shape[0]):
        for j in range(0, bateria.shape[1]):
            if i <=  3:
                if bateria[i][0] <= pBat < bateria[i+1][0]:
                    fedback.append(bateria[i][1])
                    break
            else:
                if bateria[i][0] <= pBat:
                    fedback.append(bateria[i][1])
                    break

    return fedback


# Vai mostrar o celular e a avaliação de seu hardware
def showConfigs(cell):
    analise = config(cell)

    print(f"Celular Ram: {cell['ram']}GB\nAvalição: {analise[0]}\n")
    print(f"Celular Armazenamento: {cell['armazenamento']}GB\nAvalição: {analise[1]}\n")
    print(f"Celular Câmera: {cell['camera']}MP\nAvalição: {analise[2]}\n")
    print(f"Celular Bateria: {cell['bateria']}mAh\nAvalição: {analise[3]}\n")

def verificarQualit(cell):

    fb = config(cell)

    result = (sum(fb)*2)/len(fb)

    if result >= 8:
        print("\n\n\n"+"~"*40)
        print(f"Taxa de aprovação do aparelho: {round(result*10,0)}%")
        print("~"*40)
        print("\n\n\n")
        print(f"O Celular é excelente:\n")

    elif 8 > result > 5:
        print("\n\n\n" + f"{Fore.YELLOW}~"*40)
        print(f"Taxa de aprovação do aparelho: {round(result*10,0)}%")
        print(f"~"*40)
        print(f"{Fore.WHITE}\n\n")
        print(f"O Celular é bom, mas pode ser melhorado:\n")
    else:
        print("\n\n\n"+"~"*40)
        print(f"Taxa de aprovação do aparelho: {round(result*10,0)}%")
        print("~"*40)
        print("\n\n\n")
        print(f"O Celular é obsoleto, tem que ser melhorado:\n")

    for i in range(0,len(fb)):
        if fb[i] < 3:
            if i == 0:
                print("--"*27)
                print(f"A memoria Ram pode ser melhorada: {cell["ram"]}GB é pouco")
                print("--"*27)
            if i == 1:
                print("--"*27)
                print(f"O armazenamento pode ser melhorado: {cell["armazenamento"]}GB é pouco")
                print("--"*27)
            if i == 2:
                print("--"*35)
                print(f"A camera pode ser melhorada: Uma câmera de {cell["camera"]}MP tem pouca qualidade")
                print("--"*35)
            if i == 3: 
                print("--"*40)
                print(f"O armazenamento pode ser melhorado: Uma bateria de {cell["bateria"]}mAh durará pouco tempo")
                print("--"*40)
        print("\n\n\n")