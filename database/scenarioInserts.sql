-- airline
INSERT INTO airline (name) VALUES ('JetBlue');

INSERT INTO airline_staff (username, password, first_name, last_name, date_of_birth, airline_name) VALUES ('admin', 'e2fc714c4727ee9395f324cd2e7f331f', 'Roe', 'Jones', '1978-05-25', 'JetBlue');

INSERT INTO staff_phone (phone_number, username) VALUES (11122223333, 'admin');
INSERT INTO staff_phone (phone_number, username) VALUES (44455556666, 'admin');
INSERT INTO staff_email (email, username) VALUES ('staff1@nyu.edu', 'admin');
INSERT INTO staff_email (email, username) VALUES ('staff2@nyu.edu', 'admin');

INSERT INTO airplane (id, airline_name, seats, company, model_number, manufacture_date) VALUES ('1', 'JetBlue', 4, 'B-101', 'Boeing', '2013-05-02');
INSERT INTO airplane (id, airline_name, seats, company, model_number, manufacture_date) VALUES ('2', 'JetBlue', 4, 'A-101', 'Airbus', '2011-05-02');
INSERT INTO airplane (id, airline_name, seats, company, model_number, manufacture_date) VALUES ('3', 'JetBlue', 50, 'B-101', 'Boeing', '2015-05-02');

INSERT INTO maintenance (id, airline_name, maintenance_start, maintenance_end) VALUES (1, 'JetBlue', '2025-01-27', '2025-01-29');
INSERT INTO maintenance (id, airline_name, maintenance_start, maintenance_end) VALUES (2, 'JetBlue', '2025-01-27', '2025-01-29');

INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('JFK', 'JFK', 'NYC', 'USA', 4, 'both');
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('BOS', 'BOS', 'Boston', 'USA', 2, 'both');
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('PVG', 'PVG', 'Shanghai', 'China', 2, 'both');
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('BEI', 'BEI', 'Beijing', 'China', 2, 'both');
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('SFO', 'SFO', 'San Francisco', 'USA', 2, 'both');
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('LAX', 'LAX', 'Los Angeles', 'USA', 2, 'both');
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('HKA', 'HKA', 'Hong Kong', 'China', 2, 'both');
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('SHEN', 'SHEN', 'Shenzhen', 'China', 2, 'both');

INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apartment_number, city, state, zipcode, passport_number, passport_exp, passport_country, date_of_birth) 
VALUES ('testcustomer@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Jon', 'Snow', 1555, 'Jay St', 1,'Brooklyn', 'New York', 11229, 54321, '2025-12-24', 'USA', '1999-12-19');
INSERT INTO customer_phone (phone_number, email) VALUES (12343214321, 'testcustomer@nyu.edu');
INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apartment_number, city, state, zipcode, passport_number, passport_exp, passport_country, date_of_birth) 
VALUES ('user1@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Alice', 'Bob', 5405, 'Jay St', 1, 'Brooklyn', 'New York', 11229, 54322, '2025-12-25', 'USA', '1999-11-19');
INSERT INTO customer_phone (phone_number, email) VALUES (12343224322, 'testcustomer@nyu.edu');
INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apartment_number, city, state, zipcode, passport_number, passport_exp, passport_country, date_of_birth) 
VALUES ('user2@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Cathy', 'Wood', 1702, 'Jay St', 1, 'Brooklyn', 'New York', 11229, 54323, '2025-10-24', 'USA', '1999-10-19');
INSERT INTO customer_phone (phone_number, email) VALUES (12343234323, 'testcustomer@nyu.edu');
INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apartment_number, city, state, zipcode, passport_number, passport_exp, passport_country, date_of_birth) 
VALUES ('user3@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Trudy', 'Jones', 1890, 'Jay St', 1, 'Brooklyn', 'New York', 11229, 54324, '2025-09-24', 'USA', '1999-09-19');
INSERT INTO customer_phone (phone_number, email) VALUES (12343244324, 'testcustomer@nyu.edu');

INSERT INTO flight 
(airline_name, flight_number, departure_date, departure_time, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_code, arrival_code) 
VALUES ('Jet Blue', 'JB111', '2024-12-01', '08:00:00', 'JB111', '11:30:00', '2024-12-01', 300, 'on_time', 'JFK', 'PVG');

