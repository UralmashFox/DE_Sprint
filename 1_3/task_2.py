def process(string):
    string = prepeoces(string)
    new_string = string[::-1]
    if string == new_string:
        return True
    return False


def prepeoces(string):
    return string.replace(" ", "")


if __name__ == '__main__':
    string = input("Type a word")
    if process(string):
        print('true')
    else:
        print('false')