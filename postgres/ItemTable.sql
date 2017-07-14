DROP TABLE if EXISTS items;

CREATE TABLE items(
  name                    text PRIMARY KEY NOT NULL,
  description             text           NOT NULL,
  material                text,
  category                text           NOT NULL,
  subcategory             text,
  brand                   text           NOT NULL,
  avgSoldPrice            integer,
  leastSoldPrice          integer,
  highestSoldPrice        integer,
  lowestCurrentPrice      integer,
  highestCurrentPrice    integer
);


INSERT INTO items VALUES('Fuck The President Supreme T-Shirt','Supreme Spring/Summer 2017','Cotton','T-shirt',' ','Supreme',0,0,0,0,0);
INSERT INTO items VALUES('Barrington Levy Supreme T-Shirt', 'Supreme Spring/Summer 2017', 'Cotton', 'T-shirt',' ', 'Supreme',0,0,0,0,0);
INSERT INTO items VALUES('Bape X Coca Cola Baby Milo T-shirt', 'Bape Spring/Summer 2017', 'Cotton', 'T-Shirt',' ', 'A BATHING APE', 0,0,0,0,0);
INSERT INTO items VALUES('Box Logo Supreme CDG Hoodie', 'Supreme Spring/Summer 2017','Cotton','T-shirt',' ','Supreme',0,0,0,0,0);
INSERT INTO items VALUES("Supreme Box Logo Crewneck", "Supreme Fal/Winter 2015", "Cotton","T-Shirt", "Supreme",0,0,0,0,0)
INSERT INTO items VALUES("Vlone Long Sleeve Reversible Shirt", "Vlone","Cotton","T-shirt","Long Sleeve","Vlone",0,0,0,0,0)
