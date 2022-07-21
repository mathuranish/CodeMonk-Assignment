# CodeMonk-Assignment
Created a REST API using DRF that takes in multiple paragraphs of text as input, stores each paragraph in database
and search fow word in paragraphs.


##Functionality
- Created custom user models.
- User can login via email and password.
- Admin Dashboard can be accessed via email and password
- User should first login via the api
- All subsequent api requests must be authenticated or else they will fail.
- Generates a unique ID for every paragraph that is indexed. A paragraph is defined by two newline characters.
- Convert all words to lowercase.
- Resgistered Users can search a word in paragraph at `http://127.0.0.1:8000/search/<word>` and max result of 10 paragraphs will be shown.
- List all paragraph or access them individually at `127.0.0.1:8000/list`
- Delete paragraphs individually. 
- Provided a proper Swagger API documentation.

## Getting started

- Used Django for Backend
- Used Docker to Containerize the project
- Swagger to access the stored paragraphs and accounts.

## Run Locally

### Using Docker

- Run `docker-compose up`

### Building from source

- Fork the repo `https://github.com/mathuranish/CodeMonk-Assignment` 
- Clone the repo and type the following command in terminal
    `git clone git@github.com:mathuranish/CodeMonk-Assignment.git`
- Create a virtual environment using the python command
    `python3 -m venv env`
- Install the dependencies
    `pip install -r requirements.txt`
- After the dependencies are install run the migration using command
    `python3 manage.py makemigrations && python3 manage.py migrate`
- Start the server through the following command
    `python3 manage.py runserver` -> To run Django Server.
- Register new User at `127.0.0.1:8000/auth/signup`
- Login user at `127.0.0.1:8000/auth/login`
- Add paragraphs using Swagger.
- Search for Word in the paragraphs.

