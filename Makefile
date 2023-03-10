EXECUTABLE ?= jalapeno
BINARY ?= bin/$(EXECUTABLE)
REPO=iejalapeno
REGISTRY_NAME?=docker.io/iejalapeno
IMAGE=srv6-localsids
TAG=latest
# If you connect to dockerhub via a proxy: uncomment and edit the following line (and see below docker build lines)
#PROXY=http://proxy.esl.cisco.com:8080

all: build

build:
	pip3 install -r requirements.txt

run:
	python3 srv6-localsids-proc.py

container: 
	docker build -t ${REPO}/${IMAGE}:${TAG} .

push: 
	docker push $(REGISTRY_NAME)/srv6-localsids:$(IMAGE_VERSION)