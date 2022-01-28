import psycopg2
from csv import reader

processed_patient = []

server = 'www.eecs.uottawa.ca'
userName = 'kwang126'
myPassword = 'fojVu2-qexpep-bozwyt'
group = 'group_10'
myPort = 15432
    
connection = psycopg2.connect(dbname = group, user = userName, password = myPassword, host = server, port = myPort)
cur = connection.cursor()

cur.execute('CREATE TABLE patient_dimension(patient_key int PRIMARY KEY, patient_id varchar, gender varchar, age_group varchar, aquisition_group varchar, outbreak_related BOOLEAN);')
cur.execute('insert into patient_dimension values(0, null, null, null, null, null)')
connection.commit()

with open('./source_files/Confirmed_positive_cases_of_COVID19_in_Ontario.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[3][0:7] == '2020-09' or row[3][0:7] == '2020-10' or row[3][0:7] == '2020-11' or row[3][0:7] == '2020-12':
            if 'Toronto' in row[12] or 'Ottawa' in row[12] or 'Durham' in row[12] or 'Halton' in row[12] or 'Peel' in row[12] or 'York' in row[12]:
                processed_patient.append(row)

def check_empty(keyword):
    if keyword == '' or keyword == '%':
        return 'null'
    else:
        return keyword

counter = 1
for each_row in processed_patient:
    print(counter)
    patient_id = check_empty(each_row[0].strip())
    gender = check_empty(each_row[7].strip())
    age_group = check_empty(each_row[6].strip())
    acquisition_group = check_empty(each_row[8].strip())
    if each_row[10].strip() == '':
        outbreak_related = False
    else:
        outbreak_related = True

    cur.execute('INSERT into patient_dimension values(%s, %s, %s, %s, %s, %s)', (counter, patient_id, gender, age_group, acquisition_group, outbreak_related))
    
    counter += 1

connection.commit()
cur.close()
connection.close()
