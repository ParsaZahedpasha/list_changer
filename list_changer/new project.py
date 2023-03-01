turns_= int(input ("please enter the turns you want to do the changes:\t"))

listProgram = []

for turns in range(turns_):
    changes = input("please enter the changes you want from these options:\n(append , reverse , remove , pop , sort , insert ):\t").split()
    if changes[0] == "print":
        print(listProgram)

    elif changes[0]== "append":
        listProgram.append(int(changes[1]))

    elif changes[0] == "insert":
        listProgram.insert(int(changes[1]) ,int(changes[2]))

    elif changes[0] == "remove":
        listProgram.remove(int(changes[1]))

    elif changes[0] == "reverse":
        listProgram.reverse()

    elif changes[0] == "pop":
        listProgram.pop()
        
    elif changes[0] == "sort":
        listProgram.sort()
    else:
        print("something went wrong!!!!!")