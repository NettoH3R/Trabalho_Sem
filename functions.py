from bd import *


# Vai mostrar o celular e a avaliação de seu hardware
def showConfigs(cell, analise):
    print(f"Celular Ram: {cell['ram']}GB\nAvalição: {analise[0]}\n")
    print(f"Celular Armazenamento: {cell['armazenamento']}GB\nAvalição: {analise[1]}\n")
    print(f"Celular Câmera: {cell['camera']}MP\nAvalição: {analise[2]}\n")
    print(f"Celular Bateria: {cell['bateria']}mAh\nAvalição: {analise[3]}\n")




# Função que vai verifivar a qualidade dos componentes do celular
def prev_cell(prod):
    pRam = prod["ram"]
    pArm = prod["armazenamento"]
    pCam = prod["camera"]
    pBat = prod["bateria"]

    fedback = []

    # Verifica a ram do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, ram.shape[0]):
        for j in range(0, ram.shape[1]):
            if i <  3:
                if ram[i][0] <= pRam < ram[i+1][0]:
                    fedback.append(ram[i][1])
            else:
                if ram[i][0] <= pRam:
                    fedback.append(ram[i][1])

# Verifica o armazenamento do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, armazenamento.shape[0]):
        for j in range(0, armazenamento.shape[1]):
            if i <  3:
                if armazenamento[i][0] <= pArm < armazenamento[i+1][0]:
                    fedback.append(armazenamento[i][1])
            else:
                if armazenamento[i][0] <= pArm:
                    fedback.append(armazenamento[i][1])

# Verifica a camera do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, camera.shape[0]):
        for j in range(0, camera.shape[1]):
            if i <  3:
                if camera[i][0] <= pCam < camera[i+1][0]:
                    fedback.append(camera[i][1])
            else:
                if camera[i][0] <= pCam:
                    fedback.append(camera[i][1])

# Verifica a bateria do celular qualificando de 1 a 5 com Base na base de dados
    for i in range(0, bateria.shape[0]):
        for j in range(0, bateria.shape[1]):
            if i <  3:
                if bateria[i][0] <= pBat < bateria[i+1][0]:
                    fedback.append(bateria[i][1])
            else:
                if bateria[i][0] <= pBat:
                    fedback.append(bateria[i][1])

    return fedback



