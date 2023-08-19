ALTER TABLE locations
RENAME COLUMN state_province TO state;

ALTER TABLE locations
ADD CONSTRAINT pk_location_id PRIMARY KEY (location_id);
