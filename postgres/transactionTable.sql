DROP TABLE if EXISTS transactions;

CREATE TABLE transactions(
  ID                      integer        PRIMARY KEY NOT NULL,
  SellerID                integer        NOT NULL,
  BuyerID                 integer        NOT NULL,
  AmountExchanged         integer        NOT NULL,
  listingID               integer        REFERENCES listings(listingID),
  deliveryAddress         text           NOT NULL,
  receiveAddress          text           NOT NULL,
  timeOfSale              date,
  ratingSeller            integer,
  ratingBuyer             integer,
  isValid                 boolean,
);
