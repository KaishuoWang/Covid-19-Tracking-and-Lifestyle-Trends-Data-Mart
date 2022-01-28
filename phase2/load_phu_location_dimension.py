import psycopg2
from csv import reader

server = 'www.eecs.uottawa.ca'
userName = 'kwang126'
myPassword = 'fojVu2-qexpep-bozwyt'
group = 'group_10'
myPort = 15432

processed_phu_location = []
phu_id = []
    
connection = psycopg2.connect(dbname = group, user = userName, password = myPassword, host = server, port = myPort)
cur = connection.cursor()

cur.execute('CREATE TABLE phu_location_dimension(phu_location_key int PRIMARY KEY, phu_name varchar, address varchar, city varchar, postal_code varchar, province varchar, URL varchar, latitude varchar, longitude varchar);')
cur.execute('insert into phu_location_dimension values(0,null,null,null,null,null,null,null,null)')
connection.commit()

with open('./source_files/Confirmed_positive_cases_of_COVID19_in_Ontario.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[3][0:7] == '2020-09' or row[3][0:7] == '2020-10' or row[3][0:7] == '2020-11' or row[3][0:7] == '2020-12':
            if 'Toronto' in row[12] or 'Ottawa' in row[12] or 'Durham' in row[12] or 'Halton' in row[12] or 'Peel' in row[12] or 'York' in row[12]:
                if row[11] not in phu_id:
                    processed_phu_location.append(row)
                    phu_id.append(row[11])


def check_empty(keyword):
    if keyword == '' or keyword == '%':
        return 'null'
    else:
        return keyword

counter = 1
for each_row in processed_phu_location:
    phu_name = check_empty(each_row[12].strip())
    address = check_empty(each_row[13].strip())
    city = check_empty(each_row[14].strip())
    postal_code = check_empty(each_row[15].strip())
    province = 'ON'
    url = check_empty(each_row[16].strip())
    Reporting_PHU_Latitude = check_empty(each_row[17].strip())
    Reporting_PHU_Longitude = check_empty(each_row[18].strip())
    
    cur.execute('INSERT into phu_location_dimension values(%s, %s, %s, %s, %s, %s ,%s, %s, %s)', (counter, phu_name, address, city, postal_code, province, url, Reporting_PHU_Latitude, Reporting_PHU_Longitude))

    counter += 1

connection.commit()
cur.close()
connection.close()
