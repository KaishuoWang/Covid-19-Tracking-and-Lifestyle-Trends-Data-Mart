import psycopg2
from csv import reader

processed_mobility = []

with open('./source_files/2020_CA_Region_Mobility_Report.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[2] == 'Ontario':
            if row[3] == 'Ottawa Division' or row[3] == 'Toronto Division' or row[3] == 'Regional Municipality of Durham' or row[3] == 'Regional Municipality of Halton' or row[3] == 'Regional Municipality of Peel' or row[3] == 'Regional Municipality of York':
                if row[8][0:7] == '2020-09' or row[8][0:7] == '2020-10' or row[8][0:7] == '2020-11' or row[8][0:7] == '2020-12':
                    processed_mobility.append(row)

def check_empty(keyword):
    if keyword == '' or keyword == '%':
        return 'null'
    else:
        return keyword

server = 'www.eecs.uottawa.ca'
userName = 'kwang126'
myPassword = 'fojVu2-qexpep-bozwyt'
group = 'group_10'
myPort = 15432
    
connection = psycopg2.connect(dbname = group, user = userName, password = myPassword, host = server, port = myPort)
cur = connection.cursor()

cur.execute('create table mobility_dimension(mobility_key int,metro_area varchar,subregion varchar,province varchar,date varchar,retail_and_recreation int,grocery int,parks int,transit_stations int,workplaces int,residential int,primary key (mobility_key));')
cur.execute('insert into mobility_dimension values(0, null, null, null, null, null, null, null, null, null, null);')
connection.commit()

counter = 1
for each_row in processed_mobility:
    code = 'INSERT into mobility_dimension values(' + str(counter)

    metro_area = check_empty(each_row[4].strip())
    code = code + ',\'' + metro_area + '\','

    subregion = check_empty(each_row[3].strip().replace('Regional Municipality of ','').replace(' Division', ''))
    code = code + '\'' + subregion + '\','

    province = check_empty(each_row[2].strip())
    code = code + '\'' + province + '\','

    d = check_empty(each_row[8].strip())
    code = code + '\'' + d + '\','

    retail_and_recreation = check_empty(each_row[9].strip())
    code += retail_and_recreation
    code += ','

    grocery = check_empty(each_row[10].strip())
    code += grocery
    code += ','

    parks = check_empty(each_row[11].strip())
    code += parks
    code += ','

    transit_stations = check_empty(each_row[12].strip())
    code += transit_stations
    code += ','

    workplaces = check_empty(each_row[13].strip())
    code += workplaces
    code += ','

    residential = check_empty(each_row[14].strip())
    code += residential

    code += ')'
    
    cur.execute(code)
    # cur.execute('INSERT into mobility_dimension values(%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s)', (counter, metro_area, subregion, province, d, retail_and_recreation, grocery, parks, transit_stations, workplaces, residential))
    connection.commit()

    counter += 1

cur.close()
connection.close()
