.PHONY: run gcloud-push gcloud-auth

CONTAINER_CLI ?= sudo podman
CONTAINER_IMAGE ?= cyber-punks-website
CONTAINER_VERSION ?= latest

CONTAINER_TAG = ${CONTAINER_IMAGE}:${CONTAINER_VERSION}

GCLOUD_CONTAINER_HOST = us.gcr.io
GCLOUD_PROJECT_ID = cyber-punks-299119
GCLOUD_CONTAINER_TAG = ${GCLOUD_CONTAINER_HOST}/${GCLOUD_PROJECT_ID}/${CONTAINER_TAG}

container: package.json yarn.lock tsconfig.json public/ src/ Dockerfile
	${CONTAINER_CLI} build -t ${CONTAINER_TAG} .

run:
	${CONTAINER_CLI} run -it --rm --net host ${CONTAINER_TAG}

gcloud-push:
	${CONTAINER_CLI} tag ${CONTAINER_TAG} ${GCLOUD_CONTAINER_TAG}
	${CONTAINER_CLI} push ${GCLOUD_CONTAINER_TAG}

gcloud-auth:
	gcloud auth print-access-token | ${CONTAINER_CLI} login -u oauth2accesstoken --password-stdin ${GCLOUD_CONTAINER_HOST}
