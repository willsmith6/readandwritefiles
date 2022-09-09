def main():
    
    import csv

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile, delimiter=',')
    outfile = open('avg_steps.csv','w')
    counter = 1
    step_total = 0
    month_cnt = 0

    next(csvfile)
    for record in csvfile: 
        if record[0] == str(counter):   
            step_cnt = int(record[1])
            step_total = step_cnt + step_total
            month_cnt += 1

        #outfile.write('Monthly Total: ')
        #outfile.write(str(step_total))
        #outfile.write(' ')

        outfile.write('Monthly Average: ')
        monthly_avg = (step_total)/(month_cnt)
        outfile.write(str(monthly_avg))

        outfile.write('\n')

main()