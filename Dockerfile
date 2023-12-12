FROM python:3.11-slim-buster

# Install any needed packages
RUN apt-get update && apt-get install -y \
    zsh \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Make zsh the default shell
SHELL ["/bin/zsh", "-c"]

# Create the /cogent3.github.io directory
RUN mkdir -p /cogent3.github.io

# Set the working directory in the container to /cogent3.github.io
WORKDIR /cogent3.github.io

# Create a Python virtual environment outside of the workspace folder
RUN python -m venv /c3org

# Copy the requirements.txt file into the Docker image
COPY requirements.txt /cogent3.github.io/requirements.txt

#Update pip in the virtual environment 
RUN /c3org/bin/python -m pip install --upgrade pip

# Install any needed packages specified in requirements.txt into the virtual environment
RUN /c3org/bin/pip install --no-cache-dir -r /cogent3.github.io/requirements.txt

# Activate the virtual environment when a new shell is started
RUN echo 'source /c3org/bin/activate' >> ~/.zshrc