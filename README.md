# Local 30nama

This is a fork of the 30nama hybrid version, designed to resolve issues by allowing users to serve the client locally using a simple Python command.

## Background

The original 30nama hybrid version encountered some problems. This fork provides a solution by offering a local server setup, making it easier for users to run and test the application on their own machines.

## Prerequisites

- Python 3.x installed on your system
- The project files cloned or downloaded to your local machine

## Setup

1. Clone this repository or download the project files to your local machine.
2. Navigate to the project directory in your terminal or command prompt.
3. Ensure you have a directory named 'web' in the same location as the `server.py` file. This is where your static files should be placed.

## Usage

To start the local server, run the following command in your terminal:

```bash
python3 server.py
```

This will start a local server, typically at `http://localhost:8090`. The server will automatically attempt to open this URL in your default web browser.

## Features

- Serves static files from the './web' directory
- Enables CORS (Cross-Origin Resource Sharing) for all origins
- Disables caching to ensure you always get the latest version of your files

## Troubleshooting

If you encounter any issues:

1. Ensure Python 3.x is correctly installed on your system.
2. Check that you're in the correct directory when running the server command.
3. Verify that your static files are placed in the 'web' directory.
4. If the browser doesn't open automatically, manually navigate to `http://localhost:8090` in your web browser.


## Disclaimer

This is a fork created to resolve issues with the original 30nama hybrid version. It is not officially associated with or endorsed by the original 30nama project.

