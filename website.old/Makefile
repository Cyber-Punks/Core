.PHONY: run push

CONTAINER_CLI ?= sudo podman
CONTAINER_IMAGE ?= cyberpunks/website
CONTAINER_VERSION ?= latest

CONTAINER_TAG = ${CONTAINER_IMAGE}:${CONTAINER_VERSION}

container: package.json yarn.lock tsconfig.json public/ src/ Dockerfile
	${CONTAINER_CLI} build -t ${CONTAINER_TAG} .

run:
	${CONTAINER_CLI} run -it --rm --net host ${CONTAINER_TAG}

push:
	${CONTAINER_CLI} push ${CONTAINER_TAG}
