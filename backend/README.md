Coffee Shop - Backend
-----

## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── src
  │   ├── auth
  │   │   ├── __init.py__ 
  │   │   ├── auth.py
  │   ├── database
  │   │   ├── __init.py__ 
  │   │   ├── database.db
  │   │   ├── models.py
  │   ├── __init.py__ 
  │   ├── .env
  │   ├── api.py 
  ├── requirements.txt
  ├── udacity-fsnd-udaspicelatte.postman_collection.json
  ```

## Setting up the Backend

   First, Follow instructions to install the latest version of python for your platform in the [python Documentation](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) or [install Python](https://www.python.org/downloads/) and [install PostgreSQL](https://www.postgresql.org/download/) if you haven't already.

   To start and run the local development server,

   1. Initialize and activate a virtual environment:

      We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

      ```
      $ cd YOUR_PROJECT_DIRECTORY_PATH/
      $ py -3 -m venv env
      $ env\Scripts\activate
      ```

   2. PIP Dependencies:
      
      Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory.

      ```
      $ cd backend/
      $ py -m pip install -r requirements.txt
      ```

      - [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

      - [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

      - [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

   3. Run the Server:

      From within the `./backend/src` directory first ensure you are working using your created virtual environment.

      Each time you open a new terminal session, run:

      ```bash
      export FLASK_APP=api.py;
      ```

      To run the server, execute:

      ```bash
      flask run --reload
      ```

      The `--reload` flag will detect file changes and restart the server automatically.

      /

      ```
      $ flask --app api.py run
      ```
