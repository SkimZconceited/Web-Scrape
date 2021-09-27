#file is on collecting the results of scraping to a word document.
#module for collecting plate numbers to send tehm to the main.py

def plate_collection():
    with open("Plate.txt", "r") as plates:
        numbers = plates.readlines()
        for number in numbers:
            print(number)