CREATE TABLE books (
  id int NOT NULL,
  title varchar(1023),
  author varchar(1023),
  year int,
  genre varchar(1023),
  PRIMARY KEY (id)
);

INSERT INTO books (id, title, author, year, genre) VALUES
(1, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Southern Gothic'),
(2, '1984', 'George Orwell', 1949, 'Dystopian'),
(3, 'Pride and Prejudice', 'Jane Austen', 1813, 'Classic'),
(4, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Tragedy'),
(5, 'Moby Dick', 'Herman Melville', 1851, 'Adventure');
