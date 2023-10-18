-- script creates a stored procedure AddBonus
-- it adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus(IN student_id INT,
IN project_name VARCHAR(100), IN score INT) BEGIN
DECLARE project_id INT;
SET project_id = (SELECT id FROM projects WHERE name = project_name);
INSERT INTO corrections (user_id, project_id, score) VALUES
(student_id, project_id, score);
END; 
//
DELIMITER ;
