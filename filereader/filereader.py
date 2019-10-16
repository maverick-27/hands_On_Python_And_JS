def filereading():
    print( "Printing data from file :")
    f= open('data.csv','r')

    for line in f:
        line = line.split('|')
        print(line)


if __name__ == "__main__": 
    print( "A python program to read data from a CSV file")
    filereading()
else: 
    print("")