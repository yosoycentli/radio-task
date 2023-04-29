FROM python:3.9

# Set the current working directory to /code.

# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /code

# Copy the file with the requirements to the /code directory.

# Copy only the file with the requirements first, not the rest of the code.

# As this file doesn't change often, Docker will detect it and use the cache for this step, enabling the cache for the next step too.
# COPY ./requirements.txt /code/requirements.txt
COPY . .

# ENV PATH ++++/bin:${PATH}

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
# COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]