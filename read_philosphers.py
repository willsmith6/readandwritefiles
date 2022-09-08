def main():
    
    outfile = open('philosophers.txt','r')

    #file_contents = outfile.read()
    #print(file_contents)

    line1 = outfile.readline().rstrip('\n')
    line2 = outfile.readline().rstrip('\n')
    line3 = outfile.readline().rstrip('\n')

    print(line1)
    print(line2)
    print(line3)

main()