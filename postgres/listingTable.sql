DROP TABLE if EXISTS listings;

CREATE TABLE listings(
  listingID integer NOT NULL,
  name varchar(30) NOT NULL,
  price integer NOT NULL,
  size varchar(2) NOT NULL,
  description text,
  sellerID integer NOT NULL,
  condition integer,
  onSale boolean,
  PRIMARY KEY (listingID),
  FOREIGN KEY (name) REFERENCES items (name)
);

INSERT INTO listings VALUES("1","Fuck The President Supreme T-Shirt", 80, "Medium", "Good Condition" , "543", 8, TRUE)
INSERT INTO listings VALUES("1","Fuck The President Supreme T-Shirt", 94, "Large", "Good Condition" , "544", 9, TRUE)
