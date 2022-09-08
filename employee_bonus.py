def main():
    
    import csv
    infile = open('employeepay.csv','r')
    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)
    for record in csvfile:
        emp_id = record[0]
        emp_name = (record[1]+' '+record[2])
        emp_salary = record[3]
        emp_bonus = record[4]
        total_pay = int(record[3]) + (int(record[3]) * float(record[4]))
        str(total_pay)

        print('Employee ID: ',emp_id)
        print('Employee Name: ',emp_name)
        print('Employee Salary: ',emp_salary)
        print('Employee Bonus: ',emp_bonus)
        print('Employee Total Pay: ',total_pay)
        print('')
main()