--iceberg
--find top 5 weeks with the highest number of resolved cases
SELECT D.week_in_year, count(*) AS num_resolved_case
FROM fact_table F, date_dimension D
WHERE F.reported_date_key = D.date_key AND 
	  F.Resolved = true
group by D.week_in_year
ORDER BY num_resolved_case DESC FETCH FIRST 5 ROWS ONLY;

--windowing
--show the ranking of the PHUs in terms of the number of cases of October
SELECT P.PHU_name, count(*) AS num_of_cases,
RANK() OVER (ORDER BY count(*) desc)
FROM fact_table F, date_dimension D, phu_location_dimension P
WHERE F.reported_date_key = D.Date_key AND F.Phu_Location_key = P.Phu_Location_key AND D.Month = 10
GROUP BY(D.Month,P.phu_name)

--Window clause
--compare the number of resolved cases in Ottawa to that of the previous and next months
select D.month, count(*) from fact_table F, date_dimension D, phu_location_dimension P
where F.reported_date_key = D.date_key and F.phu_location_key = P.phu_location_key and P.city = 'Ottawa'
and (D.month = 10 or D.month = 9 or D.month = 11) and F.resolved = true
group by D.month
order by D.month

--Combining
--explore the number of cases for different Month
SELECT D.month, count(F.patient_key) as num_of_cases 
FROM fact_table F, date_dimension D
WHERE F.reported_date_key = D.date_key
GROUP BY D.month

--explore the number of cases for different age group
SELECT P.age_group, count(F.patient_key) as num_of_cases 
FROM fact_table F, patient_dimension P
WHERE F.patient_key = P.patient_key 
GROUP BY P.age_group

--explore the number of cases contrasting mobility levels in Ottawa and Peel
select subregion, round(avg(retail_and_recreation),2) AS avg_retail_and_recreation, round(avg(grocery),2) as avg_grocery, 
round(avg(parks),2) as avg_parks, round(avg(transit_stations),2) as avg_transit_stations, round(avg(workplaces),2) as avg_workplaces, round(avg(residential),2) as avg_residential
from mobility_dimension
where subregion = 'Ottawa' or subregion = 'Peel'
group by subregion


--Roll-up
--roll up to all unresolved cases in data mart
select P.area, P.city, count(F.patient_key) as unresolved_cases from
fact_table F, phu_location_dimension P
where F.unresolved = true
rollup(P.area, P.city)

--Drill-down
--drill down to number of cases on 15 Sept
SELECT D.day, D.month, count(T.patient_key) AS num_of_cases
FROM date_dimension AS D, fact_table AS T
WHERE T.Reported_date_key = D.date_key and D.month = 9 and D.day = 15
GROUP BY D.day, D.month

--Slice
--The number of case (unresolved and fatal) during each spcial measure
SELECT S.title, P.phu_name, count(T.patient_key) num_of_cases
FROM fact_table AS T, special_measures_dimension AS S, phu_location_dimension P
WHERE T.special_measure_key = S.special_measures_key
	and T.phu_location_key = P.phu_location_key
	and T.special_measure_key <> 0
	and S.title = 'Lower Limits for Unmonitored and Private Social Gatherings in Ottawa, Peel and Toronto Regions'
GROUP BY S.title, P.phu_name

--the number of cases in a specific PHU (resolved, unresolved)
select R.phu_name, R.num_of_resolved, U.num_of_unresolved from
	(SELECT P.phu_name, count(F.patient_key) num_of_resolved
	FROM fact_table AS F, phu_location_dimension AS P
	WHERE F.phu_location_key = P.phu_location_key and 
	 	P.phu_name = 'Peel Public Health' and
	 	F.resolved = true
	GROUP BY P.phu_name) R
join
	(SELECT P.phu_name, count(F.patient_key) num_of_unresolved
	FROM fact_table AS F, phu_location_dimension AS P
	WHERE F.phu_location_key = P.phu_location_key and 
	 	P.phu_name = 'Peel Public Health' and
	 	F.unresolved = true
	GROUP BY P.phu_name) U
on R.phu_name = U.phu_name

--Dice
--The numbe of cases during a period of two months in Ottawa and Mississauga.
SELECT D.month, P.city, count(T.fatal) num_of_fatal
FROM fact_table AS T, date_dimension AS D, phu_location_dimension AS P
WHERE T.PHU_location_key = P.PHU_location_key AND
   T.Reported_date_key = D.date_key AND
   D.month IN (9, 10) AND
   P.city IN ('Mississauga', 'Ottawa')
GROUP BY T.fatal, D.month, P.city
order by D.month

--provide the number of unresolved cases when contrasting parks and transit in Peel and Toronto.
SELECT M.subregion, round(avg(M.parks),2), round(avg(M.transit_stations),2), count(T.fatal)
FROM fact_table AS T, mobility_dimension AS M
WHERE T.mobility_key = M.mobility_key AND
   M.subregion IN ('Toronto', 'Peel') and
   T.unresolved = true
GROUP BY M.subregion