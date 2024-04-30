# URL Shortener

### A user friendly URL shortening service built with FastAPI for backend, utilizing AWS DynamoDB as a Database, and hosted on AWS EC2.

## Technologies

### Backend

FastAPI (Python REST API framework)
Uvicorn (ASGI Server)
AWS DynamoDB (NoSQL Database)

### Frontend:

the skeleton for the frontend was downloaded from free-css.com and adjusted for my simple needs
https://www.free-css.com/free-css-templates/page296/listrace

### Infrastructure:

AWS EC2 (Ubuntu),
Nginx (Reverse Proxy)

## Usage
The frontend can be found at http://galvardi.com, the projects Rest api can be found at http://galvardi.com/api/docs

## Project Structure

frontend - continains the assets and index.html files

app.py - Contains core functions and logic for the url shortening Fastapi.

constants.py - Stores application-wide constants.

dependencies_container.py - Manages dependency injection, Ensures proper initialization and management of external
dependencies, promoting a clean separation of concerns.

dynamo_db_manager.py - Encapsulates and isolates all interactions with AWS DynamoDB, handling CRUD (Create, Read,
Update, Delete) operations for shortened URLs.

main.py - used mainly in production runs the uvicorn server

utils.py - Houses helper function for URL shortening logic, hash generation.

requirements.txt - Lists all necessary Python dependencies for the project.

## Future Improvements

- more accessible logging using CloudWatch
- continuous integration tests for easier deployment
- SSL certificate to Nginx to allow https
- further exception handling

## Contact

Gal Vardi, for any questions you can reach me at : galvardi11@gmail.com
