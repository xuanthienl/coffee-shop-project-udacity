Coffee Shop - Frontend
-----

## Main Files: Project Structure

    ```sh
    ├── README.md
    ├── e2e
    ├── src
        ├── app 
        ├── assets
        ├── environments
        ├── theme
        ├── index.html
    ```

## Getting Setup

    > _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman, and then the frontend should integrate smoothly.

## Setting up the Frontend

    First, [Install Node](https://nodejs.com/en/download) if you haven't already.

    Second, [Install Ionic Framework](https://ionicframework.com/docs/installation/cli) if you haven't already.

    1. Installing project dependencies:
    
        This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

        ```
        $ npm install
        ```

        _tip_: `npm i`is shorthand for `npm install``

    2. Configure Environment Variables

        Ionic uses a configuration file to manage environment variables. These variables ship with the transpiled software and should not include secrets.

        - Open `./src/environments/environments.ts` and ensure each variable reflects the system you stood up for the backend.

    3. Run the Server:

        Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

        ```bash
        ionic serve
        ```

        > _tip_: Do not use **ionic serve** in production. Instead, build Ionic into a build artifact for your desired platforms.
        > [Checkout the Ionic docs to learn more](https://ionicframework.com/docs/cli/commands/build)

        - If error, add step: export NODE_OPTIONS=--openssl-legacy-provider (use "set" for Windows)
