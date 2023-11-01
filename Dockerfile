# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the `pyproject.toml` and `poetry.lock` to the container
COPY pyproject.toml poetry.lock /app/

# Install Poetry and project dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . /app

# Expose the port on which your Flask app will run
EXPOSE 80

# Run your Flask app using Poetry
CMD ["poetry", "run", "python", "gistapi/gistapi.py"]
