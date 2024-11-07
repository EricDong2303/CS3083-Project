--a. One Airline name "Jet Blue".
INSERT INTO airline (airline_name) VALUES ('Jet Blue');

--b. At least Two airports named "JFK" in NYC and "PVG" in Shanghai.
INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('JFK', 'John F. Kennedy International Airport', 'New York', 'USA', 6, 'both');

INSERT INTO airport (code, name, city, country, number_of_terminals, type) VALUES 
('PVG', 'Shanghai Pudong International Airport', 'Shanghai', 'China', 3, 'both');

--c. Insert at least three customers with appropriate names and other attributes
INSERT INTO `customer` 
(email, password, first_name, last_name, building_number, street_name, apt_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('mike123@gmail.com', 'password123', 'Mike', 'Rafone', 1234, 'Main St', '100', 'New York', 'NY', 10001, 123456789, '2028-12-31', 'USA', '1985-06-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('mike123@gmail.com', '123456789');

INSERT INTO `customer` 
(email, password, first_name, last_name, building_number, street_name, apt_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('jason1@gmail.com', 'goodpassword', 'Jason', 'Jackson', 1, 'Street St', '200', 'New York', 'NY', 10001, 987654321, '2029-12-31', 'USA', '1988-06-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('jason1@gmail.com', '987654321');

INSERT INTO `customer` 
(email, password, first_name, last_name, building_number, street_name, apt_number, city, state, zipcode, passport_number, passport_exp, passport_country, dob) 
VALUES ('james3@gmail.com', 'badpassword', 'James', 'Wang', 43, 'Yes St', '300', 'New York', 'NY', 10001, 1111111111, '2026-11-31', 'USA', '1990-07-15');

INSERT INTO customer_phone(email, phone_number) VALUES ('james3@gmail.com', '1111111111');

--d. Insert at least three airplanes.
INSERT INTO `airplane` (airline_name, id, seats, model_number, manufacture_date, age, maintainance_start, maintainance_end) 
VALUES ('Jet Blue', 'JB111', 150, 'A320', '2015-05-20', 7, '2023-01-01', '2023-01-15');

INSERT INTO `airplane` (airline_name, id, seats, model_number, manufacture_date, age, maintainance_start, maintainance_end) 
VALUES ('Delta', 'DL126', 180, 'B737', '2018-08-10', 5, '2023-06-01', '2023-06-10');

INSERT INTO `airplane` (airline_name, id, seats, model_number, manufacture_date, age, maintainance_start, maintainance_end) 
VALUES ('Alaska Airlines', 'AS190', 100, 'E190', '2012-02-25', 11, '2023-03-01', '2023-03-15');

--e. Insert At least One airline Staff working for Jet Blue
INSERT INTO airline_staff (username, staff_password, first_name, last_name, dob, airline_name) 
VALUES ('JaneSmith', 'securepassword', 'Jane', 'Smith', '1985-07-20', 'Jet Blue');
