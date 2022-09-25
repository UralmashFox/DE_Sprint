def check(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string


if __name__ == "__main__":
    string = input("Type a bracket string")
    if check(string):
        print('balanced')
    else:
        print('unbalanced')