DROP TABLE IF EXISTS motor;
DROP TABLE IF EXISTS nachricht;
CREATE TABLE motor (
    motor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255)
);

CREATE TABLE nachricht (
    nachricht_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    zeitstempel DOUBLE,
    nachricht VARCHAR(255),
    motor_id INTEGER,
    FOREIGN KEY (motor_id) REFERENCES motor(motor_id));
    

INSERT INTO motor (name) VALUES ('motorix');
