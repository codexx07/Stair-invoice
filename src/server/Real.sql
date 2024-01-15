USE my_database;
CREATE TABLE IF NOT EXISTS msme(reg_Number VARCHAR(255), Company_Name VARCHAR(255));

INSERT INTO msme(reg_Number, Company_Name) VALUES('12345678', 'ABC');

SELECT * FROM msme;


