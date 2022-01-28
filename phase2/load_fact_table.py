from typing import Counter
import psycopg2
import psycopg2.extras as extras
from csv import reader
import datetime

processed = []
date = []
patient = []
mobility_measure = []
special_measures = []
weather_dimension = []
phu_location = []

server = 'www.eecs.uottawa.ca'
userName = 'kwang126'
myPassword = 'fojVu2-qexpep-bozwyt'
group = 'group_10'
myPort = 15432
    
connection = psycopg2.connect(dbname = group, user = userName, password = myPassword, host = server, port = myPort)
cur = connection.cursor()

cur.execute('create table fact_table(onset_date_key int,reported_date_key int,test_date_key int,specimen_date_key int,patient_key int,PHU_location_key int,mobility_key int,special_measure_key int,weather_key int,resolved boolean,unresolved boolean,fatal boolean,FOREIGN KEY (onset_date_key) REFERENCES date_dimension(date_key),FOREIGN KEY (reported_date_key) REFERENCES date_dimension(date_key),FOREIGN KEY (test_date_key) REFERENCES date_dimension(date_key),FOREIGN KEY (specimen_date_key) REFERENCES date_dimension(date_key),FOREIGN KEY (patient_key) REFERENCES patient_dimension(patient_key),FOREIGN KEY (PHU_location_key) REFERENCES phu_location_dimension(phu_location_key),FOREIGN KEY (mobility_key) REFERENCES mobility_dimension(mobility_key),FOREIGN KEY (special_measure_key) REFERENCES special_measures_dimension(special_measures_key),FOREIGN KEY (weather_key) REFERENCES weather_dimension(weather_key));')
connection.commit()

def get_all_dimension():
    global date
    global patient
    global mobility_measure
    global special_measures
    global weather_dimension
    global phu_location

    cur.execute('SELECT * FROM date_dimension where date_key <> 0')
    date = cur.fetchall()
    cur.execute('SELECT * FROM patient_dimension where patient_key <> 0')
    patient = cur.fetchall()
    cur.execute('SELECT * FROM mobility_dimension where mobility_key <> 0')
    mobility_measure = cur.fetchall()
    cur.execute('SELECT * FROM special_measures_dimension where special_measures_key <> 0')
    special_measures = cur.fetchall()
    cur.execute('SELECT * FROM weather_dimension where weather_key <> 0')
    weather_dimension = cur.fetchall()
    cur.execute('SELECT * FROM phu_location_dimension where phu_location_key <> 0')
    phu_location = cur.fetchall()

def process_cases():
    with open('./source_files/Confirmed_positive_cases_of_COVID19_in_Ontario.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row[3][0:7] == '2020-09' or row[3][0:7] == '2020-10' or row[3][0:7] == '2020-11' or row[3][0:7] == '2020-12':
                if 'Toronto' in row[12] or 'Ottawa' in row[12] or 'Durham' in row[12] or 'Halton' in row[12] or 'Peel' in row[12] or 'York' in row[12]:
                    processed.append(row)

def get_patient(patient_id):
    global patient
    for each_patient in patient:
        if each_patient[1] == patient_id:
            return each_patient[0]
    return 0

def get_mobility(reported_date, city):
    for each_row in mobility_measure:
        if each_row[4] == reported_date and each_row[2] == city:
            return each_row[0]
    return 0

def get_weather(reported_date, city):
    for each_row in weather_dimension:
        if each_row[5] == reported_date and each_row[4] == city:
            return each_row[0]
    return 0

def get_special_measure(reported_date):
    date_time_obj1 = datetime.datetime.strptime(reported_date, '%Y-%m-%d').date()
    for each_row in special_measures:
        if each_row[6] != 'null':
            if datetime.datetime.strptime(each_row[5], '%Y-%m-%d').date() <= date_time_obj1 and datetime.datetime.strptime(each_row[6], '%Y-%m-%d').date() >= date_time_obj1:
                return each_row[0]
        else:
            if datetime.datetime.strptime(each_row[5], '%Y-%m-%d').date() <= date_time_obj1:
                return each_row[0]
    return 0

def get_PHU(name):
    for each_row in phu_location:
        if each_row[1] == name:
            return each_row[0]
    return 0

def get_date(day, month):
    if day == '' or month == '':
        return
    for each_row in date:
        if each_row[1] == int(day) and each_row[2] == int(month):
            return each_row[0]
    return 0

def process_date(input):
    if input.strip() == '':
        return -1
    if input[0] == '0':
        return input[1]
    else:
        return input

get_all_dimension()
process_cases()
counter = 1
data = []
insert_query = 'INSERT into fact_table values %s'
for each_row in processed:
    print(counter)
    patient_key = get_patient(str(each_row[0]))

    month = each_row[2][5:7]
    day = each_row[2][8:10]
    onset = get_date(day, month)

    month = each_row[3][5:7]
    day = each_row[3][8:10]
    report = get_date(day, month)

    month = each_row[4][5:7]
    day = each_row[4][8:10]
    test = get_date(day, month)

    month = each_row[5][5:7]
    day = each_row[5][8:10]
    specimen = get_date(day, month)

    phu = get_PHU(each_row[12].strip())
    if each_row[12].strip()[0] == 'Y':
        city = 'York'
    elif each_row[12].strip()[0] == 'P':
        city = 'Peel'
    elif each_row[12].strip()[0] == 'T':
        city = 'Toronto'
    elif each_row[12].strip()[0] == 'O':
        city = 'Ottawa'
    elif each_row[12].strip()[0] == 'D':
        city = 'Durham'
    elif each_row[12].strip()[0] == 'H':
        city = 'Halton'
    mobility = get_mobility(each_row[3][0:10], city)
    special = get_special_measure(each_row[3][0:10])
    weather = get_weather(each_row[3][0:10], city)
    if each_row[9] == 'Not Resolved':
        resolved = False
        unresolved = True
        fatal = False
    elif each_row[9] == 'Resolved':
        resolved = True
        unresolved = False
        fatal = False
    
    if counter % 2000 != 0:
        data.append((onset, report, test, specimen, patient_key, phu, mobility, special, weather, resolved, unresolved, fatal))
    else:
        print('insert:' + str(counter))
        extras.execute_values(cur, insert_query, data, template=None, page_size=2000)
        connection.commit()
        data.clear()
    
    counter += 1

cur.close()
connection.close()