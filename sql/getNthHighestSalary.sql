CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    DECLARE @offset  INT ;  
    SET @offset = @N - 1;
    RETURN (
        /* Write your T-SQL query statement below. */
      Select Salary
      FROM Employee
      ORDER BY Salary ASC
      OFFSET  @offset ROWS
    FETCH NEXT 1 ROWS ONLY
    );
END