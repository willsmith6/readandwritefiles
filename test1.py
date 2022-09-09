def main():
    '''
    import csv

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile, delimiter=',')
    outfile = open('avg_steps.csv','w')
    counter = 1
    step_total = 0
    month_cnt = 0

    next(csvfile)
    for record in csvfile:
        for record in csvfile:
            if record[0] == str(counter):      
                step_cnt = int(record[1])
                step_total = step_cnt + step_total
                month_cnt += 1
        #outfile.write('Monthly Total: ')
        #outfile.write(str(step_total))
        #outfile.write(' ')

        if int(record[0]) == 1:
            outfile.write('Janurary, ')
        elif int(record[0]) == 2:
            outfile.write('Febuary, ')
        elif int(record[0]) == 3:
            outfile.write('March, ')
        elif int(record[0]) == 4:
            outfile.write('April, ')
        elif int(record[0]) == 5:
            outfile.write('May, ')
        elif int(record[0]) == 6:
            outfile.write('June, ')
        elif int(record[0]) == 7:
            outfile.write('July, ')
        elif int(record[0]) == 8:
            outfile.write('August, ')
        elif int(record[0]) == 9:
            outfile.write('September, ')
        elif int(record[0]) == 10:
            outfile.write('October, ')
        elif int(record[0]) == 11:
            outfile.write('Novmember, ')
        elif int(record[0]) == 12:
            outfile.write('December, ')
        elif int(record[0]) == 13:
            outfile.write('Nope')

        monthly_avg = (step_total)/(month_cnt)
        outfile.write(str(monthly_avg))
        outfile.write('\n')

        int(counter)
        step_total = 0
        month_cnt = 0
        counter = counter+1

        #outfile.write('hello world')


        #outfile.write('Monthly Average: ')
       ''' 
main()
