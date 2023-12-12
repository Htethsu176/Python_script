def create_file():
    with open("data.txt","w") as file:
        file.write("Hello world! \n")
        file.write("My name is John. \n")

def read_file():
    with open("data.txt","r") as file:
        print(file.read())

def update_file():
    with open("data.txt","w") as file:
        file.write("I'm twenty years old. \n")
        file.write("This is another line. \n")
        file.write("Thank you! \n")
    with open("data.txt","r") as file:
        print(file.read())

def delete_file(target_line):
    with open("data.txt","r") as file:
        lines = file.readlines()
    with open("data.txt","w") as file:
        for line in lines:
            if target_line not in line:
                file.write(line)
                
if __name__ == "__main__":
    create_file()
    read_file()
    update_file()
    delete_file("twenty")
    read_file()