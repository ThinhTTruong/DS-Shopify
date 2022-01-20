-- Answer for part a
SELECT COUNT(*) 
FROM Orders
WHERE ShipperID = 1;

-- Answer for part b
SELECT LastName 
FROM Employees 
WHERE EmployeeID = (
    SELECT TOP 1 EmployeeID 
    FROM Orders 
    GROUP BY EmployeeID 
    ORDER BY COUNT(EmployeeID) DESC);
    
-- Answer for part c
SELECT TOP 1 ProductID 
FROM OrderDetails 
WHERE OrderID IN 
	(SELECT OrderID 
    FROM Orders 
    WHERE CustomerID IN 
    	(SELECT CustomerID 
        FROM Customers 
        WHERE Country="Germany")
	) 
GROUP BY ProductID 
ORDER BY COUNT(ProductID) DESC;