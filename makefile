local:
	FLASK_APP=app FLASK_DEBUG=1 python -m flask run

requirements:
	pip install -r requirements.txt
test:
	nosetests
