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

