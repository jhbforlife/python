def print_me():
    message = input("What would you like to print? -> ")
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    print(LINE_UP, end=LINE_CLEAR)
    print(message)


print_me()
