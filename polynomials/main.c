#include <stdio.h>

#define N 2
typedef union {
  unsigned long int n;
  unsigned char bucket[8];
} buckets;

int count_bits(unsigned char b) {
  int b0 = ((1&b) == 1) ? 1 : 0;
  int b1 = ((2&b) == 2) ? 1 : 0;
  int b2 = ((4&b) == 4) ? 1 : 0;
  int b3 = ((8&b) == 8) ? 1 : 0;
  int b4 = ((16&b) == 16) ? 1 : 0;
  int b5 = ((32&b) == 32) ? 1 : 0;
  int b6 = ((64&b) == 64) ? 1 : 0;
  int b7 = ((128&b) == 128) ? 1 : 0;
  return b0+b1+b2+b3+b4+b5+b6+b7;
}


typedef unsigned char bucket;

int main() {
  int n = 2;
  int m = 2;
  buckets cur;
  cur.n = (1<<(m*4)) - 1;
  int count = 0;
  for (; cur.n != 0; cur.n--) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
      sum += count_bits(cur.bucket[i]);
    }
    if (sum == n) {
      count += 1;
    }
  }
  printf("%d\n", count);
}
