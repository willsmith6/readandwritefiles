# Import the customers.csv file using the csv module. 
#Read it and create a new file with only the full customer name and country 
#they are from. Display the total number of customers read from the file.

import csv
def main():

    num = 0
    infile = open('customers.csv','r')
    outfile = open('customer_country.csv','w')
    csvfile = csv.reader(infile, delimiter=',')
    next(csvfile)

    for record in csvfile:
        outfile.write(record[1])
        outfile.write(" ")
        outfile.write(record[2])
        outfile.write(": ")
        outfile.write(record[4])
        outfile.write("\n")
        num = num + 1

    outfile.write("The total number of customers is: ")

    outfile.write(str(num))
    outfile.close()
main()