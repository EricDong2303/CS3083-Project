CREATE TABLE `database_project`.`customer` (
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `building_number` INT NOT NULL,
  `street_name` VARCHAR(100) NOT NULL,
  `apt_number` VARCHAR(100) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `state` VARCHAR(100) NOT NULL,
  `zipcode` INT NOT NULL,
  `passport_number` INT NOT NULL,
  `passport_exp` DATE NOT NULL,
  `passport_country` VARCHAR(100) NOT NULL,
  `dob` DATE NOT NULL,
  PRIMARY KEY (`email`)
  );

CREATE TABLE `database_project`.`customer_phone` (
  `email` VARCHAR(100) NOT NULL,
  `phone_number` INT NOT NULL,
  PRIMARY KEY (`email`, `phone_number`)
  foreign key(email) references customer(email)
  );

CREATE TABLE `database_project`.`purchases`(
    email varchar(100) not null,
    ticket_id varchar(100) not null,
    primary key(`email`, `ticket_id`),
    foreign key(email) references customer(email),
    foreign key(ticket_id) references ticket(ticket_id)
);
