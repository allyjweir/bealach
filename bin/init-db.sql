DROP DATABASE IF EXISTS bealach;

CREATE DATABASE bealach;

\connect bealach;

CREATE TABLE regions (
    id      serial         PRIMARY KEY,
    name    varchar(128)    NOT NULL
);

CREATE TABLE points (
    id          serial          PRIMARY KEY,
    region_id   integer         NOT NULL,
    name        varchar(128)    NOT NULL,
    lat         varchar(64)     NOT NULL,
    lon         varchar(64)     NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions(id)
);