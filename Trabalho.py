from functions import *

def main():

    celular = {"ram" : 0, "armazenamento" : 0, "camera" : 0, "bateria" : 0 }
    
    while True:
        cRam = int(input("Qual é o valor de ram que o celular terá: "))
        if cRam >= 2:
            celular['ram'] = cRam
            break
        else:
            print(f"Valor inválido! O valor mínimo é 2GB")

        celular = {"ram" : 0, "armazenamento" : 0, "camera" : 0, "bateria" : 0 }
    
    while True:
        cArm = int(input("Qual é o valor de armazenamento que o celular terá: "))
        if cArm >= 64:
            celular['armazenamento'] = cArm
            break
        else:
            print(f"Valor inválido! O valor mínimo é 64GB")


    while True:
        cCam = int(input("Qual é o valor da câmera que o celular terá: "))
        if cCam >= 24:
            celular['camera'] = cCam
            break
        else:
            print(f"Valor inválido! O valor mínimo é 24MP")

    while True:
        cBat = int(input("Qual é o valor da câmera que a bateria terá: "))
        if cBat >= 3000:
            celular['bateria'] = cBat
            break
        else:
            print(f"Valor inválido! O valor mínimo é 3000mAh")
    
    verificarQualit(celular)
    calcValor(celular)
    showConfigs(celular)

main()
