Bitcoin-Stocks 📈

Bitcoin-Stocks is a full-stack data analysis web application built with Python, Flask, and SQLite.
The project focuses on ingesting, analyzing, and visualizing Bitcoin market data through a REST-style API and a clean web interface.

This project was built to gain hands-on experience with backend APIs, databases, and data-driven web applications.

🚀 Features

Flask backend serving REST API endpoints

SQLite database for storing historical Bitcoin market data

API endpoints for retrieving and filtering OHLCV data

Data cleaning and formatting for frontend display

Dynamic frontend rendering using JavaScript

Modular structure designed for future analytics and ML extensions

🧱 Tech Stack

Backend: Python, Flask

Database: SQLite

Data Processing: Pandas

Frontend: HTML, CSS, JavaScript

Version Control: Git & GitHub

📊 Data Schema

The Bitcoin market data is stored in SQLite with the following structure:

Column	Type
Start	TEXT
End	TEXT
Open	REAL
High	REAL
Low	REAL
Close	REAL
Volume	REAL
MarketCap	REAL

Column names are normalized at query time to ensure clean API responses.
