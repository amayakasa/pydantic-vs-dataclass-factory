all:
	@$(MAKE) install
	@$(MAKE) tests

tests:
	python3 -m tests

install:
	pip3 install -r requirements.txt