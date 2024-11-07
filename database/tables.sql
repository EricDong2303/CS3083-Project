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

CREATE TABLE purchases(
	email VARCHAR(100),
	ticket_id VARCHAR(100),
	PRIMARY KEY(email, ticket_id),
	FOREIGN KEY(email) REFERENCES customer(email),
	FOREIGN KEY(ticket_id) REFERENCES ticket(ticket_id)
);

CREATE TABLE ticket(
	ticket_id VARCHAR(100),
	flight_number INT,
	arrival_code VARCHAR(100),
	departure_code VARCHAR(100),
	ticket_price INT NOT NULL,
	card_type VARCHAR(100) NOT NULL,
	card_number INT NOT NULL,
	name_on_card VARCHAR(100) NOT NULL,
	purchase_date DATE NOT NULL,
	purchase_time TIME NOT NULL,
	PRIMARY KEY(ticket_id, flight_number, arrival_code, departure_code),
	FOREIGN KEY(flight_number, arrival_code, departure_code) REFERENCES flight(flight_number, arrival_code, departure_code)
);

CREATE TABLE ticket(
	ticket_id VARCHAR(100) not null,
	ticket_price int not null,
	card_type VARCHAR(100) not null,
	card_number VARCHAR(100) not null,
	name_on_card VARCHAR(100) not null,
	card_exp date not null,
	purchase_date date not null,
	purchase_time datetime not null,
	airline_name VARCHAR(100) not null,
	flight_number VARCHAR(100) not null,
	depart_date date not null,
	depart_time time not null,
	primary key(ticket_id),
	FOREIGN KEY(flight_number, airline_name, depart_date, depart_time) REFERENCES Flight(flight_number, airline_name, depart_date, depart_time)
);

CREATE TABLE airline(
  airline_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (airline_name)
);

CREATE TABLE airport(
  code CHAR(3) NOT NULL,
  name VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  number_of_terminals INT NOT NULL,
  type VARCHAR(100) NOT NULL check (type in ('domestic', 'international', 'both')),
  PRIMARY KEY (code)
);

CREATE TABLE airplane(
  airline_name VARCHAR(100) NOT NULL,
  id VARCHAR(100) NOT NULL,
  seats INT NOT NULL,
  model_number VARCHAR(100) NOT NULL,
  manufacture_date DATE NOT NULL,
  age INT NOT NULL,
  maintainance_start DATE NOT NULL,
  maintainance_end DATE NOT NULL,
  FOREIGN KEY(airline_name) REFERENCES Airline(airline_name),
  PRIMARY KEY (airline_name)
);

CREATE TABLE flight(
    flight_name VARCHAR(100) NOT NULL,
    flight_number VARCHAR(100) NOT NULL,
    depart_date DATE NOT NULL,
    depart_time TIME NOT NULL,
    airplane_name VARCHAR(100) NOT NULL,
    airplane_id VARCHAR(100) NOT NULL,
    arrival_time TIME NOT NULL,
    arrival_date DATE NOT NULL,
    base_price INT NOT NULL,
    flight_status VARCHAR(100) NOT NULL CHECK (flight_status IN ('on-time', 'delayed')),
    departure_airport VARCHAR(100) NOT NULL,
    arrival_airport VARCHAR(100) NOT NULL,
    PRIMARY KEY(flight_number, airplane_name, depart_date, depart_time),
    FOREIGN KEY(airplane_name) REFERENCES Airplane(airplane_name),
    FOREIGN KEY(airplane_id) REFERENCES Airplane(airplane_id),
    FOREIGN KEY(departure_airport) REFERENCES Airport(code),
    FOREIGN KEY(arrival_airport) REFERENCES Airport(code)
);

CREATE TABLE review(
    email VARCHAR(100) NOT NULL,
    airline_name VARCHAR(50) NOT NULL,
    flight_number VARCHAR(50) NOT NULL, 
    depart_date DATE NOT NULL,
    depart_time TIME NOT NULL,
    rate INT NOT NULL CHECK (rate IN (1,2,3,4,5)),
    comment VARCHAR(200) NOT NULL,
    PRIMARY KEY (email, airline_name, flight_number, depart_date, depart_time),
    FOREIGN KEY (email) REFERENCES Customer(email),
    FOREIGN KEY (flight_number, airline_name, depart_date, depart_time) REFERENCES Flight(flight_number, airline_name, depart_date, depart_time)
);

CREATE TABLE airline_staff(
    username VARCHAR(100) not null,
    staff_password VARCHAR(100) not null,
    first_name VARCHAR(100) not null,
    last_name VARCHAR(100) not null,
    dob date not null,
    airline_name VARCHAR(100) not null,
    primary key(username),
    FOREIGN KEY(airline_name) REFERENCES Airline(airline_name)
);

CREATE TABLE staff_phone(
    username VARCHAR(100) not null,
    phone_number int not null,
    primary key(username, phone_number),
    FOREIGN KEY(username) REFERENCES Airline_Staff(username)
);

CREATE TABLE staff_email(
    username VARCHAR(100) not null,
    email VARCHAR(100) not null,
    primary key(username, email),
    FOREIGN KEY(username) REFERENCES airline_staff(username)
);

