package main

import (
  "math"
  "fmt"
)

var mem [][]int
func monomial(n, m int) int {
  if m == 1 { return 1 }
  if n == 1 { return m }
  val := mem[n-1][m-1]
  if val != 0 { return val }
  val = monomial(n-1,m) + monomial(n,m-1)
  mem[n-1][m-1] = val
  return mem[n-1][m-1]
}

func main() {
  n := 10
  m := 4
  mem = make([][]int, n)
  for i := 0; i < n; i++ {
    mem[i] = make([]int, m)
  }
  total := int(math.Pow(float64(m),float64(n)))
  monomials := monomial(n,m)
  fmt.Printf("Total: %d\nMonomials: %d\nCancelled: %d\n", total, monomials, total-monomials)
}
