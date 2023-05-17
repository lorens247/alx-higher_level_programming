-- A script that creates a table called first_table in the current database in your MySQL server.
-- first_table description: id INT, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS first_table (
    id INT, -- Define the id column of type INT
    name VARCHAR(256) -- Define the name column of type VARCHAR with length 256
);
