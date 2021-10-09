create table Users (id SERIAL Primary Key,
					username varchar(80) NOT NULL Unique,
					password varchar(80),
					created_at TIMESTAMPTZ NOT NULL DEFAULT NOW());

create table Tokens (user_id integer REFERENCES Users NOT NULL,
					id varchar(80) Primary Key NOT NULL,
					created_at TIMESTAMPTZ NOT NULL DEFAULT NOW());                