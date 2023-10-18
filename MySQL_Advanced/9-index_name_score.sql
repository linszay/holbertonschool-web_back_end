-- script creates an index idx_name_first_score
-- on table names and 1st letter of name and the score
CREATE INDEX idx_name_first_score ON names (name(1), score);
