run:
	docker-compose up --build

initdb:
	docker-compose run web python create_db.py

test:
	docker-compose run web python -m unittest discover

clean:
	docker-compose down -v
