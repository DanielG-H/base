
def hex_to_decimal(num):
    hex_values = {
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15"
    }
    hexadecimal = list(num)
    hexadecimal.reverse()
    for i in range(len(hexadecimal)):
        for x in hex_values:
            if hexadecimal[i] == x:
                hexadecimal[i] = hex_values[x]

    num = 0
    for j in range(len(hexadecimal)):
        hexadecimal[j] = int(hexadecimal[j])
        num = num + (hexadecimal[j] * (16**j))
    print(f"Decimal: {num}")

    return num


def bit_octal_to_decimal(num, base):
    nums = list(num)
    nums.reverse()
    num = 0
    for i in range(len(nums)):
        nums[i] = int(nums[i])
        num = num + nums[i] * (base ** i)
    print(f"Decimal: {num}")

    return num


def decimal_to_octal_hex_bit(num, base):
    hex_values = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F"
    }
    nums = [0] * 100
    i = 0
    num = int(num)

    while num != 0:
        nums[i] = num % base
        num = num // base
        i += 1
    nums.reverse()
    j = 0
    while nums[j] == 0:
        j += 1

    nums_len = (len(nums) - j) * -1
    num_split = [""] * (nums_len * -1)
    while nums_len < 0:
        num_split[nums_len] = str(nums[nums_len])
        for x in hex_values:
            if num_split[nums_len] == x:
                num_split[nums_len] = hex_values[x]
        nums_len += 1

    num = ""
    for k in range(len(num_split)):
        num += num_split[k]

    unit = ""
    if base == 8:
        unit = "Octal"
    elif base == 16:
        unit = "Hexadecimal"
    elif base == 2:
        unit = "Binary"
    print(f"{unit}: {num}")

    return num


def check_binary(num):
    is_binary = False
    num_split = list(num)
    for i in range(len(num_split)):
        if num_split[i] in ["1", "0"]:
            is_binary = True
        else:
            is_binary = False
            break

    return is_binary


def check_decimal(num):
    is_decimal = False
    num_split = list(num)
    for i in range(len(num_split)):
        if num_split[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            is_decimal = True
        else:
            is_decimal = False
            break

    return is_decimal


def check_hex(num):
    is_hex = False
    num_split = list(num)
    for i in range(len(num_split)):
        if num_split[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
            is_hex = True
        else:
            is_hex = False
            break

    return is_hex


def check_octal(num):
    is_octal = False
    num_split = list(num)
    for i in range(len(num_split)):
        if num_split[i] in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            is_octal = True
        else:
            is_octal = False
            break

    return is_octal


def validate_correct_base(num, option):
    if option == "1":
        is_binary = check_binary(num)
        while is_binary is False:
            print("---Invalid Binary---"
                  "Please enter a number composed only by ones and zeros: ")
            num = input()
            is_binary = check_binary(num)
    elif option == "2":
        is_decimal = check_decimal(num)
        while is_decimal is False:
            print("---Invalid Decimal---"
                  "Please enter a number composed by integer positive numbers: ")
            num = input()
            is_decimal = check_decimal(num)
    elif option == "3":
        is_hex = check_hex(num)
        while is_hex is False:
            print("---Invalid Hexadecimal---"
                  "Please enter a number composed by numbers in range 0-9 and/or letters in range A-F: ")
            num = input()
            is_hex = check_hex(num)
    elif option == "4":
        is_octal = check_octal(num)
        while is_octal is False:
            print("---Invalid Octal---"
                  "Please enter a number composed by numbers in range 0-7: ")
            num = input()
            is_octal = check_octal(num)

    return num


def check_if_no_all_zeros(num):
    split_num = list(num)
    j = 0
    for i in range(len(split_num)):
        if split_num[i] == "0":
            j += 1

    if j == len(split_num):
        no_zero = False
        print("\nBinary: 0000"
              "\nDecimal: 0"
              "\nHexadecimal: 0"
              "\nOctal: 0")
    else:
        no_zero = True

    return no_zero


def type_of_conversion(option):
    print("Type in the number to convert: ")
    num = input().upper()
    num = validate_correct_base(num, option)
    no_all_zero = check_if_no_all_zeros(num)
    if no_all_zero is True:
        if option == "1":
            num = bit_octal_to_decimal(num, 2)
            decimal_to_octal_hex_bit(num, 8)
            decimal_to_octal_hex_bit(num, 16)
        elif option == "2":
            decimal_to_octal_hex_bit(num, 2)
            decimal_to_octal_hex_bit(num, 8)
            decimal_to_octal_hex_bit(num, 16)
        elif option == "3":
            num = hex_to_decimal(num)
            decimal_to_octal_hex_bit(num, 2)
            decimal_to_octal_hex_bit(num, 8)
        elif option == "4":
            num = bit_octal_to_decimal(num, 8)
            decimal_to_octal_hex_bit(num, 2)
            decimal_to_octal_hex_bit(num, 16)


def check_option_in_range(op):
    in_range = False
    if op in ["0", "1", "2", "3", "4"]:
        in_range = True

    return in_range


def validate_correct_option(op):
    is_option = check_option_in_range(op)
    while is_option is False:
        print("---Invalid Option---"
              "Please enter an option in range 1-4: ")
        op = input()
        is_option = check_option_in_range(op)

    return op


if __name__ == '__main__':
    opt = "-1"
    while opt != "0":
        print("\nWelcome to the BASE CONVERTER"
              "\n1) Binary"
              "\n2) Decimal"
              "\n3) Hexadecimal"
              "\n4) Octal\n")
        print("Type in the number of the starting base (0 to exit): ")
        opt = input()
        opt = validate_correct_option(opt)
        if opt != "0":
            type_of_conversion(opt)
        input()
