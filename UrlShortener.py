import requests
from PyQt5.QtWidgets import QApplication
import sys
import time

def urlShortener(url):  # Main function to connect with url shorting site and get the shorted URL
    done = False
    while done == False:
        site = requests.get("https://vurl.com/api.php?url=" + url)
        if not site.text == "Invalid URL":
            return site
        else:
            print("Wrong type of URL, try again.")
            exit()

def LinkCopy(text): # Function to save a link to clipboard
    app = QApplication(sys.argv)
    cb = QApplication.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText(text, mode=cb.Clipboard)

def choice(text): # Function to query whether to copy the link due to code optimization
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
            print("\nSomething went wrong, please try again.")
            time.sleep(0.5)

def main():
    url = input("Type URL to be shortened: ")
    site = urlShortener(url).text
    print("\n" + site)
    time.sleep(0.5)
    if choice("\nCopy the URL to clipboard? Y/N"):
        LinkCopy(site)
        print("URL was copied successfully\n")
    print("In 3 seconds the program will turn off by itself")
    time.sleep(3)
    exit()
    

if __name__ == "__main__":
    main()
