
position.cgi: position.c
	cc -o position.cgi position.c

clean:
	rm -f position.cgi

all: position.cgi
