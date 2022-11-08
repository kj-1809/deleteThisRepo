def isEmpty(stack):
    if(len(stack) == 0):
        return True
    return False

def push(stack , item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return 'State is already empty'
    return stack.pop()

def peek(stack):
        if isEmpty(stack):
            return 'Stack is already empty'
        return(stack[-1])
def display(stack):
    if isEmpty(stack):
        print('Stack is Empty')
    else:
        print("top : " , stack[len(stack) -1])
        for i in range(len(stack) -2 , -1 , -1):
            print(stack[i])

def main():
    stack = []
    while(True):
        print('Stack Operations : ')
        print('1)Push')
        print('2)Pop')
        print('3)Peek')
        print('4)Display')
        print('5)Exit')

        choice = int(input('Enter a your choice number : '))

        if (choice == 1):
            item = input('Enter a item : ')
            push(stack , item)
        elif (choice == 2):
            print(pop(stack))
        elif(choice == 3):
            print(peek(stack))
        elif(choice == 4):
            display(stack)
        else:
            break
main()