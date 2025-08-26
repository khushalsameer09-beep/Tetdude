#1
'''try:
    f = open("sample.txt", "r")
    for line in f:
        print(line.strip())
    f.close()
except FileNotFoundError:
    print("File not found")'''
#2
data=input("Enter text to write in file: ")
with open("output.txt", "w") as file:
    file.write(data+"\n")
    print("File written")
more_data=input("Enter text to write in file: ")
with open("output.txt", "a") as file:
    file.write(more_data+"\n")
    print("File written")
    print("File written")
print("\nFinal content of file is")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
