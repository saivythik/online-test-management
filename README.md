# Online Test Management System

This is a FastAPI-based online test management system where admins can create tests and users can attempt the tests and receive their results.

## Features

- User authentication and authorization
- Admin functionality: Create, update, and delete tests; view all users' results
- User functionality: Attempt available tests, view their test results
- MySQL database for data storage
- Docker support for easy deployment

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/online-test-management.git
   cd online-test-management
   ```

2. Set up a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the MySQL database and update the connection string in `database.py`.

4. Run the application:
   ```
   uvicorn main:app --reload
   ```

## Running Tests

To run the unit tests:

```
pytest
```

## Docker Usage

To build and run the Docker container:

```
docker build -t online-test-management .
docker run -p 8000:8000 online-test-management
```

## API Documentation

Once the application is running, you can access the API documentation at `http://localhost:8000/docs`.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.