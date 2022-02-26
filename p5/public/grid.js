
grid = env => {
  stroke('black')
  // Main grid lines
  strokeWeight(2)
  _line(-1,0,1,0)
  _line(0,1,0,-1)

  // Small grid lines
  strokeWeight(.25)
  let n = 10
  range(n)
    .map(x => (2*x-n)/n)
    .forEach(x => _line(-1,x,1,x))

  range(n)
    .map(x => (2*x-n)/n)
    .forEach(x => _line(x,1,x,-1))
}
