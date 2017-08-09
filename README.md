# Logs Analyzer

The Logs Analyzer gathers information from a logs database of a newspaper website
to build reports.

### Prerequisites

Create the database from the newsdata.sql file provided and load the data into PostgreSQL with the following command:

```
psql -d news -f newsdata.sql
```

Before running the application, create the following views in your PostgreSQL database:

```
create view a1 as select to_char(time,'FMMonth FMDD, YYYY'), count(status) as total from log
where status = '404 NOT FOUND'
group by to_char(time,'FMMonth FMDD, YYYY')
```
```
create view r2 as select to_char(time,'FMMonth FMDD, YYYY'), count(status) as total from log
group by to_char(time,'FMMonth FMDD, YYYY')
```
```
create view rate_val as
select r2.to_char, cast(a1.total*100 as float)/ cast(r2.total as float) as val from a1,r2 where a1.to_char = r2.to_char
```

### Installing

In order to start the applicaton, run the following command:

```
python3 analyzer.py
```

## Authors

* **Carlos Montenegro** - *Initial work* - [carlos2606](https://github.com/carlos2606)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

