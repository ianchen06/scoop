.PHONY: dev

build:
	docker build -t scoop .
dev: build
	docker run -it --rm -v $$(pwd):/app -p 8000:8000 scoop python manage.py runserver 0.0.0.0:8000
dev-shell: build
	docker run -it --rm -v $$(pwd):/app -p 8000:8000 scoop bash
