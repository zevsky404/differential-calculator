import re as regex

counter_0001_0001, counter_0010_0001, counter_0100_0001, counter_1000_0001 = 0, 0, 0, 0
counter_0001_0010, counter_0010_0010, counter_0100_0010, counter_1000_0010 = 0, 0, 0, 0
counter_0001_0100, counter_0010_0100, counter_0100_0100, counter_1000_0100 = 0, 0, 0, 0
counter_0001_1000, counter_0010_1000, counter_0100_1000, counter_1000_1000 = 0, 0, 0, 0

s_box_dict = {
    "0000": "1110",
    "0001": "0111",
    "0010": "0001",
    "0011": "1010",
    "0100": "0011",
    "0101": "0010",
    "0110": "1011",
    "0111": "1101",
    "1000": "0110",
    "1001": "0000",
    "1010": "1111",
    "1011": "1000",
    "1100": "0101",
    "1101": "1100",
    "1110": "1001",
    "1111": "0100"
}


def s_box(org_number):
    block1 = org_number[0:4]
    block2 = org_number[4:8]
    block3 = org_number[8:12]
    block4 = org_number[12:16]

    output = s_box_dict[block1] + s_box_dict[block2] + s_box_dict[block3] + s_box_dict[block4]

    # print("original number: " + org_number + "new number: " + output)
    return output


def transposition(bn):
    output = ""
    output = bn[0] + bn[4] + bn[8] + bn[12] + bn[1] + bn[5] + bn[9] + bn[13] + bn[2] + bn[6] + bn[10] + bn[14] + bn[3] + bn[7] + bn[11] + bn[15]

    return output


def find_pattern(pattern, number):
    reg1 = "0001"
    reg2 = "0010"
    reg3 = "0100"
    reg4 = "1000"

    global counter_0001_0001, counter_0010_0001, counter_0100_0001, counter_1000_0001
    global counter_0001_0010, counter_0010_0010, counter_0100_0010, counter_1000_0010
    global counter_0001_0100, counter_0010_0100, counter_0100_0100, counter_1000_0100
    global counter_0001_1000, counter_0010_1000, counter_0100_1000, counter_1000_1000

    match1 = regex.search(reg1, number)
    match2 = regex.search(reg2, number)
    match3 = regex.search(reg3, number)
    match4 = regex.search(reg4, number)

    if match1 is not None:
        if pattern == "0001":
            counter_0001_0001 += 1
        if pattern == "0010":
            counter_0010_0001 += 1
        if pattern == "0100":
            counter_0100_0001 += 1
        if pattern == "1000":
            counter_1000_0001 += 1

    if match2 is not None:
        if pattern == "0001":
            counter_0001_0010 += 1
        if pattern == "0010":
            counter_0010_0010 += 1
        if pattern == "0100":
            counter_0100_0010 += 1
        if pattern == "1000":
            counter_1000_0010 += 1

    if match3 is not None:
        if pattern == "0001":
            counter_0001_0100 += 1
        if pattern == "0010":
            counter_0010_0100 += 1
        if pattern == "0100":
            counter_0100_0100 += 1
        if pattern == "1000":
            counter_1000_0100 += 1

    if match4 is not None:
        if pattern == "0001":
            counter_0001_1000 += 1
        if pattern == "0010":
            counter_0010_1000 += 1
        if pattern == "0100":
            counter_0100_1000 += 1
        if pattern == "1000":
            counter_1000_1000 += 1


def cipher(block, pattern, number):
    s_box_output = s_box(number)
    transposition_output = transposition(s_box_output)
    find_pattern(pattern, transposition_output[block * 4:block * 4 + 4])


def main():
    for i in range(4096):
        bin_str_i = str(bin(i))
        gen_number = ""
        for j in range(12 - len(bin_str_i) + 2):
            gen_number += "0"
        gen_number += bin_str_i[2:]
        for block in range(4):
            for pattern in ["1000", "0100", "0010", "0001"]:
                input_number = gen_number[0:block * 4] + pattern + gen_number[block * 4:]
                cipher(block, pattern, input_number)
                # print(input_number)

    print("If given 0001, then we get: \n"
          + "0001: " + str(counter_0001_0001) + " times,\n"
          + "0010: " + str(counter_0001_0010) + " times,\n"
          + "0100: " + str(counter_0001_0100) + " times,\n"
          + "1000: " + str(counter_0001_1000) + " times.\n")

    print("If given 0010, then we get: \n"
          + "0001: " + str(counter_0010_0001) + " times,\n"
          + "0010: " + str(counter_0010_0010) + " times,\n"
          + "0100: " + str(counter_0010_0100) + " times,\n"
          + "1000: " + str(counter_0010_1000) + " times.\n")

    print("If given 0100, then we get: \n"
          + "0001: " + str(counter_0100_0001) + " times,\n"
          + "0010: " + str(counter_0100_0010) + " times,\n"
          + "0100: " + str(counter_0100_0100) + " times,\n"
          + "1000: " + str(counter_0100_1000) + " times.\n")

    print("If given 1000, then we get: \n"
          + "0001: " + str(counter_1000_0001) + " times,\n"
          + "0010: " + str(counter_1000_0010) + " times,\n"
          + "0100: " + str(counter_1000_0100) + " times,\n"
          + "1000: " + str(counter_1000_1000) + " times.\n")


if __name__ == "__main__":
    main()