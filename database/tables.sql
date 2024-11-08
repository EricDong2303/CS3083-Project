CREATE TABLE customer(
	email VARCHAR(100),
	password VARCHAR(100) NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	building_number INT NOT NULL,
	street_name VARCHAR(100) NOT NULL,
	apartment_name VARCHAR(100) NOT NULL,
	city VARCHAR(100) NOT NULL,
	state VARCHAR(100) NOT NULL,
	zipcode INT NOT NULL,
	passport_num INT NOT NULL,
	passport_country VARCHAR(100) NOT NULL,
	passport_number INT NOT NULL,
	date_of_birth DATE NOT NULL,
	PRIMARY KEY(email)
);

CREATE TABLE customer_phone(
	phone_number INT,
	email VARCHAR(100),
	PRIMARY KEY(phone_number, email),
	FOREIGN KEY(email) REFERENCES customer(email)
);

CREATE TABLE purchase(
	email VARCHAR(100),
	ticket_id VARCHAR(100),
	PRIMARY KEY(email, ticket_id),
	FOREIGN KEY(email) REFERENCES customer(email),
	FOREIGN KEY(ticket_id) REFERENCES ticket(ticket_id)
);

CREATE TABLE ticket(
	ticket_id VARCHAR(100),
	flight_number INT NOT NULL,
	airline_name VARCHAR(100) NOT NULL,
	departure_date VARCHAR(100) NOT NULL,
	departure_time TIME NOT NULL,
	ticket_price INT NOT NULL,
	card_type VARCHAR(100) NOT NULL,
	card_number INT NOT NULL,
	name_on_card VARCHAR(100) NOT NULL,
	card_exp DATE NOT NULL,
	purchase_date DATE NOT NULL,
	purchase_time TIME NOT NULL,
	PRIMARY KEY(ticket_id),
	FOREIGN KEY(flight_number, airline_name, departure_date, departure_time) REFERENCES flight(flight_number, airline_name, departure_date, departure_time)
);


CREATE TABLE review(
	email VARCHAR(100),
	flight_number INT,
	airline_name VARCHAR(100),
	departure_date VARCHAR(100),
	departure_time TIME,
	rating INT NOT NULL,
	comment VARCHAR(100) NOT NULL,
	PRIMARY KEY(email, flight_number, airline_name, departure_date, departure_time),
	FOREIGN KEY(email) REFERENCES customer(email),
	FOREIGN KEY(flight_number, airline_name, departure_date, departure_time) REFERENCES flight(flight_number, airline_name, departure_date, departure_time)
);

CREATE TABLE flight(
	flight_number INT,
	airline_name VARCHAR(100),
	arrival_code VARCHAR(100) NOT NULL,
	departure_code VARCHAR(100) NOT NULL,
	airplane_id INT NOT NULL,
	departure_date DATE,
	departure_time TIME,
	arrival_date DATE NOT NULL,
	arrival_time TIME NOT NULL,
	base_price INT NOT NULL,
	PRIMARY KEY(flight_number, airline_name, departure_date, departure_time),
	FOREIGN KEY(airline_name) REFERENCES airline(name),
	FOREIGN KEY(arrival_code) REFERENCES airport(code),
	FOREIGN KEY(departure_code) REFERENCES airport(code),
	FOREIGN KEY(airplane_id) REFERENCES airplane(id)
);

CREATE TABLE airline(
  name VARCHAR(100),
  PRIMARY KEY (name)
);

CREATE TABLE airport(
	code VARCHAR(100),
	name VARCHAR(100) NOT NULL,
	city VARCHAR(100) NOT NULL,
	country VARCHAR(100) NOT NULL,
	number_of_terminals INT NOT NULL,
	type VARCHAR(100) NOT NULL check (type in ('domestic', 'international', 'both')),
	PRIMARY KEY(code)
);

CREATE TABLE airplane(
	id VARCHAR(100),
	airline_name VARCHAR(100),
	seats INT NOT NULL,
	company VARCHAR(100) NOT NULL,
	model_number INT NOT NULL,
	manufacture_date DATE NOT NULL,
	PRIMARY KEY(id, airline_name),
	FOREIGN KEY(airline_name) REFERENCES airline(name)
);

CREATE TABLE maintenance(
	id VARCHAR(100),
	airline_name VARCHAR(100),
	maintenance_start DATE,
	maintenance_end DATE,
	PRIMARY KEY(id, airline_name, maintenance_start, maintenance_end),
	FOREIGN KEY(id, airline_name) REFERENCES airplane(id, airline_name)
);

CREATE TABLE airline_staff(
	username VARCHAR(100),
	airline_name VARCHAR(100) NOT NULL,
	password VARCHAR(100) NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	date_of_birth DATE NOT NULL,
	PRIMARY KEY(username),
	FOREIGN KEY(airline_name) REFERENCES airline(name)
);

CREATE TABLE staff_email(
	email VARCHAR(100),
	username VARCHAR(100),
	PRIMARY KEY(email, username),
	FOREIGN KEY(username) REFERENCES airline_staff(username)
);

CREATE TABLE staff_phone(
	phone_number INT,
	username VARCHAR(100),
	PRIMARY KEY(phone_number, username),
	FOREIGN KEY(username) REFERENCES airline_staff(username)
);
