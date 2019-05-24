#include <stdio.h>
#include <stdlib.h>

int main() {
  fprintf(stderr, "%s\n", getenv("QUERY_STRING"));
  printf("HTTP/1.1 200 OK\n\nOK\n");
  return 0;
}
