DROP TABLE IF EXISTS motor;
DROP TABLE IF EXISTS topic;
DROP TABLE IF EXISTS nachricht;
CREATE TABLE motor (
    motor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255)
);

CREATE TABLE topic (
    topic_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255)
);

CREATE TABLE nachricht (
    nachricht_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    zeitstempel DOUBLE,
    topic VARCHAR(255),
    nachricht VARCHAR(255),
    motor_id INTEGER,
    FOREIGN KEY (motor_id) REFERENCES motor(motor_id)
);

INSERT INTO topic (name) VALUES ('motors/motorix/control');
INSERT INTO motor (name) VALUES ('motorix');
