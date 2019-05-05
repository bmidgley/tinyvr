#include <stdio.h>
#include <stdlib.h>

int main() {
  fprintf(stderr, "%s\n", getenv("QUERY_STRING"));
  return 0;
}
