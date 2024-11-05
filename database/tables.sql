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
  `customercol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`email`));
);
