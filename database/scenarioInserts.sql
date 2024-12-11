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
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 102, 'SFO', '2024-09-20', '13:25:25', 'LAX', '2024-09-20', '16:50:25', 300, 'on_time', 3);


INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 104, 'PVG', '2024-10-04', '13:25:25', 'BEI', '2024-10-04', '16:50:25', 300, 'on_time', 3);


INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 106, 'SFO', '2024-08-04', '13:25:25', 'LAX', '2024-08-04', '16:50:25', 350, 'delayed', 3);


INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 206, 'SFO', '2025-02-04', '13:25:25', 'LAX', '2025-02-04', '16:50:25', 300, 'on_time', 2);


INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 207, 'LAX', '2025-03-04', '13:25:25', 'SFO', '2025-03-04', '16:50:25', 300, 'on_time', 2);


INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 134, 'JFK', '2023-12-15', '13:25:25', 'BOS', '2023-12-15', '16:50:25', 300, 'delayed', 3);


INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 296, 'PVG', '2024-12-30', '13:25:25', 'SFO', '2024-12-30', '16:50:25', 3000, 'on_time', 1);

INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 715, 'PVG', '2024-09-28', '13:25:25', 'BEI', '2024-09-28', '16:50:25', 500, 'delayed', 1);

INSERT INTO flight 
(airline_name, flight_number, departure_code, departure_date, departure_time, arrival_code, arrival_date, arrival_time, base_price, flight_status, airplane_id) 
VALUES ('JetBlue', 839, 'SHEN', '2023-12-26', '13:25:25', 'BEI', '2023-12-26', '16:50:25', 300, 'on_time', 3);

--tickets

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('1', 'JetBlue', 102, '2024-09-20', '13:25:25', 300, 'credit', 1111222233334444, 'Jon Snow', '2025-03-01', '2024-08-17', '11:15:55', 'Jon', 'Snow', '1999-11-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('2', 'JetBlue', 102, '2024-09-20', '13:25:25', 300, 'credit', 1111222233335555, 'Alice Bob', '2025-03-01', '2024-08-16', '11:55:55', 'Alice', 'Bob', '1999-11-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('3', 'JetBlue', 102, '2024-09-20', '13:25:25', 300, 'credit', 1111222233335555, 'Cathy Wood', '2025-03-01', '2024-09-14', '11:55:55', 'Cathy', 'Wood', '1999-10-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('4', 'JetBlue', 104, '2024-10-04', '13:25:25', 300, 'credit', 1111222233335555, 'Alice Bob', '2024-03-01', '2024-08-21', '11:55:55', 'Alice', 'Bob', '1999-11-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('5', 'JetBlue', 104, '2024-10-04', '13:25:25', 300, 'credit', 1111222233334444, 'Jon Snow', '2024-03-01', '2024-09-28', '11:55:55', 'Jon', 'Snow', '1999-12-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('6', 'JetBlue', 106, '2024-08-04', '13:25:25', 350, 'credit', 1111222233334444, 'Jon Snow', '2024-03-01', '2024-08-02', '11:55:55', 'Jon', 'Snow', '1999-12-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('7', 'JetBlue', 106, '2024-08-04', '13:25:25', 350, 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01', '2024-07-23', '11:55:55', 'Trudy', 'Jones', '1999-09-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('8', 'JetBlue', 839, '2023-12-26', '13:25:25', 300, 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01', '2023-12-23', '11:55:55', 'Trudy', 'Jones', '1999-09-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('9', 'JetBlue', 102, '2024-09-20', '13:25:25', 300, 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01', '2024-07-14', '11:55:55', 'Trudy', 'Jones', '1999-09-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('11', 'JetBlue', 134, '2023-12-15', '13:25:25', 300, 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01', '2024-10-23', '11:55:55', 'Trudy', 'Jones', '1999-09-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('12', 'JetBlue', 715, '2024-09-28', '13:25:25', 500, 'credit', 1111222233334444, 'Jon Snow', '2024-03-01', '2024-05-02', '11:55:55', 'Jon', 'Snow', '1999-12-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('14', 'JetBlue', 206, '2025-02-04', '13:25:25', 400, 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01', '2024-11-20', '11:55:55', 'Trudy', 'Jones', '1999-09-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('15', 'JetBlue', 206, '2025-02-04', '13:25:25', 400, 'credit', 1111222233335555, 'Alice Bob', '2024-03-01', '2024-11-21', '11:55:55', 'Alice', 'Bob', '1999-11-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('16', 'JetBlue', 206, '2025-02-04', '13:25:25', 400, 'credit', 1111222233335555, 'Cathy Wood', '2024-03-01', '2024-09-19', '11:55:55', 'Cathy', 'Wood', '1999-10-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('17', 'JetBlue', 207, '2025-03-04', '13:25:25', 300, 'credit', 1111222233335555, 'Alice Bob', '2024-03-01', '2024-08-15', '11:55:55', 'Alice', 'Bob', '1999-11-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('18', 'JetBlue', 207, '2025-03-04', '13:25:25', 300, 'credit', 1111222233334444, 'Jon Snow', '2024-03-01', '2024-09-25', '11:55:55', 'Jon', 'Snow', '1999-12-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('19', 'JetBlue', 296, '2024-12-30', '13:25:25', 3000, 'credit', 1111222233334444, 'Alice Bob', '2024-03-01', '2024-11-22', '11:55:55', 'Alice', 'Bob', '1999-11-19');

INSERT INTO ticket
(ticket_id, airline_name, flight_number, departure_date, departure_time, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, first_name, last_name, dob)
VALUES ('20', 'JetBlue', 296, '2024-12-30', '13:25:25', 3000, 'credit', 1111222233334444, 'Jon Snow', '2024-03-01', '2023-12-17', '11:55:55', 'Jon', 'Snow', '1999-12-19');


-- purchase

INSERT INTO purchase (email, ticket_id)
VALUES ('testcustomer@nyu.edu', '1');
INSERT INTO purchase (email, ticket_id)
VALUES ('user1@nyu.edu', '2');
INSERT INTO purchase (email, ticket_id)
VALUES ('user2@nyu.edu', '3');
INSERT INTO purchase (email, ticket_id)
VALUES ('user1@nyu.edu', '4');
INSERT INTO purchase (email, ticket_id)
VALUES ('testcustomer@nyu.edu', '5');
INSERT INTO purchase (email, ticket_id)
VALUES ('testcustomer@nyu.edu', '6');
INSERT INTO purchase (email, ticket_id)
VALUES ('user3@nyu.edu', '7');
INSERT INTO purchase (email, ticket_id)
VALUES ('user3@nyu.edu', '8');
INSERT INTO purchase (email, ticket_id)
VALUES ('user3@nyu.edu', '9');
INSERT INTO purchase (email, ticket_id)
VALUES ('user3@nyu.edu', '11');
INSERT INTO purchase (email, ticket_id)
VALUES ('testcustomer@nyu.edu', '12');
INSERT INTO purchase (email, ticket_id)
VALUES ('user3@nyu.edu', '14');
INSERT INTO purchase (email, ticket_id)
VALUES ('user1@nyu.edu', '15');
INSERT INTO purchase (email, ticket_id)
VALUES ('user2@nyu.edu', '16');
INSERT INTO purchase (email, ticket_id)
VALUES ('user1@nyu.edu', '17');
INSERT INTO purchase (email, ticket_id)
VALUES ('testcustomer@nyu.edu', '18');
INSERT INTO purchase (email, ticket_id)
VALUES ('user1@nyu.edu', '19');
INSERT INTO purchase (email, ticket_id)
VALUES ('testcustomer@nyu.edu', '20');

INSERT INTO review (email, flight_number, airline_name, departure_date, departure_time, rating, comment)
VALUES ('testcustomer@nyu.edu', 102, 'JetBlue', '2024-09-20', '13:25:25', 4, 'Very Comfortable');
INSERT INTO review (email, flight_number, airline_name, departure_date, departure_time, rating, comment)
VALUES ('user1@nyu.edu', 102, 'JetBlue', '2024-09-20', '13:25:25', 5, 'Relaxing, check-in and onboarding very professional');
INSERT INTO review (email, flight_number, airline_name, departure_date, departure_time, rating, comment)
VALUES ('user2@nyu.edu', 102, 'JetBlue', '2024-09-20', '13:25:25', 3, 'Satisfied and will use the same flight again');
INSERT INTO review (email, flight_number, airline_name, departure_date, departure_time, rating, comment)
VALUES ('testcustomer@nyu.edu', 104, 'JetBlue', '2024-10-04', '13:25:25', 1, 'Customer care services are not good');
INSERT INTO review (email, flight_number, airline_name, departure_date, departure_time, rating, comment)
VALUES ('user1@nyu.edu', 104, 'JetBlue', '2024-10-04', '13:25:25', 5, 'Comfortable journey and professional');
