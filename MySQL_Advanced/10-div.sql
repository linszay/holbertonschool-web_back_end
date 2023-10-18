-- script creates a function SafeDiv that divides & returns
-- the 1st by the 2nd num or returns 0 if 2nd num = 0
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
IF b = 0 THEN
RETURN 0;
END IF;
RETURN a / b;
END;
//
DELIMITER ;
