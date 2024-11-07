--a. One Airline name "Jet Blue".
INSERT INTO airline (airline_name) VALUES ('Jet Blue');

--b. At least Two airports named "JFK" in NYC and "PVG" in Shanghai.
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('JFK', 'John F. Kennedy International Airport', 'New York', 'USA', 6, 'both');

INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('PVG', 'Shanghai Pudong International Airport', 'Shanghai', 'China', 3, 'both');

--c. Insert at least three customers with appropriate names and other attributes
INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apt_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('mike123@gmail.com', 'password123', 'Mike', 'Rafone', 1234, 'Main St', '100', 'New York', 'NY', 10001, 123456789, '2028-12-31', 'USA', '1985-06-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('mike123@gmail.com', '123456789');

INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apt_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('jason1@gmail.com', 'goodpassword', 'Jason', 'Jackson', 1, 'Street St', '200', 'New York', 'NY', 10001, 987654321, '2029-12-31', 'USA', '1988-06-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('jason1@gmail.com', '987654321');

INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apt_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('james3@gmail.com', 'badpassword', 'James', 'Wang', 43, 'Yes St', '300', 'New York', 'NY', 10001, 1111111111, '2026-11-31', 'USA', '1990-07-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('james3@gmail.com', '1111111111');

--d. Insert at least three airplanes.
INSERT INTO airplane (airline_name, id, seats, model_number, manufacture_date, age, maintainance_start, maintainance_end) 
VALUES ('Jet Blue', 'JB111', 150, 'A320', '2015-05-20', 7, '2023-01-01', '2023-01-15');

INSERT INTO airplane (airline_name, id, seats, model_number, manufacture_date, age, maintainance_start, maintainance_end) 
VALUES ('Delta', 'DL126', 180, 'B737', '2018-08-10', 5, '2023-06-01', '2023-06-10');

INSERT INTO airplane (airline_name, id, seats, model_number, manufacture_date, age, maintainance_start, maintainance_end) 
VALUES ('Alaska Airlines', 'AS190', 100, 'E190', '2012-02-25', 11, '2023-03-01', '2023-03-15');

--e. Insert At least One airline Staff working for Jet Blue
INSERT INTO airline_staff (username, staff_password, first_name, last_name, dob, airline_name) 
VALUES ('JaneSmith', 'securepassword', 'Jane', 'Smith', '1985-07-20', 'Jet Blue');

--f. Insert several flights with on-time, and delayed statuses.
INSERT INTO flight 
(airline_name, flight_number, depart_date, depart_time, airplane_name, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_airport, arrival_airport) 
VALUES ('Jet Blue', 'JB111', '2024-12-01', '08:00:00', 'Jet Blue A320', 'JB111', '11:30:00', '2024-12-01', 300, 'on-time', 'JFK', 'LAX');

INSERT INTO flight 
(airline_name, flight_number, depart_date, depart_time, airplane_name, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_airport, arrival_airport) 
VALUES ('Jet Blue', 'JB123', '2024-02-01', '09:00:00', 'Jet Blue A320', 'JB123', '11:30:00', '2024-02-02', 700, 'delayed', 'JFK', 'PVG');

INSERT INTO flight 
(airline_name, flight_number, depart_date, depart_time, airplane_name, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_airport, arrival_airport) 
VALUES ('Delta', 'DL123', '2024-03-01', '10:00:00', 'Delta 757', 'DL123', '01:30:00', '2024-03-02', 1000, 'delayed', 'BOS', 'PKX');

INSERT INTO flight 
(airline_name, flight_number, depart_date, depart_time, airplane_name, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_airport, arrival_airport) 
VALUES ('American Airlines', 'AA122', '2024-04-01', '10:00:00', 'AA 737 MAX', 'AA122', '01:30:00', '2024-04-02', 100, 'on-time', 'LGA', 'ORD');

--g. Insert some tickets for corresponding flights and insert some purchase records (customers bought sometickets).
INSERT INTO ticket
(ticket_id, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, airline_name, flight_number, depart_date, depart_time) 
VALUES ('T1', 300, 'VISA', '4111111111111111', 'Jackson Doe', '2025-08-31', '2024-11-01', '2024-11-01 09:30:00', 'Jet Blue', 'JB111', '2024-12-01', '08:00:00');

INSERT INTO ticket
(ticket_id, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, airline_name, flight_number, depart_date, depart_time) 
VALUES ('T2', 700, 'MASTERCARD', '5500000000000004', 'Eric Smith', '2026-09-15', '2024-11-02', '2024-11-02 10:00:00', 'Delta', 'DL102', '2024-12-02', '14:00:00');

INSERT INTO purchases (email, ticket_id)
VALUES ('ed2303@nyu.edu', 'T1');

INSERT INTO purchases (email, ticket_id)
VALUES ('Janesmith@gmail.com', 'T2');
