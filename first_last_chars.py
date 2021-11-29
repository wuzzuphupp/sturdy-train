string = input("Write a sentence: ")
if len(string) < 4:
    print("Please input a longer sentence")
else:
    print("The first two characters of your sentence are: ")
    print(string[0:2])
    print("The last two characters of your sentence are: ")
    print(string[-2:])
