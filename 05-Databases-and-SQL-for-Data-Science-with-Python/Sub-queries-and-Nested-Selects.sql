--retrieve all employee records whose salary is lower than the average salary
SELECT *
FROM EMPLOYEES
WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES);

--execute a query that retrieves all employee records with EMP_ID, SALARY, and maximum salary as MAX_SALARY in every row
SELECT EMP_ID, SALARY, (SELECT MAX(SALARY) FROM EMPLOYEES) AS MAX_SALARY 
FROM EMPLOYEES;

--extract the first and last names of the oldest employee
SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE B_DATE = (SELECT MIN(B_DATE) FROM EMPLOYEES);

--Use sub-queries to create derived tables, which can then be used to query specific information. Say you want to know the average salary of the top 5 earners in the company. You will first have to extract a table of the top five salaries as a table. From that table, you can query the average value of the salary. 
SELECT AVG(SALARY) 
FROM (SELECT SALARY 
	  FROM EMPLOYEES 
	  ORDER BY SALARY DESC 
	  LIMIT 5) AS SALARY_TABLE;

--You need to order the data in ascending salary order and limit it to the top five entries, treating this as a derived table. Take the average of these entries.
SELECT AVG(SALARY) 
FROM (SELECT SALARY 
	  FROM EMPLOYEES 
	  ORDER BY SALARY 
	  LIMIT 5) AS SALARY_TABLE;

--Write a query to find the records of employees older than the average age of all employees
SELECT * 
FROM EMPLOYEES 
WHERE YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE))) > 
	(SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE)))) 
	FROM EMPLOYEES);

--From the Job_History table, display the list of Employee IDs, years of service, and average years of service for all entries
SELECT EMPL_ID, YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE))), 
	(SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE)))) 
	FROM JOB_HISTORY)
FROM JOB_HISTORY;

