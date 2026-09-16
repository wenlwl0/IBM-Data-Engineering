SELECT SUM(COST) FROM PETRESCUE;
--calculates the total cost of all animal rescues in the PETRESCUE table

SELECT SUM(COST) AS SUM_OF_COST FROM PETRESCUE;
--assign a label to the query SUM_OF_COST

SELECT MAX(QUANTITY) FROM PETRESCUE;
--output of this query will be the maximum value of all elements in the column

SELECT MIN(QUANTITY) FROM PETRESCUE;
--query can easily be changed to display the minimum quantity using the MIN function instead

SELECT AVG(COST) FROM PETRESCUE;
--query that displays the average cost of animals rescued

