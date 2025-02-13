print("Hello world!")  

with open("intro.txt", "r", encoding="utf-8") as file:
    print(file.read().strip())  