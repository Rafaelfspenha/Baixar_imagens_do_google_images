import time
import pyautogui
import os

# evitar palavras com cedilha 'ç'
# não abrir nomes que tanha muitas propaganda como celulares.
# salvar 1 foto no local que as demais fotos serão salvos.
# abrir a página do google imagens (anônimo).
# os nomes terão no máximo 20 letras.

n1= input("Digite o 1º nome:")
n2= input("Digite o 2º nome:")
n3= input("Digite o 3º nome:")
n4= input("Digite o 4º nome:")
n5= input("Digite o 5º nome:")
n6= input("Digite o 6º nome:")
n7= input("Digite o 7º nome:")
n8= input("Digite o 8º nome:")
n9= input("Digite o 9º nome:")
n10= input("Digite o 10º nome:")

def robo():
    j = 1
    k = 1


    pyautogui.sleep(6)
    pyautogui.moveTo(100, 300)
    pyautogui.click(button="left")

    while k <= 2:
        k += 1
        pyautogui.sleep(6)
        pyautogui.moveTo(750,300)
        pyautogui.click(button='right')
        pyautogui.sleep(6)

        i=1
        while i <= 5:
            pyautogui.press("up")
            i+=1
        pyautogui.sleep(6)
        pyautogui.press('enter')
        os.system('cls' if os.name=='nt' else 'clear')
        pyautogui.sleep(6)
        pyautogui.moveTo(100, 300)
        pyautogui.sleep(6)
        pyautogui.click(button="left")
        pyautogui.sleep(6)
        pyautogui.press('left')

        if j%2 == 0:
            pyautogui.write('a')
        else:
            pyautogui.write('b')

        j+=1

        pyautogui.press('enter')
        pyautogui.sleep(3)
        pyautogui.press('right')

    pyautogui.sleep(6)
    pyautogui.moveTo(250,100)
    pyautogui.sleep(6)
    pyautogui.click(button='left')
    pyautogui.sleep(6)

    i=1
    while i<=20:
        pyautogui.press('backspace')
        i+=1


pyautogui.sleep(6)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.sleep(12)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
pyautogui.sleep(12)
pyautogui.hotkey('ctrl','shift','n')
pyautogui.sleep(6)
pyautogui.write(n1)
pyautogui.sleep(6)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
pyautogui.sleep(6)
pyautogui.moveTo(150, 180)
pyautogui.sleep(6)
pyautogui.click(button="left")
pyautogui.sleep(6)
robo()

pyautogui.sleep(8)
pyautogui.write(n2)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()

pyautogui.sleep(8)
pyautogui.write(n3)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()

pyautogui.sleep(8)
pyautogui.write(n4)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()

pyautogui.sleep(8)
pyautogui.write(n5)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()

pyautogui.sleep(8)
pyautogui.write(n6)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()

pyautogui.sleep(8)
pyautogui.write(n7)
pyautogui.press('enter')
robo()

pyautogui.sleep(8)
pyautogui.write(n8)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()

pyautogui.sleep(8)
pyautogui.write(n9)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()

pyautogui.sleep(8)
pyautogui.write(n10)
pyautogui.press('enter')
os.system('cls' if os.name=='nt' else 'clear')
robo()
