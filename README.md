## Basic Application Setup

I have setup a Docker file, so just to run this once you clone the repository would be 
* Install Docker.
* Run the following command to build the docker image `docker build -t <image-name> .`
* Once the image has been built, you can run the service by `docker run -p 9876:9876 gistapi`
  * You can run the above command with the `-d` to run it in the background.
* Visit the following url `127.0.0.1/ping` to confirm if it's up and running.   

In case you would like to run the application without Docker, 
* You would need `python:3.11` and [poetry](https://python-poetry.org/) installed.
* Once poetry has been installed, run `poetry install` to install the required dependencies.
* You can then run `poetry run python gistapi/gistapi.py` to start the server.
  * Or you can enter the virtual env using `poetry shell` and then run `python gistapi/gistapi.py`

Tests can be run by `poetry run pytest`

## Notes
* I have not written any tests for the methods from `api_service.py` since they are just calling the github api under the hood. it felt easier to just mock them than hitting the actual endpoints and I would be just testing if the endpoint is up or not. I would go with VCR.py in case I would need add tests for it.
* `Implement handling of huge gists` => Over the top of my head, I would move the entire process of fetching of gists and their details to a background job, so that we can process it asynchronously and then provide the result once the search is done. 
* `Set up the necessary tools to ensure code quality (feel free to pick up a set of tools you personally prefer)` => I have worked only with pylint and a basic config file. For this project I tried using black and found it very easy to configure on vscode and have it autocorrect the empty spaces I left everywhere. 


### Original readme content from here
-----------------------------------------------------------------------------------------------------------------------------------------
# Challenge

This challenge is divided between the main task and additional stretch goals. All of those stretch goals are optional, but we would love to see them implemented. It is expected that you should be able to finish the challenge in about 1.5 hours. If you feel you are not able to implement everything on time, please, try instead describing how you would solve the points you didn't finish.

And also, please do not hesitate to ask any questions. Good luck!

## gistapi

Gistapi is a simple HTTP API server implemented in Flask for searching a user's public Github Gists.
The existing code already implements most of the Flask boilerplate for you.
The main functionality is left for you to implement.
The goal is to implement an endpoint that searches a user's Gists with a regular expression.
For example, I'd like to know all Gists for user `justdionysus` that contain the pattern `import requests`.
The code in `gistapi.py` contains some comments to help you find your way.

To complete the challenge, you'll have to write some HTTP queries from `Gistapi` to the Github API to pull down each Gist for the target user.
Please don't use a github API client (i.e. using a basic HTTP library like requests or aiohttp or urllib3 is fine but not PyGithub or similar).


## Stretch goals

* Implement a few tests (using a testing framework of your choice)
* In all places where it makes sense, implement data validation, error handling, pagination
* Migrate from `requirements.txt` to `pyproject.toml` (e.g. using [poetry](https://python-poetry.org/))
* Implement a simple Dockerfile
* Implement handling of huge gists
* Set up the necessary tools to ensure code quality (feel free to pick up a set of tools you personally prefer)
* Document how to start the application, how to build the docker image, how to run tests, and (optionally) how to run code quality checkers
* Prepare a TODO.md file describing possible further improvements to the archtiecture:
    - Can we use a database? What for? SQL or NoSQL?
    - How can we protect the api from abusing it?
    - How can we deploy the application in a cloud environment?
    - How can we be sure the application is alive and works as expected when deployed into a cloud environment?
    - Any other topics you may find interesting and/or important to cover
