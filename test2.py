def main():
    
    import csv

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile, delimiter=',')
    outfile = open('avg_steps.csv','w')
    counter = 1

    jan_total = 0
    feb_total = 0
    mar_total = 0
    apr_total = 0
    may_total = 0
    june_total = 0
    july_total = 0
    aug_total = 0
    sept_total = 0
    oct_total = 0
    nov_total = 0
    dec_total = 0

    jan_cnt = 0
    feb_cnt = 0
    mar_cnt = 0
    apr_cnt = 0
    may_cnt = 0
    june_cnt = 0
    july_cnt = 0
    aug_cnt = 0
    sept_cnt = 0
    oct_cnt = 0
    nov_cnt = 0
    dec_cnt = 0

    next(csvfile)
    for record in csvfile: 
        if record[0] == str(1):   
            jan = int(record[1])
            jan_total = jan + jan_total
            jan_cnt += 1
        
        counter = counter+1
        if record[0] == str(2):   
            feb = int(record[1])
            feb_total = feb + feb_total
            feb_cnt += 1

        counter = counter+1
        if record[0] == str(3):   
            mar = int(record[1])
            mar_total = mar + mar_total
            mar_cnt += 1

        counter = counter+1
        if record[0] == str(4):   
            apr = int(record[1])
            apr_total = apr + apr_total
            apr_cnt += 1

        counter = counter+1
        if record[0] == str(5):   
            may = int(record[1])
            may_total = may + may_total
            may_cnt += 1

        counter = counter+1
        if record[0] == str(6):   
            june = int(record[1])
            june_total = june + june
            june_cnt += 1

        counter = counter+1
        if record[0] == str(7):   
            july = int(record[1])
            july_total = july + july_total
            july_cnt += 1

        counter = counter+1
        if record[0] == str(8):   
            aug = int(record[1])
            aug_total = aug + aug_total
            aug_cnt += 1

        counter = counter+1
        if record[0] == str(9):   
            sept = int(record[1])
            sept_total = sept + sept_total
            sept_cnt += 1

        counter = counter+1
        if record[0] == str(10):   
            octo = int(record[1])
            oct_total = octo + oct_total
            oct_cnt += 1

        counter = counter+1
        if record[0] == str(11):   
            nov = int(record[1])
            nov_total = nov + not_total
            nov_cnt += 1

        counter = counter+1
        if record[0] == str(12):   
            dec = int(record[1])
            dec_total = dec + dec_total
            dec_cnt += 1


        outfile.write('January Average: ')
        jan_avg = (jan_total)/(jan_cnt)
        outfile.write(str(jan_avg))
        outfile.write('\n')

        outfile.write('February Average: ')
        feb_avg = (feb_total)/(feb_cnt)
        outfile.write(str(feb_avg))
        outfile.write('\n')

        outfile.write('March Average: ')
        mar_avg = (mar_total)/(mar_cnt)
        outfile.write(str(mar_avg))
        outfile.write('\n')

        outfile.write('April Average: ')
        apr_avg = (apr_total)/(apr_cnt)
        outfile.write(str(apr_avg))
        outfile.write('\n')

        outfile.write('May Average: ')
        may_avg = (may_total)/(may_cnt)
        outfile.write(str(may_avg))
        outfile.write('\n')

        outfile.write('June Average: ')
        june_avg = (june_total)/(june_cnt)
        outfile.write(str(june_avg))
        outfile.write('\n')

        outfile.write('July Average: ')
        july_avg = (july_total)/(july_cnt)
        outfile.write(str(july_avg))
        outfile.write('\n')

        outfile.write('August Average: ')
        aug_avg = (aug_total)/(aug_cnt)
        outfile.write(str(aug_avg))
        outfile.write('\n')

        outfile.write('September Average: ')
        sept_avg = (sept_total)/(sept_cnt)
        outfile.write(str(sept_avg))
        outfile.write('\n')

        outfile.write('October Average: ')
        oct_avg = (oct_total)/(oct_cnt)
        outfile.write(str(oct_avg))
        outfile.write('\n')
                
        outfile.write('November Average: ')
        nov_avg = (nov_total)/(nov_cnt)
        outfile.write(str(nov_avg))
        outfile.write('\n')

        outfile.write('December Average: ')
        dec_avg = (dec_total)/(dec_cnt)
        outfile.write(str(dec_avg))
        outfile.write('\n')

main()