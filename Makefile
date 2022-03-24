NAME ?= nikhilsharma710

all: build run push

images:
	docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

build:
	docker build -t ${NAME}/midterm:1.0 .

run:
	docker run --rm -d -p 5029:5000 --name nikhil-midterm ${NAME}/midterm:1.0

push:
	docker push ${NAME}/midterm:1.0

pull:
	docker pull ${NAME}/midterm:1.0

kill:
	docker rm -f nikhil-midterm
