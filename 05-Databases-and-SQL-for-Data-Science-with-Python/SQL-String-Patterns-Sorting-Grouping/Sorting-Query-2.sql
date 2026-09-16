SELECT F_NAME, L_NAME, DEP_ID 
FROM EMPLOYEES
ORDER BY DEP_ID DESC, L_NAME DESC;

--Output of the same query in descending order of department ID, and within each department, the records is ordered in descending alphabetical order by last name. For descending order, it uses the DESC clause.