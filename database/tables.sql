CREATE TABLE `database_project`.`customer` (
  email VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  building_number INT NOT NULL,
  street_name VARCHAR(100) NOT NULL,
  apt_number VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zipcode INT NOT NULL,
  passport_number INT NOT NULL,
  passport_exp DATE NOT NULL,
  passport_country VARCHAR(100) NOT NULL,
  dob DATE NOT NULL,
  PRIMARY KEY (email)
);

CREATE TABLE `database_project`.`customer_phone` (
	email VARCHAR(100) NOT NULL,
	phone_number INT NOT NULL,
	PRIMARY KEY (email, phone_number)
	foreign key(email) references customer(email)
);

CREATE TABLE `database_project`.`purchases`(
    email varchar(100) not null,
    ticket_id varchar(100) not null,
    primary key(email, ticket_id),
    foreign key(email) references customer(email),
    foreign key(ticket_id) references ticket(ticket_id)
);

CREATE TABLE `database_project`.`ticket` (
	ticket_id varchar(100) not null,
	ticket_price int not null,
	card_type varchar(100) not null,
	card_number varchar(100) not null,
	name_on_card varchar(100) not null,
	card_exp date not null,
	purchase_date date not null,
	purchase_time datetime not null,
	airline_name varchar(100) not null,
	flight_number varchar(100) not null,
	depart_date date not null,
	depart_time time not null,
	primary key(ticket_id),
	foreign key(flight_number, airline_name, depart_date, depart_time) references Flight(flight_number, airline_name, depart_date, depart_time)
);

CREATE TABLE `database_project`.`airline` (
  airline_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (airline_name)
);

CREATE TABLE `database_project`.`airport` (
  code CHAR(3) NOT NULL,
  name VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  number_of_terminals INT NOT NULL,
  type VARCHAR(100) NOT NULL check (type in ('domestic', 'international', 'both')),
  PRIMARY KEY (code)
);

CREATE TABLE `database_project`.`airplane` (
  airplane_name VARCHAR(100) NOT NULL,
  id VARCHAR(100) NOT NULL,
  seats INT NOT NULL,
  model_number VARCHAR(100) NOT NULL,
  manufacture_date DATE NOT NULL,
  age INT NOT NULL,
  maintainance_start DATE NOT NULL,
  maintainance_end DATE NOT NULL,
  foreign key(airline_name) references Airline(airline_name),
  PRIMARY KEY (airline_name)
);

CREATE TABLE `database_project`.`flight` (
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

CREATE TABLE `database_project`.`review` (
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
