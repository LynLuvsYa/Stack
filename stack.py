def push():
    global pointer
    item = input("input data item to input \n")
    pointer += 1
    if pointer >= len(stack): print("Error: Stack Full") # if it's larger than the length of the stack, that means it's full
    else: stack[pointer] = item
    return

def pop():
    global pointer
    if pointer < 0: print("Error: Stack Empty") #basically, if it's less than zero, then no items have been added to the stack yet.
    else:
        print(stack[pointer])
        pointer -= 1
    return

def arrowpos(): # just a general way to see where the pointer is (wip)
    for x in range(len(arrow)): arrow[x] = ""
    arrow[pointer + 1] = "<"
    return

def prettyprint():
    print("[")
    print(arrow[0])
    for x in range(len(stack)): print(stack[x], arrow[x + 1])
    print("]")
    
def retreive():
    global pointer
    with open("stacktxt.txt", "r") as file:
        data = file.readline().rstrip()
        while data != "":
            stack.append(data)
            arrow.append("")
            data = file.readline().rstrip()
    pointer = int(stack[-1])
    stack.pop(-1)
    
def runaway():
    choice = input("add to text file for later use? y/n")
    if choice == "y" or choice == "Y": SENDIT()
    if choice == "n" or choice == "N": exit()

def SENDIT():
    with open("stacktxt.txt", "w") as file:
        for x in range(len(stack)): file.write(stack[x] + "\n")
        file.write(str(pointer))
        
stack = []
arrow = ["<"]
pointer = 0
if int(input("retrieve previous data from text file? 1 = yes, any other = no \n")) == 1:
    retreive()
else:
    for x in range(int(input("how many bits of data? \n"))): # user can define how much data can be added to the stack
        stack.append("Empty")
        arrow.append("")
    pointer = -1 
choice = "wiufe"# random stuff to make sure the bit underneath has a value to compare with at the start
arrowpos()
prettyprint()
while choice != "out" and choice  != "Out":
    choice = input("push, pop or out? \n")
    if choice == "push" or choice == "Push": push()
    if choice == "pop" or choice == "Pop": pop()
    if choice == "out" or choice == "Out": runaway()
    arrowpos()
    prettyprint()
