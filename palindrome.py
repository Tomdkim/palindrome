import sys

def main(char_array):
    length = len(char_array)
    myDict = {}
    num_of_chars = 0
    for i in range(0,length):
        char = char_array[i]
        if (char not in myDict):
            myDict[char] = 1
            num_of_chars += 1
        else:
            count = myDict[char]
            myDict[char] = count+1
    num_of_odd_chars = 0
    vals = list(myDict.values())
    for i in range(0, num_of_chars):
        if (vals[i] % 2 == 1):
            num_of_odd_chars += 1
    if (length % 2 == 0 and num_of_odd_chars != 0):
        print("A palindrome cannot be formed.")
    elif (length % 2 == 1 and num_of_odd_chars != 1):
        print("A palindrome cannot be formed.")
    else:
        print("A palindrome can be formed.")

if __name__ == "__main__":
    argv = len(sys.argv)
    if (argv <= 1):
        print("Wrong number of arguments.")
        exit(1)
    char_array = []
    for i in range(1,argv):
        char_array.append(sys.argv[i])
    main(char_array)