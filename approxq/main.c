#include <math.h>
#include <stdlib.h>
#include <stdio.h>

int main()
{
  int q = 809;
  int s = 350;
  int bound = q / 4;
  float result = 0;
  for (size_t i = 0; i < 12; i++) {
    int a = s + (rand() % (2 * bound + 1) - 101);
    result += a / pow(2, i);
    printf("Approximate %d with %d\n", s, a);
    printf("Subtract %d from %d to get %d\n", a, s, s-a);
    s = s - a;
    printf("multiply %d by 2 to get %d\n", s, 2*s);
    s = 2 * s;
  }
  printf("Result = %f\n", result);
}
