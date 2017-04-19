import sys

def main(word):
    length = len(word)
    myDict = {}
    num_of_values = 0
    for i in range(0,length):
        char = word[i]
        if (char not in myDict):
            myDict[char] = 1
            num_of_values += 1
        else:
            count = myDict[char]
            myDict[char] = count+1
    num_of_odd_chars = 0
    vals = list(myDict.values())
    for i in range(0, num_of_values):
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