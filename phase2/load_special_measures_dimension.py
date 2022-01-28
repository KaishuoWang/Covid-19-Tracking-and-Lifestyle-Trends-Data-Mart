import psycopg2

server = 'www.eecs.uottawa.ca'
userName = 'kwang126'
myPassword = 'fojVu2-qexpep-bozwyt'
group = 'group_10'
myPort = 15432

connection = psycopg2.connect(dbname = group, user = userName, password = myPassword, host = server, port = myPort)
cur=connection.cursor()

cur.execute('create table special_measures_dimension(special_measures_key int,title varchar,description varchar,keyword_1 varchar,keyword_2 varchar,start_date varchar,end_date varchar,url varchar,primary key (special_measures_key));')
cur.execute('insert into special_measures_dimension values(0,null,null,null,null,null,null,null)')
connection.commit()

def insert_into_db(key, title, description, keyword_1, keyword_2, start_date, end_date, url):
    global connection
    global cur

    cur.execute('INSERT into special_measures_dimension values(%s, %s, %s, %s, %s ,%s, %s, %s)', (key, title, description, keyword_1, keyword_2, start_date, end_date, url))

    connection.commit()

key = 1
title = 'Lower Limits for Unmonitored and Private Social Gatherings in Ottawa, Peel and Toronto Regions'
description = 'Unmonitored and private social gatherings include functions, parties, dinners, gatherings, BBQs or wedding receptions held in private residences, backyards, parks and other recreational areas. 10 people at an indoor event or gathering (previous limit of 50); or 25 people at an outdoor event or gathering (previous limit of 100). Indoor and outdoor events and gatherings cannot be merged together. These are not accumulative and gatherings of 35 (25 outdoors and 10 indoors) are not permitted. The new limits will only apply to persons within the boundaries of the following public health units: Ottawa Public Health; Peel Public Health; and Toronto Public Health.'
keyword_1 = 'Unmonitored and Private Social Gatherings'
keyword_2 = 'limit'
start_date = '2020-09-18'
end_date = '2020-10-22'
url = 'https://news.ontario.ca/en/release/58402/lower-limits-for-unmonitored-and-private-social-gatherings-in-ottawa-peel-and-toronto-regions'
insert_into_db(key, title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 2
title = 'New Public Health Measures Implemented Provincewide to Keep Ontarians Safe'
description = 'Over the past five weeks, Ontario has experienced an increase in the rate of new COVID-19 cases. Private social gatherings continue to be a significant source of transmission in many local communities, along with outbreak clusters in restaurants, bars, and other food and drink establishments, including strip clubs, with most cases in the 20-39 age group. To ensure the continued health and safety of Ontarians, reduce the risk of transmission, and limit future outbreaks of COVID-19, the amended order will apply province-wide effective 12:01 a.m. on Saturday September 26 and will: Apply additional measures and restrictions to restaurants, bars and other food and drink establishments (including nightclubs) by prohibiting the sale of alcohol after 11 p.m., and prohibiting the consumption of alcohol on the premises after 12:00 a.m. until 9:00 a.m. (including employees), and requiring establishments to close by 12:00 a.m. and remain closed until 5:00 a.m. except for takeout or delivery; Close all strip clubs across the province; and Require businesses or organizations to comply with any advice, recommendations, and instructions issued by the Office of the Chief Medical Officer of Health on screening for COVID-19.'
keyword_1 = 'restaurants, bars and other food and drink establishments (including nightclubs), strip clubs'
keyword_2 = 'Reduce business hours or shut down completely'
start_date = '2020-09-26'
end_date = '2020-10-22'
url = 'https://news.ontario.ca/en/release/58548/new-public-health-measures-implemented-provincewide-to-keep-ontarians-safe'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 3
title = 'Ontario Implementing Additional Public Health and Testing Measures to Keep People Safe'
description = 'Extending the pause on any further reopening of businesses, facilities, and organizations for an additional 28 days, unless already permitted to open under O. Reg 364/20; Targeted measures will also be implemented in Ottawa, Peel, and Toronto as a result of their higher than average rates of transmission. These include: Setting an indoor capacity limit to restrict occupancy at restaurants, bars and other food and drink establishments (including nightclubs) to the number of patrons who can maintain a physical distance of at least two metres from every other patron, to a maximum of 100 patrons, permitting no more than six patrons per table, requiring operators to ensure patrons lining up or congregating outside of their establishment maintain physical distancing, and mandating that the name and contact information for each patron be collected; Restricting group exercise classes at gyms and other fitness settings to 10 individuals, as well as restricting the total number of people allowed at these facilities to a maximum of 50; and Setting a limit on the number of people allowed at meeting and event facilities, including banquet halls, to six people per table and 50 people per facility.'
keyword_1 = 'pause on any further reopening of businesses, facilities, and organizations'
keyword_2 = 'Limit the number of people gathered'
start_date = '2020-10-03'
end_date = '2020-10-22'
url = 'https://news.ontario.ca/en/release/58645/ontario-implementing-additional-public-health-and-testing-measures-to-keep-people-safe'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 4
title = 'Ontario Implementing Additional Public Health Measures in Toronto, Ottawa and Peel Region'
description = 'Reducing limits for all social gatherings and organized public events to a maximum of 10 people indoors and 25 people outdoors where physical distancing can be maintained. The two limits may not be combined for an indoor-outdoor event; Prohibiting indoor food and drink service in restaurants, bars and other food and drink establishments, including nightclubs and food court areas in malls; Closing of: Indoor gyms and fitness centres (i.e., exercise classes and weight and exercise rooms); Casinos, bingo halls and other gaming establishments; Indoor cinemas; Performing arts centres and venues; Spectator areas in racing venues; Interactive exhibits or exhibits with high risk of personal contact in museums, galleries, zoos, science centres, landmarks, etc.; Prohibiting personal care services where face coverings must be removed for the service (e.g. makeup application, beard trimming); Reducing the capacity limits for: Tour and guide services to 10 people indoors and 25 people outdoors Real estate open houses to 10 people indoors, where physical distancing can be maintained. In-person teaching and instruction (e.g. cooking class) to 10 people indoors and 25 people outdoors, with exemptions for schools, child care centres, universities, colleges of applied arts and technology, private career colleges, the Ontario Police College, etc. Meeting and event spaces to 10 people indoors and 25 people outdoors, and Limiting team sports to training sessions (no games or scrimmages).'
keyword_1 = 'Additional Public Health Measures'
keyword_2 = 'Toronto, Ottawa and Peel Region'
start_date = '2020-10-10'
end_date = '2020-10-22'
url = 'https://news.ontario.ca/en/release/58767/ontario-implementing-additional-public-health-measures-in-toronto-ottawa-and-peel-region'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 5
title = 'Ontario Moving Additional Region to Modified Stage 2'
description = 'Reducing limits for all social gatherings and organized public events to a maximum of 10 people indoors and 25 people outdoors where physical distancing can be maintained. The two limits may not be combined for an indoor-outdoor event; Prohibiting indoor food and drink service in restaurants, bars and other food and drink establishments, including nightclubs and food court areas in malls; Closing of: Indoor gyms and fitness centres (i.e., exercise classes and weight and exercise rooms); Casinos, bingo halls and other gaming establishments; Indoor cinemas, performing arts centres and venues, (except for rehearsing or performing a recorded or broadcasted performance subject to conditions, including no spectators); Spectator areas in racing venues; Interactive exhibits or exhibits with high risk of personal contact in museums, galleries, zoos, science centres, landmarks, etc.; Prohibiting personal care services where face coverings must be removed for the service (e.g. makeup application, beard trimming); Prohibiting real estate open houses (permitting in-person showing by appointments only) Reducing the capacity limits for: Tour and guide services to 10 people indoors and 25 people outdoors In-person teaching and instruction (e.g. cooking class) to 10 people indoors and 25 people outdoors, with certain exemptions, including for schools, universities, colleges of applied arts and technology, private career colleges, the Ontario Police College, etc. Meeting and event spaces to 10 people indoors and 25 people outdoors with limited exemptions, including for government operations and the delivery of government services; and Limiting team sports to training sessions (no games or scrimmages). Schools, child care centres, and places of worship will remain open in these communities and must continue to follow the public health measures in place. Before-school and after-school programs will also continue to be exempt from these new restrictions and will remain open.'
keyword_1 = 'Modified Stage 2'
keyword_2 = 'York Region will join Ottawa, Peel and Toronto public health regions in a modified Stage 2'
start_date = '2020-10-19'
end_date = 'null'
url = 'https://news.ontario.ca/en/release/58842/ontario-moving-additional-region-to-modified-stage-2'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 6
title = 'Ontario Moves Public Health Unit Regions into COVID-19 Response Framework to Keep Ontario Safe and Open'
description = 'Lockdown: No public health unit regions. Red-Control: Peel Regional Health Unit. Orange-Restrict: Ottawa Public Health; and York Region Public Health. Yellow-Protect: Brant County Health Unit; City of Hamilton Public Health Services; Durham Region Health Department; Eastern Ontario Health Unit; Haldimand-Norfolk Health Unit; Halton Region Public Health; Niagara Region Public Health; Region of Waterloo Public Health and Emergency Services; Simcoe Muskoka District Health Unit; and Wellington-Dufferin-Guelph Public Health. Green-Prevent: Algoma Public Health; Chatham-Kent Public Health; Grey Bruce Health Unit; Kingston, Frontenac and Lennox & Addington Public Health; Haliburton, Kawartha, Pine Ridge District Health Unit; Hastings Prince Edward Public Health; Huron Perth Public Health; Lambton Public Health; Leeds, Grenville & Lanark District Health Unit; Middlesex-London Health Unit; North Bay Parry Sound District; Northwestern Health Unit; Peterborough Public Health; Porcupine Health Unit; Public Health Sudbury & Districts; Renfrew County and District Health Unit; Southwestern Public Health; Thunder Bay District Health Unit; Timiskaming Health Unit; and Windsor-Essex County Health Unit.'
keyword_1 = 'Public Health Unit Region Classifications'
keyword_2 = 'null'
start_date = '2020-11-07'
end_date = 'null'
url = 'https://news.ontario.ca/en/release/59081/ontario-moves-public-health-unit-regions-into-covid-19-response-framework-to-keep-ontario-safe-and-o'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 7
title = 'Ontario Updating COVID-19 Response Framework to Help Stop the Spread of COVID-19'
description = 'Red-Control: Hamilton Public Health Services Halton Region Public Health Toronto Public Health York Region Public Health Orange-Restrict: Brant County Health Unit Durham Region Health Department Eastern Ontario Health Unit Niagara Region Public Health Wellington-Dufferin-Guelph Public Health Region of Waterloo Public Health Yellow-Protect: Huron Perth Public Health Middlesex-London Health Unit Public Health Sudbury & Districts Southwestern Public Health Windsor-Essex County Health Unit'
keyword_1 = 'Updated Public Health Unit Region Classifications'
keyword_2 = 'long-term care homes visitor restrictions'
start_date = '2020-11-16'
end_date = 'null'
url ='https://news.ontario.ca/en/release/59205/ontario-updating-covid-19-response-framework-to-help-stop-the-spread-of-covid-19'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 8
title = 'Ontario Taking Further Action to Stop the Spread of COVID-19'
description = 'Red-Control: Durham Region Health Department; and Region of Waterloo Public Health and Emergency Services. Orange-Restrict: Huron Perth Public Health; Simcoe Muskoka District Health Unit; Southwestern Public Health; and Windsor-Essex County Health Unit. Yellow-Protect: Chatham-Kent Public Health; Eastern Ontario Health Unit; Grey Bruce Health Unit; Kingston, Frontenac and Lennox & Addington Public Health; Peterborough Public Health; and Thunder Bay District Health Unit.'
keyword_1 = 'Updated Public Health Unit Region Classifications'
keyword_2 = 'At least 28 days'
start_date = '2020-11-23'
end_date = '2020-12-20'
url = 'https://news.ontario.ca/en/release/59305/ontario-taking-further-action-to-stop-the-spread-of-covid-19'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 9
title = 'Ontario Moving Regions to New Levels in COVID-19 Response Framework'
description = 'Red-Control: Windsor-Essex County Health Unit. Orange-Restrict: Haldimand-Norfolk Health Unit. Yellow-Protect: Hastings Prince Edward Public Health Lambton Public Health; and Northwestern Health Unit.'
keyword_1 = 'Updated Public Health Unit Region Classifications'
keyword_2 = 'null'
start_date = '2020-11-30'
end_date = '2020-12-27'
url = 'https://news.ontario.ca/en/release/59388/ontario-moving-regions-to-new-levels-in-covid-19-response-framework'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 10
title = 'Ontario Moving Three Regions to New Levels in COVID-19 Response Framework'
description = 'Orange-Restrict: Middlesex-London Health Unit; and Thunder Bay District Health Unit. Yellow-Protect: Haliburton, Kawartha, Pine Ridge District Health Unit.'
keyword_1 = 'Updated Public Health Unit Region Classifications'
keyword_2 = 'null'
start_date = '2020-12-07'
end_date = '2021-01-03'
url = 'https://news.ontario.ca/en/release/59489/ontario-moving-three-regions-to-new-levels-in-covid-19-response-framework'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 11
title = 'Ontario Extends COVID-19 Orders'
description = 'The Ontario government, in consultation with the Chief Medical Officer of Health, is extending all orders currently in force under the Reopening Ontario (A Flexible Response to COVID-19) Act, 2020 (ROA) until January 20, 2021. This extension will support the safe delivery of health care and other critical services until COVID-19 vaccines are approved and widely available.'
keyword_1 = 'Reopening Ontario (A Flexible Response to COVID-19) Act, 2020 (ROA)'
keyword_2 = 'extand'
start_date = '2020-12-10'
end_date = '2021-01-20'
url = 'https://news.ontario.ca/en/release/59551/ontario-extends-covid-19-orders-1'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 12
title = 'Ontario Moving Regions to New Levels with Stronger Public Health Measures'
description = 'Grey-Lockdown: Windsor-Essex County Health Unit; and York Region Public Health. Red-Control: Middlesex-London Health Unit; Simcoe Muskoka District Health Unit; and Wellington-Dufferin-Guelph Public Health. Orange-Restrict: Eastern Ontario Health Unit. Yellow-Protect: Leeds, Grenville and Lanark District Health Unit.'
keyword_1 = 'Updated Public Health Unit Region Classifications'
keyword_2 = 'null'
start_date = '2020-12-14'
end_date = '2021-01-10'
url = 'https://news.ontario.ca/en/release/59603/ontario-moving-regions-to-new-levels-with-stronger-public-health-measures'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 13
title = 'Ontario Taking Further Action to Limit Spread of COVID-19'
description = 'Based on the latest data, the following public health regions will move from their current level in the framework to the following levels effective Monday, December 21, 2020 at 12:01 a.m. with Peel Public Health and Toronto Public Health remaining in lockdown until at least January 4, 2021: Grey-Lockdown: City of Hamilton Public Health Services. Red-Control: Brant County Health Unit. Niagara Region Public Health. Orange-Restrict: Kingston, Frontenac and Lennox & Addington Public Health. Yellow-Protect: Timiskaming Health Unit. Green-Prevent Public Health Sudbury & Districts.'
keyword_1 = 'Updated Public Health Unit Region Classifications'
keyword_2 = 'Peel Public Health and Toronto Public Health remaining in lockdown until at least January 4, 2021'
start_date = '2020-12-21'
end_date = '2021-01-17'
url = 'https://news.ontario.ca/en/release/59776/ontario-taking-further-action-to-limit-spread-of-covid-19'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

key = 14
title = 'Ontario Announces Provincewide Shutdown to Stop Spread of COVID-19 and Save Lives'
description = 'In response to these exceptional circumstances, the Provincewide Shutdown would put in place time-limited public health and workplace safety measures similar to those in other jurisdictions. It would help stop the trend of high COVID-19 transmission in communities, preserve health system capacity, safeguard vulnerable populations and those who care for them, and save lives. Measures include, but are not limited to: Restricting indoor organized public events and social gatherings, except with members of the same household (the people you live with). Individuals who live alone may consider having exclusive close contact with one other household. Prohibiting in-person shopping in most retail settings - curbside pickup and delivery can continue. Discount and big box retailers selling groceries will be limited to 25 per cent capacity for in-store shopping. Supermarkets, grocery stores and similar stores that primarily sell food, as well as pharmacies, will continue to operate at 50 per cent capacity for in-store shopping. Restricting indoor access to shopping malls - patrons may only go to a designated indoor pickup area (by appointment only), essential retail stores that are permitted to be open (e.g. pharmacy, grocery store), or, subject to physical distancing and face covering requirements, to the food court for takeout purchases. Shopping malls may also establish outdoor designated pickup areas. Prohibiting indoor and outdoor dining. Restaurants, bars and other food or drink establishments will be permitted to operate by take out, drive-through, and delivery only.'
keyword_1 = 'provincewide lockdown'
keyword_2 = 'Schools located in some Public Health Unit regions can resume in-person instruction on January 11, 2021 for both elementary and secondary students'
start_date = '2020-12-26'
end_date = '2021-01-18'
url = 'https://news.ontario.ca/en/release/59790/ontario-announces-provincewide-shutdown-to-stop-spread-of-covid-19-and-save-lives'
insert_into_db(key,title, description, keyword_1, keyword_2, start_date, end_date, url)

cur.close()
connection.close()