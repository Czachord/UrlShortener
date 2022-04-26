import requests
from PyQt5.QtWidgets import QApplication
import sys
import time

def urlShortener(url):
    done = False
    while done == False:
        strona = requests.get("https://vurl.com/api.php?url=" + url)
        if not strona.text == "Invalid URL":
            done = True
            return strona
        else:
            print("Zły link, spróbuj jeszcze raz")
            exit()

def LinkCopy(text):
    app = QApplication(sys.argv)
    cb = QApplication.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText(text, mode=cb.Clipboard)

def choice(text):
    done = False
    while done == False:
        print(text)
        anwser = input()
        if anwser.lower() == "y":
            done = True
            return True
        elif anwser.lower() == "n":
            done = True
            return False
        else:
            print("\nCoś poszło spróbuj jeszcze raz")
            time.sleep(0.5)

def main():
    url = input("Podaj URL do skrócenia: ")
    strona = urlShortener(url).text
    print("\n" + strona)
    time.sleep(0.5)
    if choice("\nCzy skopiować link? Y/N"):
        LinkCopy(strona)
        print("Link został skopiowany\n")
    print("Za 5 sekund program sam się wyłączy")
    time.sleep(5)
    exit()
    

if __name__ == "__main__":
    main()