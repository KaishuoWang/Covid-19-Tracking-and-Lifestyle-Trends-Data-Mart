import datetime
import holidays
import psycopg2

canadian_holidays = holidays.CA()
year = 2020

def get_day(given_day_of_week):
    if given_day_of_week == 1:
        return 'Monday'
    elif given_day_of_week == 2:
        return "Tuesday"
    elif given_day_of_week == 3:
        return "Wednesday"
    elif given_day_of_week == 4:
        return "Thursday"
    elif given_day_of_week == 5:
        return "Friday"
    elif given_day_of_week == 6:
        return "Saturday"
    elif given_day_of_week == 7:
        return "Sunday"

server = 'www.eecs.uottawa.ca'
userName = 'kwang126'
myPassword = 'fojVu2-qexpep-bozwyt'
group = 'group_10'
myPort = 15432

connection = psycopg2.connect(dbname = group, user = userName, password = myPassword, host = server, port = myPort)
cur=connection.cursor()

cur.execute('create table date_dimension(date_key int, day int, month int, day_of_week int, week_in_year int, year int, weekend bool, holiday bool, season varchar, primary key (date_key) );')
cur.execute('insert into date_dimension values(0, null, null, null, null, null, null, null, null)')
connection.commit()

def insert_into_db(key, day, month, day_of_week, week_of_year, year, if_weekend, if_holiday, season):
    global connection
    global cur

    cur.execute('INSERT into date_dimension values(%s, %s, %s, %s, %s ,%s, %s, %s, %s)', (key, day, month, day_of_week, week_of_year, year, if_weekend, if_holiday, season))

    connection.commit()

counter = 0

for eachDay in range(1,31):
    counter += 1
    month = 9
    season = 'Fall'
    day = eachDay
    if_holiday = datetime.date(year, month, day) in canadian_holidays
    day_of_week = datetime.date(year, month, day).isocalendar()[2]
    if_weekend = day_of_week > 5
    week_of_year = datetime.date(year, month, day).isocalendar()[1]
    insert_into_db(counter, day, month, day_of_week, week_of_year, year, if_weekend, if_holiday, season)

for eachDay in range(1,32):
    counter += 1
    month = 10
    day = eachDay
    season = 'Fall'
    if_holiday = datetime.date(year, month, day) in canadian_holidays
    day_of_week = datetime.date(year, month, day).isocalendar()[2]
    if_weekend = day_of_week > 5
    week_of_year = datetime.date(year, month, day).isocalendar()[1]
    insert_into_db(counter, day, month, day_of_week, week_of_year, year, if_weekend, if_holiday, season)

for eachDay in range(1,31):
    counter += 1
    month = 11
    day = eachDay
    season = 'Fall'
    if_holiday = datetime.date(year, month, day) in canadian_holidays
    day_of_week = datetime.date(year, month, day).isocalendar()[2]
    if_weekend = day_of_week > 5
    week_of_year = datetime.date(year, month, day).isocalendar()[1]
    insert_into_db(counter, day, month, day_of_week, week_of_year, year, if_weekend, if_holiday, season)

for eachDay in range(1,32):
    counter += 1
    month = 12
    day = eachDay
    season = 'Winter'
    if_holiday = datetime.date(year, month, day) in canadian_holidays
    day_of_week = datetime.date(year, month, day).isocalendar()[2]
    if_weekend = day_of_week > 5
    week_of_year = datetime.date(year, month, day).isocalendar()[1]
    insert_into_db(counter, day, month, day_of_week, week_of_year, year, if_weekend, if_holiday, season)

cur.close()
connection.close()
