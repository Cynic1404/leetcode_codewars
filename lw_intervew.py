# put lines for tests to the test array
test = ["aa", "bb", "cc", "aa", "cc", "aa", "cc", "dd", "bb"]

#creates a file  and add lines to it
file = open('myfile.txt', 'w')
for test_line in test:
    file.writelines(f"{test_line}\n")
file.close()
######################################



def text_print(k, file_name='myfile.txt'):
    # the storage for n lines
    temp_storage = []

    # here we read the file line by line, even if it's is huge we don't need to store it in memory
    with open(file_name, 'r') as file:
        line = file.readline()

        while line:
            # remove extra spaces for the string
            line = line.strip()
            # if the line contained only spaces we move to the next line
            if not line:
                line = file.readline()
                continue

            # when the temp_storage has more than k elements we remove the first one
            if len(temp_storage) > k:
                temp_storage.pop(0)

            # here we check if the last string we read matches with any elements in the storage and print it if it doesn't
            found_match = False
            for string in temp_storage:
                if string == line:
                    found_match = True
                    break
            if not found_match:
                print(line)

            # add the latest string to the storage
            temp_storage.append(line)

            # read the next line
            line = file.readline()

text_print(k=3)



