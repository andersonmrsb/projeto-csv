📄 Netflix CSV Project
🎯 Purpose  
This application was designed to query and organize Netflix titles (movies and TV shows) using a SQLite database. Users can explore information such as the number of titles, countries of origin, release years, and types of production.

The CSV file used as the data source is available here: Netflix Movies and TV Shows – Kaggle.

📂 Project Structure

app.py → Main file with the interactive menu for the user.

functions.py → Set of functions that perform queries on the database.

reposit.py → Class responsible for connecting and executing queries in SQLite.

Database (netflix.db) → Contains the Netflix table with columns such as:

Title

Type (Movie or TV Show)

Country

Release Year

⚙️ Features

List all titles: displays all records from the database.

Count titles: returns the total number of titles, with optional filtering by type (movie or series).

List countries without repetition: shows all unique countries, even when they appear in combinations.

List movies and series by country: given a selected country, displays movies first and then TV shows.

List available years: shows all unique release years present in the database.

List movies by year: displays all movies released in a specific year.

🧩 Development Approach  
This project was built using:

SOLID principles → ensuring sustainable, scalable, and flexible code design.

DRY (Don’t Repeat Yourself) → avoiding redundancy and promoting code reuse.

Object-Oriented Programming (OOP) → organizing the application into classes and methods for greater clarity and extensibility.
