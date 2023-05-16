SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


-- Table Structure for Venues

DROP TABLE IF EXISTS Venues;
CREATE TABLE Venues (
    venue_id int AUTO_INCREMENT UNIQUE NOT NULL,
    address varchar(255) NOT NULL,
    capacity int NOT NULL,
    email varchar(255) NOT NULL,
    phone_number varchar(255) NOT NULL,
    PRIMARY KEY (venue_id)
);

-- Inserting Data into Venues

INSERT INTO Venues (address, capacity, email, phone_number)
VALUES ('26617 NE 120th St, Big Tree, WA 98019', 20000, 'venue1@email.com', '1111-222-2222'),
('2348 N Mountain Rd, Placeville, CA 95947', 15000, 'venue2@email.net', '1010-221-6622'),
('5901 Place Ave, Queens, NY 11378', 30000, 'venue3@email.com', '666-666-0000');

-- Table Structure for Artists

DROP TABLE IF EXISTS Artists;
CREATE TABLE Artists (
    artist_id int AUTO_INCREMENT UNIQUE NOT NULL,
    artist_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    phone_number varchar(255) NOT NULL,
    PRIMARY KEY (artist_id)
);

-- Inserting Data into Artists

INSERT INTO Artists (artist_name, email, phone_number)
VALUES ('Invisible Band', 'invisb@email.net', '555-222-1111'),
('Beethoven', 'beets@email.com', '222-111-0000'),
('Tavern Bard', 'tavernb@email.net', '444-444-4444');

-- Table Structure for Customers

DROP TABLE IF EXISTS Customers;
CREATE TABLE Customers (
    customer_id int AUTO_INCREMENT UNIQUE NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    phone_number varchar(255),
    PRIMARY KEY (customer_id)
);

-- Inserting Data into Customers

INSERT INTO Customers (first_name, last_name, email, phone_number)
VALUES ('Mary', 'Smith', 'marysm@email.com', NULL),
('George', 'Boole', 'georgeb@email.com', '111-000-1111'),
('Pierre', 'Fermat', 'pierreferm@email.net', '555-363-3363');

-- Table Structure for Concerts

DROP TABLE IF EXISTS Concerts;
CREATE TABLE Concerts (
    concert_id int AUTO_INCREMENT UNIQUE NOT NULL,
    date date NOT NULL,
    time time NOT NULL,
    venue_id int NOT NULL,
    artist_id int NOT NULL,
    PRIMARY KEY (concert_id),
    FOREIGN KEY (venue_id) REFERENCES Venues(venue_id) 
		ON DELETE CASCADE,
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
		ON DELETE CASCADE
);

-- Inserting Data into Concerts

INSERT INTO Concerts (date, time, venue_id, artist_id)
VALUES ('2023-12-20', '18:00:00', 1, 1),
('2023-12-14', '16:00:00', 1, 3),
('2024-01-12', '20:00:00', 3, 3);

-- Table Structure for TicketSales

DROP TABLE IF EXISTS TicketSales;
CREATE TABLE TicketSales (
    sale_number int AUTO_INCREMENT UNIQUE NOT NULL,
    sale_date date NOT NULL,
    amount_paid decimal(10,2) NOT NULL,
    customer_id int NOT NULL,
    PRIMARY KEY (sale_number),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
		ON DELETE CASCADE
);

-- Inserting Data into TicketSales

INSERT INTO TicketSales (sale_date, amount_paid, customer_id)
VALUES ('2023-09-24', 200.00, 2),
('2023-09-24', 400.00, 3),
('2024-08-12', 200.00, 1);

-- Table Structure for Concerts_TicketSales

DROP TABLE IF EXISTS Concerts_TicketSales;
CREATE TABLE Concerts_TicketSales (
    concert_sale_id int AUTO_INCREMENT UNIQUE NOT NULL,
    sale_number int NOT NULL,
    concert_id int NOT NULL,
    PRIMARY KEY (concert_sale_id),
    FOREIGN KEY (sale_number) REFERENCES TicketSales(sale_number)
		ON DELETE CASCADE,
    FOREIGN KEY (concert_id) REFERENCES Concerts(concert_id)
		ON DELETE CASCADE
);

-- Inserting Data into Concerts_TicketSales

INSERT INTO Concerts_TicketSales (sale_number, concert_id)
VALUES (1, 1), (3, 1), (3, 1), (2, 3);


SET FOREIGN_KEY_CHECKS=1;
COMMIT;