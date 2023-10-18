-- script creates a stored procedure AddBonus
-- it adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus(IN student_id INT,
IN project_name VARCHAR(225), IN score INT) BEGIN
DECLARE project_id INT;
SELECT id INTO project_id
FROM projects WHERE name = project_name;
IF project_id IS NULL THEN
INSERT INTO projects (name) VALUES (project_name);
SET project_id = LAST_INSERT_ID();
END IF;
INSERT INTO corrections (user_id, project_id, score) VALUES
(student_id, project_id, score);
END; 
//
DELIMITER ;
