# AOI

Python 3.5+

# Install Docker

	sudo dpkg -i docker-ce_17.03.2~ce-0~ubuntu-xenial_amd64.deb
	sudo cp docker-compose /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
	XSOCK=/tmp/.X11-unix
	xhost +SI:localuser:root

# Save the docker image as a tar file

	docker save -o <save image to path> <image name>

# Load the image into docker

	docker load -i <path to image tar file>
