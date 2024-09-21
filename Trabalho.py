from bd import *

celular = {"ram" : 8, "armazenamento" : 256, "camera" : 60, "bateria" : 4575 }


def prev_cell(prod):
    pRam = prod["ram"]
    pArm = prod["armazenamento"]
    pCam = prod["camera"]
    pBat = prod["bateria"]

    fedback = []


    for i in range(0, ram.shape[0]):
        for j in range(0, ram.shape[1]):
            if i <  3:
                if ram[i][0] <= pRam < ram[i+1][0]:
                    fedback.append(ram[i][1])
            else:
                if ram[i][0] <= pRam:
                    fedback.append(ram[i][1])


    for i in range(0, armazenamento.shape[0]):
        for j in range(0, armazenamento.shape[1]):
            if i <  3:
                if armazenamento[i][0] <= pArm < armazenamento[i+1][0]:
                    fedback.append(armazenamento[i][1])
            else:
                if armazenamento[i][0] <= pArm:
                    fedback.append(armazenamento[i][1])


    for i in range(0, camera.shape[0]):
        for j in range(0, camera.shape[1]):
            if i <  3:
                if camera[i][0] <= pCam < camera[i+1][0]:
                    fedback.append(camera[i][1])
            else:
                if camera[i][0] <= pCam:
                    fedback.append(camera[i][1])


    for i in range(0, bateria.shape[0]):
        for j in range(0, bateria.shape[1]):
            if i <  3:
                if bateria[i][0] <= pBat < bateria[i+1][0]:
                    fedback.append(bateria[i][1])
            else:
                if bateria[i][0] <= pBat:
                    fedback.append(bateria[i][1])

    return fedback


analize = prev_cell(celular)

print(f"Celular Ram: {celular['ram']}GB\nAvalição: {analize[0]}\n")
print(f"Celular Armazenamento: {celular['armazenamento']}GB\nAvalição: {analize[1]}\n")
print(f"Celular Câmera: {celular['camera']}MP\nAvalição: {analize[2]}\n")
print(f"Celular Bateria: {celular['bateria']}mAh\nAvalição: {analize[3]}\n")

