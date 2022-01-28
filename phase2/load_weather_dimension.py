import psycopg2
from csv import reader

processed_weather = []

with open('source_files/climate.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[5] == '2020' and (row[6] == '09' or row[6] == '9' or row[6] == '10' or row[6] == '11' or row[6] == '12'):
            processed_weather.append(row)

def check_empty(keyword):
    if keyword == '':
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

cur.execute('create table weather_dimension(weather_key int, daily_high_temperature int, daily_low_temperature int, precipitation int, city varchar, date_of_weather varchar, primary key(weather_key));')
cur.execute('insert into weather_dimension values(0, null,null,null,null,null)')
connection.commit()

counter = 1
for each_row in processed_weather:
	code = ''
	daily_high_temperature = check_empty(each_row[9].strip())
	code += daily_high_temperature
	code += ','
	daily_low_temperature = check_empty(each_row[11].strip())
	code += daily_low_temperature
	code += ','
	precipitation = check_empty(each_row[23].strip())
	code += precipitation
	code += ','
	if each_row[2].strip() == 'TORONTO NORTH YORK':
		city = 'York'
	elif each_row[2].strip() == 'TORONTO INTL A':
		city = 'Peel'
	elif each_row[2].strip() == 'TORONTO CITY':
	    city = 'Toronto'
	elif each_row[2].strip() == 'KING CITY NORTH':
	    city = 'Durham'
	elif each_row[2].strip() == 'OTTAWA CDA':
	    city = 'Ottawa'
	elif each_row[2].strip() == 'BURLINGTON PIERS (AUT)':
	    city = 'Halton'
	else:
	    city = 'null'
	
	if each_row[4].strip()[5] == '9':
		if len(each_row[4].strip()) == 8:
			date_of_weather = each_row[4].strip()[0:4] + '-09-0' + each_row[4].strip()[-1]
		else:
			date_of_weather = each_row[4].strip()[0:4] + '-09-' + each_row[4].strip()[7:9]
	else:
		date_of_weather = each_row[4].strip().replace('/','-')
		if len(date_of_weather) == 8:
			date_of_weather = date_of_weather[0:7] + '0' + date_of_weather[-1]

	cur.execute('INSERT into weather_dimension values(%s,' + code + '%s ,%s)', (counter,city,date_of_weather))
	connection.commit()

	counter += 1

cur.close()
connection.close()
