def main():

    import csv

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile, delimiter=',')
    outfile = open('avg_steps.csv','w')

    counter = 1 
    step_total = 0
    month_cnt = 0

    months = ['January','February','March','April','May','June','July','August','September','October','November','December']

    next(csvfile)


    for record in csvfile: 

        if record[0] == str(counter):   

            step_cnt = int(record[1])
            step_total = step_cnt + step_total
            month_cnt += 1
        
        else:
            month_avg = (step_total)/(month_cnt)
            #outfile.write(months)
            outfile.write(str(month_avg))
            outfile.write('\n')
            step_total = step_cnt + step_total

            counter = record[0]

    outfile.close()


main()