import csv

infile = open('steps.csv','r')
csvfile = csv.reader(infile, delimiter=',')
outfile = open('avg_steps.csv','w')


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

jan_counter = 0
feb_counter = 0
mar_counter = 0
apr_counter = 0
may_counter = 0
june_counter = 0
july_counter = 0
aug_counter = 0
sept_counter = 0
oct_counter = 0
nov_counter = 0
dec_counter = 0

next(csvfile)
for record in csvfile:
    while record[0] == 1:
        jan_total += int(record[1])
        jan_counter = jan_counter+1
        jan_avg = (jan_total/jan_counter)
    while record[0] == 2:
        feb_total += int(record[1])
        feb_counter = feb_counter+1
    while record[0] == 3:
        mar_total += int(record[1])
        mar_counter = mar_counter+1
    while record[0] == 4:
        apr_total += int(record[1])
        apr_counter = apr_counter+1
    while record[0] == 5:
        may_total += int(record[1])
        may_counter = may_counter+1
    while record[0] == 6:
        june_total += int(record[1])
        june_counter = june_counter+1
    while record[0] == 7:
        july_total += int(record[1])
        july_counter = july_counter+1
    while record[0] == 8:
        aug_total += int(record[1])
        aug_counter = aug_counter+1
    while record[0] == 9:
        sept_total += int(record[1])
        sept_counter = sept_counter+1
    while record[0] == 10:
        oct_total += int(record[1])
        oct_counter = oct_counter+1
    while record[0] == 11:
        nov_total += int(record[1])
        nov_counter = nov_counter+1
    while record[0] == 12:
        dec_total += int(record[1])
        dec_counter = dec_counter+1

'''
    jan_avg = (jan_total/jan_counter)
    feb_avg = (feb_total/feb_counter)
    mar_avg = (mar_total/mar_counter)
    apr_avg = (apr_total/apr_counter)
    may_avg = (may_total/may_counter)
    june_avg = (june_total/june_counter)
    july_avg = (july_total/july_counter)
    aug_avg = (aug_total/aug_counter)
    sept_avg = (sept_total/sept_counter)
    oct_avg = (oct_total/oct_counter)
    nov_avg = (nov_total/nov_counter)
    dec_avg = (dec_total/dec_counter)
'''

'''
outfile.write(str(jan_avg))
outfile.write(str(feb_avg))
outfile.write(str(mar_avg))
outfile.write(str(apr_avg))
outfile.write(str(may_avg))
outfile.write(str(june_avg))
outfile.write(str(july_avg))
outfile.write(str(aug_avg))
outfile.write(str(sept_avg))
outfile.write(str(oct_avg))
outfile.write(str(nov_avg))
outfile.write(str(dec_avg))
'''