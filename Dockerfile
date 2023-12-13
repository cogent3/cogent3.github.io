# Start with a base Debian image
FROM debian:bookworm-slim

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Install any needed packages
RUN apt-get update && \
    apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3-pip \
    python3-venv \  
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    zsh \
    curl \
    git \
    gcc \
    autojump && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Python 3.11 as the default Python version: requires root
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# install sudo so we can create a non root account to use as default
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to non-root user
USER $USERNAME

# Create the virtual environment, activate it, and install packages
RUN python3 -m venv /home/user/c3org && \
    . /home/user/c3org/bin/activate && \
    pip install --upgrade pip

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Make zsh the default shell
SHELL ["/bin/zsh", "-c"]

# Create the /cogent3.github.io directory
RUN sudo mkdir -p /cogent3.github.io

# Set the working directory in the container to /cogent3.github.io
WORKDIR /cogent3.github.io

# Copy the requirements.txt file into the Docker image
COPY requirements.txt /cogent3.github.io/requirements.txt

# Install any needed packages specified in requirements.txt into the virtual environment
RUN /home/user/c3org/bin/pip install --no-cache-dir -r /cogent3.github.io/requirements.txt

# Activate the virtual environment when a new shell is started
RUN echo 'source /home/user/c3org/bin/activate' >> ~/.zshrc
