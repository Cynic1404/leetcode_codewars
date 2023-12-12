def largestGoodInteger(num):
    res = ""
    counter = 0
    while counter + 2 < len(num):
        if num[counter] == num[counter + 1] == num[counter + 2]:
            if not res:
                res = int(num[counter])
            else:
                if int(num[counter]) > res:
                    res = int(num[counter])
            counter += 3
        else:
            counter += 1
    return str(res) * 3

print(largestGoodInteger("4818042931906802860005960222213336669500011846936171709111"))