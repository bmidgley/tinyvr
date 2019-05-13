
www/position.cgi: position.c
	cc -o www/position.cgi position.c

clean:
	rm -f position.cgi

all: position.cgi
