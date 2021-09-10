SET client_encoding = 'UTF8';

CREATE EXTENSION "uuid-ossp";


CREATE TABLE users (
    uuid TEXT PRIMARY KEY DEFAULT uuid_generate_v4(),
    username text NOT NULL,
    password text NOT NULL,
    name text NOT NULL,
    surname text NOT NULL,
    email text NOT NULL,
    is_vaccinated boolean NOT NULL,
    phone text
);


CREATE TABLE facilities (
    id serial PRIMARY KEY,
    name text NOT NULL,
    address text NOT NULL,
    max_capacity integer NOT NULL,
    percentage_capacity_allowed integer NOT NULL
);


CREATE TABLE access_log (
    facility_id integer NOT NULL,
    user_id text NOT NULL,
    type text NOT NULL,
    timestamp timestamp with time zone NOT NULL,
    temperature text NOT NULL,
    CONSTRAINT access_log_pk PRIMARY KEY (facility_id, user_id, type, timestamp),
    CONSTRAINT access_log_fk1 FOREIGN KEY (facility_id) REFERENCES facilities(id) ON DELETE CASCADE,
    CONSTRAINT access_log_fk2 FOREIGN KEY (user_id) REFERENCES users(uuid) ON DELETE CASCADE
);


