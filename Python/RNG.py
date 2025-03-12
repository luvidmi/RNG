# def readFiles():
#     massNames = []
#     file = open('names.txt','r', encoding = "utf-8")
#     content = file.read()
#     massNames.append(content)

#     file.close()
#     return massNames

# def main():
#     massNames = readFiles()
#     print(massNames)
#     return

# if __name__ == "__main__":
#     main()

def readFiles():
    a = [str(i).split() for i in open('names.txt','r',encoding='utf-8')]
    return a

def main():
    massNames = readFiles()
    print(massNames)
    return

if __name__ == "__main__":
    main()