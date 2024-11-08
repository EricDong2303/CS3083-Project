-- a. One Airline name "Jet Blue".
INSERT INTO airline (name) VALUES ('Jet Blue');

-- b. At least Two airports named "JFK" in NYC and "PVG" in Shanghai.
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('JFK', 'John F. Kennedy International Airport', 'New York', 'USA', 6, 'both');

INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('PVG', 'Shanghai Pudong International Airport', 'Shanghai', 'China', 3, 'both');

-- c. Insert at least three customers with appropriate names and other attributes
INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apartment_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('mike123@gmail.com', 'password123', 'Mike', 'Rafone', 1234, 'Main St', '100', 'New York', 'NY', 10001, 123456789, '2028-12-31', 'USA', '1985-06-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('mike123@gmail.com', '123456789');

INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apartment_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('jason1@gmail.com', 'goodpassword', 'Jason', 'Jackson', 1, 'Street St', '200', 'New York', 'NY', 10001, 987654321, '2029-12-31', 'USA', '1988-06-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('jason1@gmail.com', '987654321');

INSERT INTO customer 
(email, password, first_name, last_name, building_number, street_name, apartment_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('james3@gmail.com', 'badpassword', 'James', 'Wang', 43, 'Yes St', '300', 'New York', 'NY', 10001, 1111111111, '2026-11-30', 'USA', '1990-07-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('james3@gmail.com', '1111111111');

-- d. Insert at least three airplanes.
INSERT INTO airplane (airline_name, id, company, seats, model_number, manufacture_date) 
VALUES ('Jet Blue', 'JB111', 'Airbus', 150, '320', '2015-05-20');

INSERT INTO airplane (airline_name, id, company, seats, model_number, manufacture_date) 
VALUES ('Jet Blue', 'DL126', 'Lockheed Martin', 180, '737', '2018-08-10');

INSERT INTO airplane (airline_name, id, company, seats, model_number, manufacture_date) 
VALUES ('Jet Blue', 'AS190', 'Boeing', 100, '190', '2012-02-25');

-- e. Insert At least One airline Staff working for Jet Blue
INSERT INTO airline_staff (username, password, first_name, last_name, date_of_birth, airline_name) 
VALUES ('JaneSmith', 'securepassword', 'Jane', 'Smith', '1985-07-20', 'Jet Blue');

-- f. Insert several flights with on-time, and delayed statuses.
INSERT INTO flight 
(airline_name, flight_number, depart_date, depart_time, airplane_name, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_airport, arrival_airport) 
VALUES ('Jet Blue', JB111, '2024-12-01', '08:00:00', 'JB111', '11:30:00', '2024-12-01', 300, 'on-time', 'JFK', 'PVG');

INSERT INTO flight 
(airline_name, flight_number, departure_date, departure_time, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_code, arrival_code) 
VALUES ('Jet Blue', JB123, '2024-02-01', '09:00:00', 'AS190', '11:30:00', '2024-02-02', 700, 'delayed', 'JFK', 'PVG');

INSERT INTO flight 
(airline_name, flight_number, departure_date, departure_time, airplane_id, arrival_time, arrival_date, base_price, flight_status, departure_code, arrival_code) 
VALUES ('Jet Blue', JB146, '2024-03-01', '10:00:00', 'DL126', '01:30:00', '2024-03-02', 1000, 'delayed', 'PVG', 'JFK');


--g. Insert some tickets for corresponding flights and insert some purchase records (customers bought sometickets).
INSERT INTO ticket
(ticket_id, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, airline_name, flight_number, departure_date, departure_time) 
VALUES ('T1', 300, 'VISA', '4111111', 'Jackson Doe', '2025-08-31', '2024-11-01', '2024-11-01 09:30:00', 'Jet Blue', 'JB111', '2024-12-01', '08:00:00');

INSERT INTO ticket
(ticket_id, ticket_price, card_type, card_number, name_on_card, card_exp, purchase_date, purchase_time, airline_name, flight_number, departure_date, departure_time) 
VALUES ('T2', 700, 'MASTERCARD', '550004', 'Eric Smith', '2026-09-15', '2024-11-02', '2024-11-02 10:00:00', 'Jet Blue', 'JB123', '2024-02-01', '9:00:00');

INSERT INTO purchase (email, ticket_id)
VALUES ('jason1@gmail.com', 'T1');

INSERT INTO purchase (email, ticket_id)
VALUES ('james3@gmail.com', 'T2');
