-- creates the MySQL server user user_0d_1 with all privileges
-- The user_0d_1 password will be set
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_id_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
