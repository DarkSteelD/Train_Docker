run:
	podman-compose up --build

initdb:
	podman-compose run web python create_db.py

test:
	podman-compose run web python -m unittest discover

clean:
	podman-compose down -v
