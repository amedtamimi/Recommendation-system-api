FROM python:3.9

# Maintainer info
LABEL maintainer="ameedtamimi@gmail.com"

# Make working directories
RUN  mkdir -p  /RecommendationApi
WORKDIR  /RecommendationApi

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy every file in the source folder to the created working directory
COPY  . .

# Run the python application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
