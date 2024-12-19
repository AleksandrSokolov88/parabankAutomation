06.11.2024
Upload to GitHub
Fixing a lot
Too lazy to write readme

test cases here
https://app.qase.io/project/PARABANK

Install docker ubuntu

1. Update the current packages

Commands:

sudo apt update
sudo apt upgrade -y

Why:

    apt update updates the package index to ensure the system knows about the latest versions of packages.
    apt upgrade upgrades the installed packages to their latest versions.

Sure! Here’s the same explanation translated into English:

1. Update the current packages

Commands:

sudo apt update  
sudo apt upgrade -y

Why:

    apt update updates the package index to ensure the system knows about the latest versions of packages.
    apt upgrade upgrades the installed packages to their latest versions.

Reasoning:
Keeping your system updated reduces the chance of compatibility issues between existing packages and the new ones (like
Docker).

2. Install dependencies

Command:

sudo apt install -y \
ca-certificates \
curl \
gnupg \
lsb-release

What the packages do:

    ca-certificates: Installs root certificates for verifying the authenticity of downloaded packages.
    curl: A tool to download files from web servers (used to fetch Docker's GPG key).
    gnupg: Provides tools for working with GPG keys, which verify the authenticity of packages.
    lsb-release: Allows the system to determine the Ubuntu distribution version (e.g., 20.04 or 22.04).

3. Add Docker's GPG key

Command:

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

Why:
Docker signs its packages with a GPG key to ensure their authenticity. We need to download this key and save it in a
format compatible with APT.

What happens:

    mkdir -p /etc/apt/keyrings: Creates a directory to store the key (if it doesn’t already exist).
    curl -fsSL ...: Downloads the key from Docker's official website.
    sudo gpg --dearmor ...: Converts the key into binary format (.gpg) for APT.

4. Configure the Docker repository

Command:

echo \
"
deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

What happens:

    deb: Indicates the repository format for APT.
    [arch=$(dpkg --print-architecture)]: Ensures packages are downloaded for the system’s architecture (e.g., amd64 or arm64).
    signed-by=/etc/apt/keyrings/docker.gpg: Links the repository to the previously downloaded GPG key.
    https://download.docker.com/linux/ubuntu: Docker’s official repository URL.
    $(lsb_release -cs): Automatically inserts your Ubuntu version's codename (e.g., focal for 20.04).
    stable: Specifies the stable release of Docker.

5. Install Docker

Command:

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

What the packages do:

    docker-ce: The core Docker engine (Community Edition).
    docker-ce-cli: The command-line client to manage Docker.
    containerd.io: A container runtime used by Docker to handle container operations.
    docker-buildx-plugin: A plugin that enables advanced image-building features.
    docker-compose-plugin: A plugin for managing multi-container applications with Docker Compose.

6. Verify the installation

Command:

sudo docker --version

Why:
This checks if Docker is installed correctly and outputs its version. A successful output confirms the installation.

Sure! Here’s the same explanation translated into English:

1. Update the current packages

Commands:

sudo apt update
sudo apt upgrade -y

Why:

    apt update updates the package index to ensure the system knows about the latest versions of packages.
    apt upgrade upgrades the installed packages to their latest versions.

Reasoning:
Keeping your system updated reduces the chance of compatibility issues between existing packages and the new ones (like
Docker).

2. Install dependencies

Command:

sudo apt install -y \
ca-certificates \
curl \
gnupg \
lsb-release

What the packages do:

    ca-certificates: Installs root certificates for verifying the authenticity of downloaded packages.
    curl: A tool to download files from web servers (used to fetch Docker's GPG key).
    gnupg: Provides tools for working with GPG keys, which verify the authenticity of packages.
    lsb-release: Allows the system to determine the Ubuntu distribution version (e.g., 20.04 or 22.04).

Reasoning:
These are essential tools and libraries that Docker relies on. Without them, the system cannot validate package
signatures or fetch the required files.

3. Add Docker's GPG key

Command:

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

Why:
Docker signs its packages with a GPG key to ensure their authenticity. We need to download this key and save it in a
format compatible with APT.

What happens:

    mkdir -p /etc/apt/keyrings: Creates a directory to store the key (if it doesn’t already exist).
    curl -fsSL ...: Downloads the key from Docker's official website.
    sudo gpg --dearmor ...: Converts the key into binary format (.gpg) for APT.

Reasoning:
Without the GPG key, the system won’t trust Docker’s packages and will refuse to install them.

4. Configure the Docker repository

Command:

echo \
"
deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

What happens:

    deb: Indicates the repository format for APT.
    [arch=$(dpkg --print-architecture)]: Ensures packages are downloaded for the system’s architecture (e.g., amd64 or arm64).
    signed-by=/etc/apt/keyrings/docker.gpg: Links the repository to the previously downloaded GPG key.
    https://download.docker.com/linux/ubuntu: Docker’s official repository URL.
    $(lsb_release -cs): Automatically inserts your Ubuntu version's codename (e.g., focal for 20.04).
    stable: Specifies the stable release of Docker.

Reasoning:
This step adds Docker's official repository to the system, allowing APT to fetch and install Docker packages tailored
for your Ubuntu version.

5. Install Docker

Command:

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

What the packages do:

    docker-ce: The core Docker engine (Community Edition).
    docker-ce-cli: The command-line client to manage Docker.
    containerd.io: A container runtime used by Docker to handle container operations.
    docker-buildx-plugin: A plugin that enables advanced image-building features.
    docker-compose-plugin: A plugin for managing multi-container applications with Docker Compose.

Reasoning:
These packages collectively provide all the tools needed to run, manage, and build Docker containers.

6. Verify the installation

Command:

sudo docker --version

Why:
This checks if Docker is installed correctly and outputs its version. A successful output confirms the installation.

7. Run Docker without sudo

Command:

sudo usermod -aG docker $USER  
sudo reboot

What happens:

    usermod -aG docker $USER: Adds the current user to the docker group, allowing them to run Docker commands without sudo.

https://mailtrap.io/inboxes/3340403/messages

https://eu-north-1.console.aws.amazon.com/ec2/home?region=eu-north-1#Instances:instanceState=running

https://www.youtube.com/watch?v=O8N1lvkIjig