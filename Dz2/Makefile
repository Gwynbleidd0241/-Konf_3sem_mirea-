.PHONY: run tests

run:
	 go run main.go -config=config.xml
	dot -Tpng ./files/output.dot -o ./files/output.png
tests:
	 go test

.DEFAULT_GOAL := run