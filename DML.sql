-- SELECT
SELECT address, capacity, email, phone_number FROM Venues;

SELECT artist_name, email, phone_number FROM Artists
ORDER BY artist_name;

SELECT sale_number, customer_id, sale_date, amount_paid FROM TicketSales
ORDER BY sale_number;

-- INSERT
INSERT INTO Venues (address, capacity, email, phone_number)
VALUES(:address_input, :capacity_input, :email_input, :phone_number_input);

INSERT INTO Artists (artist_name, email, phone_number)
VALUES(:artist_name_input, :email_input, :phone_number_input);

INSERT INTO TicketSales (customer_id, sale_date, amount_paid)
VALUES(:customer_id, :sale_date_input, :amount_paid_input);

-- UDPATE
UPDATE Venues
SET address = :address_input, email = :email_input, phone_number = :phone_number_input
WHERE venue_id = :venue_id_input;

UPDATE Artists
SET artist_name = :artist_name_input, email = :email_input, phone_number = :phone_number_input
WHERE artist_id = :artist_id_input;

UPDATE TicketSales
SET sale_date = :sale_date_input, amount_paid = :amount_paid_input
WHERE sale_number = :sale_number_input;

-- DELETE
DELETE FROM Venues WHERE venue_id = :venue_id_input;
DELETE FROM Artists WHERE artist_id = :artist_id_input;
DELETE FROM TicketSales WHERE sale_number = :sales_number_input;


-- Queries for Customers
-- Create
INSERT INTO Customers (first_name, last_name, email, phone_number)
VALUES (:first_nameInput, :last_nameInput, :emailInput, :phone_numberInput);

-- Read
SELECT customer_id, first_name, last_name, email, phone_number FROM Customers;

-- Update
SELECT customer_id, first_name, last_name, email, phone_number FROM Customers WHERE customer_id = :selected_id;
UPDATE Customers 
    SET first_name = :first_nameInput, last_name = :last_nameInput, 
    email = :emailInput, phone_number = :phone_numberInput
    WHERE customer_id = :selected_id;

--Delete
DELETE FROM Customers WHERE customer_id = :selected_id;


-- Queries for Concerts
-- get venue IDs for dropdown
SELECT venue_id FROM Venues;

-- get artist IDs for dropdown
SELECT artist_id, artist_name FROM Artists;

-- Create
INSERT INTO Concerts (date, time, venue_id, artist_id)
VALUES (:dateInput, :timeInput, :venue_idInput, :artist_idInput);

-- Read
SELECT concert_id, date, time, venue_id, Artists.artist_name FROM Concerts
    INNER JOIN Artists ON Artists.artist_id = Concerts.artist_id;

-- Update
SELECT concert_id, date, time, venue_id, Artists.artist_name FROM Concerts
    INNER JOIN Artists ON Artists.artist_id = Concerts.artist_id 
    WHERE concert_id = :selected_id;

UPDATE Concerts 
    SET date = :dateInput, time = :timeInput, 
    venue_id = :venue_idInput, artist_id = :artist_idInput
    WHERE concert_id = :selected_id;

--Delete
DELETE FROM Concerts WHERE concert_id = :selected_id;


-- Queries for Concerts_TicketSales
-- Read
SELECT concert_sale_id, sale_number, concert_id FROM Concerts_TicketSales;