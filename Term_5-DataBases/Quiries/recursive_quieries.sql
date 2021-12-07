DROP TABLE ParentOf;

CREATE TABLE ParentOf(
    parent VARCHAR(20) NOT NULL,
    child VARCHAR(20) NOT NULL,
);

INSERT INTO ParentOf
    VALUES
        ('Alice', 'Carol'),
        ('Bob', 'Carol'),
        ('Carol', 'Dave'),
        ('Carol', 'George'),
        ('Dave', 'Mary'),
        ('Eve', 'Mary'),
        ('Mary', 'Frank');


WITH Rec(parent, child)
    AS (
        SELECT parent, child
        FROM ParentOf
        WHERE child = 'Mary'
        UNION ALL
        SELECT par.parent, par.child
        FROM ParentOf as par
        JOIN Rec as rec
        ON rec.parent = par.child
        
    )
    
-- Предки Mary
SELECT parent FROM REC;


WITH Rec(parent, child)
    AS (
        SELECT parent, child
        FROM ParentOf
        WHERE parent = 'Carol'
        UNION ALL
        SELECT par.parent, par.child
        FROM ParentOf as par
        JOIN Rec as rec
        ON rec.child = par.parent
    )
    

SELECT * FROM REC;



CREATE TABLE Employee(
    ID INT NOT NULL,
    salary INT NOT NULL
);

CREATE TABLE Manager(
    mID INT NOT NULL,
    eID INT NOT NULL
);

CREATE TABLE Project(
    name VARCHAR(30),
    mgrID INT
);


INSERT INTO Employee
    VALUES
        (123, 100),
        (890, 110),
        (234, 90),
        (345, 80),
        (456, 70),
        (567, 60),
        (111, 200),
        (222, 150),
        (333, 120),
        (098, 15);

INSERT INTO Manager
    VALUES
        (123, 234),
        (111, 222),
        (234, 345),
        (234, 456),
        (345, 567),
        (123, 890),
        (890, 098);


INSERT INTO Project
    VALUES
    	('X', 123),
    	('Y', 234),
    	('Z', 456);


WITH PRemps(ID) AS (SELECT mgrID AS ID FROM Project WHERE name LIKE @Proj
					UNION ALL
					SELECT eID as ID
					FROM Manager M, PRemps X
					WHERE M.mID = X.ID)
SELECT SUM (salary) AS PRojectSalary
FROM Employee
WHERE ID IN (SELECT ID FROM PRemps);







WITH FibbonacciNumbers (RecursionLevel, FibbonacciNumber, NextNumber)
AS (
	SELECT 0 AS RecursionLevel,
		   0 AS FibbonacciNumber,
		   1 AS NextNumber
	UNION ALL
	SELECT a.RecursionLevel + 1 AS RecursionLevel,
		   a.NextNumber AS FibbonacciNumber
		   a.FibbonacciNumber + a.NextNumber AS NextNumber
	FROM FibbonacciNumbers a
	WHERE a.RecursionLevel < 10
)

SELECT 'F' + CAST( fn.RecursionLevel AS VARCHAR) AS FibonacciOrdinal,
	   fn.FibbonacciNumber,
	   fn.NextNumber
FROM FibbonacciNumbers fn
GO


