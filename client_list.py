def main():
    num = 0
    
    infile = open('clients.txt','r')

    for i in infile:
        num = num+1
        print(num,". ",i.strip('\n'),sep='')

main()