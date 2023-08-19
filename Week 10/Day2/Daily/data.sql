
CREATE TABLE actors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    age INTEGER
);

INSERT INTO actors (age) VALUES (30);


SELECT COUNT(*) FROM actors;