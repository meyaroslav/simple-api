CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INT NOT NULL
);

INSERT INTO books (title, author, year) VALUES
('1984', 'George Orwell', 1949),
('Brave New World', 'Aldous Huxley', 1932),
('Fahrenheit 451', 'Ray Bradbury', 1953);
