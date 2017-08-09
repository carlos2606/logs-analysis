# logs-analysis
Logs analyzer for a newspaper website.

## Steps to run the application:

### Create the following views in you database

```create view a1 as select to_char(time,'FMMonth FMDD, YYYY'), count(status) as total from log
where status = '404 NOT FOUND'
group by to_char(time,'FMMonth FMDD, YYYY')
;```

```create view r2 as select to_char(time,'FMMonth FMDD, YYYY'), count(status) as total from log
group by to_char(time,'FMMonth FMDD, YYYY')
;```

```create view rate_val as
select r2.to_char, cast(a1.total*100 as float)/ cast(r2.total as float) as val from a1,r2 where a1.to_char = r2.to_char;```

### Run the following file

```python3 analyzer.py```