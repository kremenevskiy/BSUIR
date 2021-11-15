USE Northwind;
GO


-- Построить запрос, формирующий вывод всех данных обо всех регионах (Region)
SELECT * 
FROM Region;


-- Построить запрос, формирующий вывод названия, адреса, города первых 5 поставщиков, отсортированные в алфавитном порядке по названию.
SELECT TOP 5 
    CompanyName,
    Address,
    City
FROM Suppliers
ORDER BY CompanyName;


-- Вывести все данные о сотруднике Robert King
SELECT *
FROM Employees
WHERE 
    FirstName = 'Robert' AND
    LastName = 'King';


-- Вывести цены всех товаров, продажа которых прекращена (discontinued)
SELECT 
    UnitPrice
FROM Products
WHERE 
    Discontinued = 1;


-- Сформировать список (содержащий наименование, отпускную цену, остаток) товаров на складе, остатки которых более 100 единиц.
SELECT ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock > 100;


-- Вывести список всех сотрудников с днями рождения в октябре
SELECT LastName, FirstName, BirthDate
FROM Employees
WHERE MONTH(BirthDate) = 10;


-- Определить, кто из сотрудников имеет степень Ph.D. (образование указано в столбце Notes)
SELECT EmployeeID, LastName, FirstName, Notes
FROM Employees
WHERE Notes LIKE '%Ph.D%';


-- Построить запрос, формирующий табличный вывод: фамилию сотрудника и указание старше он/она 60 лет или нет
SELECT LastName,
    CASE
        WHEN YEAR(GETDATE()) - YEAR(BirthDate) > 60 THEN 1
        ELSE 0 END
    as 'age > 60'
FROM Employees;


--  Сформировать список (содержащий наименование, цену, остаток) товаров категории Beverages на складе, остатки которых более 100 единиц.
SELECT ProductName, UnitPrice, UnitsInStock
FROM Products as P
WHERE CategoryID = (
    SELECT CategoryID
    FROM Categories
    WHERE CategoryName = 'Beverages');


-- Вывести общую стоимость всех заказов, которые оформил сотрудник фирмы “Steven Buchanan»  в июле 1996 г., с указанием кода заказа, даты заказа и общей суммы.
SELECT 
    OD.OrderId,
    SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as OrderPrice,
    O.OrderDate
FROM [Order Details] as OD
    JOIN Orders as O
    ON OD.OrderID = O.OrderID
WHERE 
    O.EmployeeID = (
        SELECT EmployeeID
        FROM Employees 
        WHERE LastName = 'Buchanan' AND FirstName = 'Steven') AND
    MONTH(OrderDate) = 7 AND
    YEAR(OrderDate) = 1996
GROUP BY OD.OrderID, O.OrderDate


-- Вывести номера и даты заказов с товарами категории “Seafood”.
SELECT OrderID, OrderDate
FROM Orders
WHERE 
    OrderID IN (
        SELECT OrderId
        FROM [Order Details]
        WHERE ProductID IN (
            SELECT ProductID
            FROM Products
            WHERE CategoryID = (
                SELECT CategoryID
                FROM Categories
                WHERE CategoryName = 'Seafood'))
                );


-- Вывести все товары, отправленные в 1997 году в Канаду (неповторяющиеся значения)
SELECT *
FROM Products
WHERE ProductId IN (
    SELECT ProductId
    FROM [Order Details]
    WHERE OrderID IN (
        SELECT OrderID
        FROM Orders
        WHERE 
            ShipCountry = 'Canada' AND
            YEAR(ShippedDate) = 1997));


-- Вывести все товары, отправленные в 1997 году в Канаду (неповторяющиеся значения) посредством Speedy Express.
SELECT *
FROM Products
WHERE ProductId IN (
    SELECT ProductId
    FROM [Order Details]
    WHERE OrderID IN (
        SELECT OrderID
        FROM Orders
        WHERE
            ShipCountry = 'Canada' AND
            YEAR(ShippedDate) = 1997 AND
            ShipVia = (
                SELECT ShipperId
                FROM Shippers
                WHERE CompanyName = 'Speedy Express')));


-- Определить количество заказов в базе данных.
SELECT COUNT(OrderId) as 'Count of orders'
FROM Orders;


-- Выполнить расчет позиций и общую стоимость товаров, входящих в заказы, отправленные 21 октября 1997 года
SELECT 
    P.ProductID,
    SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as TotalPrice,
    SUM(OD.Quantity) as TotalItems
FROM [Order Details] as OD
JOIN Products as P
ON P.ProductID = OD.ProductID
WHERE OrderId in (
    SELECT OrderId
    FROM Orders
    WHERE 
        YEAR(OrderDate) = 1997 AND
        MONTH(OrderDate) = 10 AND
        DAY(OrderDate) = 21)
GROUP BY(P.ProductId);


-- Выполнить расчет количества поставленного на склад товара с кодом 4 менеджером поставщика с кодом 3.
SELECT COUNT(UnitsInStock) as Quintity
FROM Products
WHERE ProductID = 4 AND SupplierID = 3;


-- Выполнить расчет общей стоимости поставленной продукции в феврале 1998 года 
SELECT 
    SUM(OD.UnitPrice * OD.Quantity * (1-OD.Discount)) as TotalPrice_1998_02
FROM [Order Details] as OD
    JOIN Products as P
    ON P.ProductID = OD.ProductID
WHERE 
    OD.OrderID in (
        SELECT OrderID
        FROM Orders
        WHERE
            YEAR(OrderDate) = 1998 AND
            MONTH(OrderDate) = 2
        )


-- Получить количество типов товаров, продажи которых не прекращены
SELECT COUNT(ProductId)
FROM Products
WHERE Discontinued = 0;


-- Выполнить расчет количества заказов, которые обслуживали сотрудники фирмы в 1997-1998 гг. с указанием года, сотрудника и количества заказов.
SELECT
    Employees.LastName as Employee_Surname,
    YEAR(OrderDate) as Year,
    COUNT(OrderID) as total_orders
FROM Orders
    JOIN Employees
    ON Employees.EmployeeID = Orders.EmployeeID
WHERE
    YEAR(OrderDate) BETWEEN 1997 AND 1998
GROUP BY YEAR(OrderDate), Employees.LastName


-- Вывести наименования категорий товаров на складе, остатки по которым меньше 100, с указанием категории и суммы остатка
SELECT 
    C.CategoryName as Category_name,
    SUM(P.UnitsInStock) as Products_in_stock
FROM Products as P
    JOIN Categories as C
    ON P.CategoryID = C.CategoryID
GROUP BY CategoryName
HAVING SUM(P.UnitsInStock) < 100;




-- Вывести список сотрудников, общая сумма заказов которых составила в 1996 г. 5000 и более денежных единиц
SELECT 
    Emp.LastName,
    Emp.FirstName,
    SUM(OD.Quantity * OD.UnitPrice * (1 - OD.Discount)) as money
FROM [Order Details] AS OD
    JOIN Orders as O
    ON OD.OrderID = O.OrderID
    JOIN Employees as Emp
    ON O.EmployeeID = Emp.EmployeeID
    JOIN Products as P
    ON P.ProductID = OD.ProductID
WHERE YEAR(O.OrderDate) = 1996
GROUP BY EMp.LastName,  Emp.FirstName
HAVING SUM(OD.Quantity * OD.UnitPrice * (1 - OD.Discount)) > 5000;


-- Вывести стоимость заказов, отправленных в 1997 году, в разрезе стран.
SELECT 
    O.ShipCountry,
    SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount))
FROM Orders as O
JOIN [Order Details] as OD
ON O.OrderID = OD.OrderID
WHERE YEAR(O.OrderDate) = 1997
GROUP BY O.ShipCountry;


-- Чтобы использовать PIVOT
ALTER DATABASE Northwind   
SET COMPATIBILITY_LEVEL = 100;


-- Вывести стоимость заказов, отправленных в 1997 году, в разрезе стран, страны указаны в колонках итоговой таблицы.
SELECT *
FROM (
    SELECT
        O.ShipCountry as country,
        OD.UnitPrice * OD.Quantity * (1- OD.Discount) as total
    FROM Orders as O
    JOIN [Order Details] as OD
    ON O.OrderID = OD.OrderID
    WHERE YEAR(O.OrderDate) = 1997
) look
PIVOT(
    SUM(total)
    FOR country in (Argentina, USA, France, Finland, Italy, Brazil, Germany, Switzerland)
) as pivot_table;


-- Вывести стоимость сделанных заказов помесячно с подведением промежуточных ежегодных итогов и общий итог.
SELECT 
    YEAR(O.OrderDate) as year,
    MONTH(O.OrderDate) as month,
    SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as TotalInMonth,
    SUM(SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount))) 
        OVER(partition by YEAR(O.OrderDate) ORDER BY MONTH(O.OrderDate)) as TotalYearIncome
FROM [Order Details] as OD
    JOIN Orders as O
    ON O.OrderID = OD.OrderID
GROUP BY YEAR(O.OrderDate), MONTH(O.OrderDate)


-- Вывести стоимость всех заказов заказчика HILARION-Abastos в 1997 году помесячно.
SELECT 
    MONTH(O.OrderDate) as month,
    SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as TotalPrice
FROM [Order Details] as OD
    JOIN Orders as O
    ON OD.OrderID = O.OrderID
WHERE O.CustomerID = (
    SELECT CustomerId
    FROM Customers
    WHERE CompanyName = 'HILARION-Abastos'
    ) 
    AND YEAR(O.OrderDate) = 1997
GROUP BY MONTH(O.OrderDate);


-- Вывести наименование товаров, остатки на складе которых от 5 до 10 и от 25 и более
SELECT 
    ProductName,
    UnitsInStock
FROM Products
WHERE (UnitsInStock BETWEEN 5 AND 10) OR (UnitsInStock > 25);


-- Вывести заказы, в которые включены более 2-х товаров
SELECT 
    OD.OrderID,
    COUNT(OD.OrderID) as TypesProductsInOrder
FROM [Order Details] as OD
GROUP BY OD.OrderID
HAVING COUNT(OD.OrderID) > 2


--  Определить города, в которые направлены более 3 заказов
SELECT 
    ShipCity as city,
    COUNT(OrderID) as CountOrders
FROM Orders 
GROUP BY ShipCity
HAVING COUNT(OrderID) > 3;



-- Построить запрос для определения изменения средней стоимости заказа в ноябре 1997 г по сравнению с ноябрём 1996 г.
DECLARE @AVERAGE_NOV_1997 INT
DECLARE @AVERAGE_NOV_1996 INT


SET @AVERAGE_NOV_1997 = (
    SELECT AVG(a.Price)
    FROM (
        SELECT OD.OrderID,
        SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as Price
        FROM [Order Details] as OD
            JOIN Orders as O
            ON O.OrderID = OD.OrderID
        WHERE 
            YEAR(O.OrderDate) = 1997 AND
            MONTH(O.OrderDate) = 11
        GROUP BY OD.OrderID) a)


SET @AVERAGE_NOV_1996 = (
    SELECT AVG(a.Price)
    FROM (
        SELECT OD.OrderID,
        SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as Price
        FROM [Order Details] as OD
            JOIN Orders as O
            ON O.OrderID = OD.OrderID
        WHERE 
            YEAR(O.OrderDate) = 1996 AND
            MONTH(O.OrderDate) = 11
        GROUP BY OD.OrderID) a)


SELECT
    @AVERAGE_NOV_1997 as average_1997_november,
    @AVERAGE_NOV_1996 as average_1996_november,
    ABS(@AVERAGE_NOV_1997-@AVERAGE_NOV_1996) as difference



-- Построить запрос для определения среднего и медианного значений стоимости заказов в 1997 году
DECLARE @AVERAGE_1997 INT;
DECLARE @MEDIAN_1997 INT;
DECLARE @count_orders INT;


SET @AVERAGE_1997 = (
    SELECT AVG(a.Price)
    FROM (
        SELECT
            OD.OrderID,
            SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as Price
        FROM [Order Details] as OD
            JOIN Orders as O
            ON O.OrderID = OD.OrderID
        WHERE YEAR(O.OrderDate) = 1997
        GROUP BY OD.OrderID) a);


SET @count_orders = (
    SELECT COUNT(*)
    FROM Orders
    WHERE YEAR(OrderDate) = 1997);


SET @MEDIAN_1997 = (
    SELECT 
        outted.Price
    FROM (
        SELECT  
            nested.OrderID,
            nested.Price,
            ROW_NUMBER() OVER(ORDER BY nested.OrderID) as R
        FROM (
            SELECT 
                OD.OrderID,
                SUM(OD.UnitPrice * OD.Quantity * (1 - OD.Discount)) as Price
            FROM [Order Details] as OD
                JOIN Orders as O
                ON O.OrderID = OD.OrderID
            WHERE YEAR(O.OrderDate) = 1997
            GROUP BY OD.OrderID) nested) outted 
    WHERE R = (@count_orders + 1) / 2
)

SELECT @AVERAGE_1997 as average, @MEDIAN_1997 as median;
SELECT (@count_orders + 1) / 2 as midian_position