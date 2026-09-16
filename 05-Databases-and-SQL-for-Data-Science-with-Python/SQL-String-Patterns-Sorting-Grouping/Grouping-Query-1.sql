SELECT DEP_ID, COUNT(*)
FROM EMPLOYEES
GROUP BY DEP_ID;

--For each department ID we wish to retrieve the number of employees in the department.