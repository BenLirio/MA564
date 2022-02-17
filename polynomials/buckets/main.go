package main
import (
  "os"
  "bytes"
  "fmt"
)

func check(e error) {
  if e != nil {
    panic(e)
  }
}
type Buckets []int

func CreateBuckets(n int, m int) Buckets {
  buckets := make(Buckets, n)
  buckets[len(buckets)-1] = m
  return buckets
}

func (buckets Buckets) Move(src, dst, amt int) {
  if src == dst { return }
  if buckets[src] < amt {
    panic("Not enough to move")
  } else {
    buckets[src] -= amt
    buckets[dst] += amt
  }
}

func (buckets Buckets) Next() bool {
  for i := 1; i < len(buckets); i++ {
    if buckets[i] > 0 {
      buckets.Move(0, i-1, buckets[0])
      buckets.Move(i, i-1, 1)
      return true
    }
  }
  return false
}

func main() {
  N := 14
  M := 14
  table := make([][]int, N)
  for i := 0; i < len(table); i++ {
    table[i] = make([]int, M)
  }
  for n := 1; n < N; n++ {
    for m := 0; m < M; m++ {
      buckets := CreateBuckets(n,m)
      i := 1
      for buckets.Next() {
        i += 1
      }
      table[n][m] = i
    }
  }
  if table[2][2] != 3 {
      fmt.Printf("n=%d m=%d = %d, got %d\n", 2, 2, 3, table[2][2])
  }
  if table[3][2] != 6 {
      fmt.Printf("n=%d m=%d = %d, got %d\n", 2, 2, 6, table[3][2])
  }
  if table[3][3] != 10 {
      fmt.Printf("n=%d m=%d = %d, got %d\n", 2, 2, 10, table[3][3])
  }
  f, err := os.Create("combination.csv")
  check(err)
  defer f.Close()
  var buffer bytes.Buffer
  for i := 0; i < len(table); i++ {
    for j := 0; j < len(table[i]); j++ {
      buffer.WriteString(fmt.Sprintf("%d", table[i][j]))
      if j+1 != len(table[i]) {
        buffer.WriteString(",")
      }
    }
    buffer.WriteString("\n")
  }
  f.Write(buffer.Bytes())
}
