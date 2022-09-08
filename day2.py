def main():
    import csv
    
    infile = open('steps.csv','r')

    outfile = open('avg_steps.csv','w')

    months = ['January','February','March','April','May','June','July','August','September','October','November','December']


    with infile as f:
        next(f)
        csvfile = csv.reader(f, delimiter=',')
        data = list(csvfile)

    print(data)

main()
