PHONY: all xml1 xml2 tests

all: xml1 xml2 tests

xml1:
	@cat "test/xml_lazar1.xml" | go run main.go

xml2:
	@cat "test/xml_lazar2.xml" | go run main.go

tests:
	go test -v
