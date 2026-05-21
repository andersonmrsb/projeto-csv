📄 CSV Netflix Project
🎯 Purpose
This application is designed to query and organize Netflix titles (movies and TV shows) from a SQLite database.
Users can explore information such as the number of titles, countries of origin, release years, and production types.

📂 Project Structure
app.py → Main file with the interactive menu for the user.

functions.py → Set of functions that perform queries on the database.

reposit.py → Class responsible for connecting to and executing queries in SQLite.

Database (netflix.db) → Contains the netflix table with columns such as:

Title

Type (Movie or TV Show)

Country

Release year

⚙️ Features
List all titles: displays all records from the database.

Count titles: returns the total number of titles, with optional filtering by type (movie or TV show).

List countries without repetition: shows all unique countries, even when they appear in combinations.

List movies and TV shows by country: given a selected country, displays movies first and then TV shows.

List available years: shows all unique release years present in the database.

List movies by year: displays all movies released in a specific year.

🧩 Development Approach
This project was built using:

SOLID principles → ensuring maintainable, scalable, and flexible code design.

DRY (Don't Repeat Yourself) → avoiding redundancy and promoting code reuse.

Object-Oriented Programming (OOP) → organizing the application into classes and methods for clarity and extensibility.