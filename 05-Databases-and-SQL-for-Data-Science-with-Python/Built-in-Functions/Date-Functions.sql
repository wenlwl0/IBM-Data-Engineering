SELECT DAY(RESCUEDATE) FROM PETRESCUE;
SELECT MONTH(RESCUEDATE) FROM PETRESCUE;
SELECT YEAR(RESCUEDATE) FROM PETRESCUE;
-- query that displays the rescue date.

SELECT DATE_ADD(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE
--interval to be added to the date in the column.
--displays third day of each rescue

SELECT DATE_ADD(RESCUEDATE, INTERVAL 2 MONTH) FROM PETRESCUE
--add 2 months to date

SELECT DATE_SUB(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE
--retrieve a date before the one given in the column by a given number using the function DATE_SUB

SELECT DATEDIFF(CURRENT_DATE, RESCUEDATE) FROM PETRESCUE
--query that displays the length of time the animals have been rescued, for example, the difference between the current date and the rescue date

SELECT FROM_DAYS(DATEDIFF(CURRENT_DATE, RESCUEDATE)) FROM PETRESCUE
--To present the output in a YYYY-MM-DD format, another function FROM_DAYS(number_of_days)can be used. This function takes a number of days and returns the required formatted output

