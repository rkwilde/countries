# Data Engineering ETL Pipeline Challenge

## Overview
You are tasked with designing and implementing an ETL (Extract, Transform, Load) data pipeline that retrieves data from a public API, processes it, and loads it into a relational database. The pipeline should run on a schedule and handle real-world scenarios such as API failures, data validation, and efficient processing.

## Requirements

### Core Requirements
1. Create a data pipeline that:
   - Extracts data from one of the suggested public APIs (or another API of your choice)
   - Transforms the data to make it suitable for analysis
   - Loads the transformed data into a relational database
   - Runs on a regular schedule (hourly, daily, etc.)

2. Your solution must include:
   - A Python-based implementation for API extraction and data transformation
   - Storage of processed data in a file format like Parquet or CSV as an intermediate step
   - An upsert mechanism to load data into the target database
   - Proper error handling and logging
   - Unit tests for critical components

### Technical Guidelines
- **Programming Language**: Python 3.8+
- **Data Storage**: Any relational database (PostgreSQL, SQLite, or MySQL are good choices if you don't have access to Snowflake)
- **Scheduling**: Preferably using Airflow, but any orchestration tool is acceptable
- **Code Quality**: Follow PEP 8 guidelines, include docstrings, and maintain clean, modular code
- **Version Control**: Git repository with clear commit history

## Evaluation Criteria
Your solution will be evaluated based on:
1. **Functionality**: Does the pipeline work end-to-end?
2. **Code Quality**: Is the code clean, well-organized and following best practices?
3. **Scalability**: Could the solution handle larger volumes of data?
4. **Error Handling**: How does the pipeline handle errors and edge cases?
5. **Idempotency**: Can the pipeline run multiple times without duplicating data?
6. **Documentation**: Is the solution well documented?

## Extra Points
- Setting up a local Docker environment with Airflow and your database
- Implementing a proper CI/CD pipeline with GitHub Actions
- Making API calls asynchronous or multi-threaded to improve performance
- Creating a modular architecture that could be extended to other data sources
- Implementing comprehensive data validation
- Adding monitoring and alerting for pipeline failures

## Suggested APIs
Below are some suggested free public APIs that are well-suited for this challenge. You may choose one of these or any other API of your preference:

1. **CoinGecko API**
   - Data: Cryptocurrency market data
   - Documentation: [https://www.coingecko.com/api/documentation](https://www.coingecko.com/api/documentation)
   - No authentication required
   - Example endpoint: `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1`

2. **OpenWeather API**
   - Data: Current weather and forecasts
   - Documentation: [https://openweathermap.org/api](https://openweathermap.org/api)
   - Free API key required (simple signup)
   - Good for demonstrating incremental data loads

3. **REST Countries API**
   - Data: Country information including population, currencies, languages
   - Documentation: [https://restcountries.com/](https://restcountries.com/)
   - No authentication required
   - Example endpoint: `https://restcountries.com/v3.1/all`

4. **Open Library API**
   - Data: Book information, authors, publications
   - Documentation: [https://openlibrary.org/developers/api](https://openlibrary.org/developers/api)
   - No authentication required
   - Example endpoint: `https://openlibrary.org/subjects/python.json`

5. **NASA API**
   - Data: Astronomy Picture of the Day, Mars rover photos, etc.
   - Documentation: [https://api.nasa.gov/](https://api.nasa.gov/)
   - Free API key required (simple signup)
   - Example endpoint: `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`

## Submission Guidelines
1. Create a GitHub repository with your solution
2. Include a comprehensive README.md that:
   - Explains the architecture of your solution
   - Provides setup instructions
   - Documents any assumptions or design decisions
   - Outlines potential improvements or extensions
3. Make sure your code is well-commented and follows best practices
4. Include any necessary configuration files (Docker, Airflow DAGs, etc.)

## Time Expectation
We expect this challenge to take approximately 3-4 hours of focused work. Please don't spend more than 5 hours on this project.

## Questions?
If you have any questions or need clarification about the challenge, please don't hesitate to reach out to [contact email].

Good luck!
