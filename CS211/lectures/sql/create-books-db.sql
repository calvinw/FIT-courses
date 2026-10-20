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

INSERT INTO books (id, title, author, year, genre) VALUES
(6, 'Dune', 'Frank Herbert', 1965, 'Science Fiction'),
(7, 'Foundation', 'Isaac Asimov', 1951, 'Science Fiction'),
(8, 'Do Androids Dream of Electric Sheep?', 'Philip K. Dick', 1968, 'Science Fiction'),
(9, 'A Fire Upon the Deep', 'Vernor Vinge', 1992, 'Science Fiction'),
(10, 'The Martian Chronicles', 'Ray Bradbury', 1950, 'Science Fiction');

INSERT INTO books (id, title, author, year, genre) VALUES
(11, 'The 7 Habits of Highly Effective People', 'Stephen Covey', 1989, 'Self Help'),
(12, 'Atomic Habits', 'James Clear', 2018, 'Self Help'),
(13, 'Daring Greatly', 'Brené Brown', 2012, 'Self Help'),
(14, 'Think and Grow Rich', 'Napoleon Hill', 1937, 'Self Help'),
(15, 'How to Win Friends and Influence People', 'Dale Carnegie', 1936, 'Self Help');
