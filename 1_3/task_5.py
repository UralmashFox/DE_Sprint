def process(string):
    num1, num2 = string.split(" ")
    num1 = int(num1, 2)
    num2 = int(num2, 2)
    res = bin(num1 * num2).replace("0b", "")
    return res


if __name__ == "__main__":
    bin_string = input("Type 2 binary numbers with space between them")
    print(process(bin_string))
