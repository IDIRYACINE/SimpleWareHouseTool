CREATE TABLE `Sales` (
  `id` int PRIMARY KEY Default CURRENT_TIMESTAMP,
  `sale_date` Date,
  `country` varchar(50),
  `sale_profit` float,
  `sale_status` int ,
  `product_code` Varchar(30),
  `sale_quantity` int,
  `postal_code` int
);

CREATE TABLE `Countries` (
  `country_code` int PRIMARY KEY,
  `country_name` varchar(255)
);

CREATE TABLE `Cities` (
  `postal_code` int,
  `city_name` varchar(255),
  `country_code` int,
  PRIMARY KEY (`postal_code`, `country_code`)
);

CREATE TABLE `Products` (
  `product_code` varchar(30) PRIMARY KEY,
  `product_name` varchar(255)
);

CREATE TABLE `Summaries` (
  `id` int Primary Key Default CURRENT_TIMESTAMP,
  `generated_date` Date ,
  `visiblity_level` int,
  `sale_date` Date,
  `profit` float,

);

CREATE INDEX `Sales_index_0` ON `Sales` (`sale_date`, `country_code`, `product_code`);

CREATE INDEX `Summaries_index_1` ON `Summaries` (`visiblity_level`, `sale_date`);

ALTER TABLE `Sales` ADD FOREIGN KEY (`product_code`) REFERENCES `Products` (`product_code`);

ALTER TABLE `Sales` ADD FOREIGN KEY (`postal_code`) REFERENCES `Cities` (`postal_code`);

ALTER TABLE `Cities` ADD FOREIGN KEY (`country_code`) REFERENCES `Countries` (`country_code`);


