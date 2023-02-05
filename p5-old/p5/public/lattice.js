drawRect = () => {
  x1 = 0
  y1 = 0
  x2 = state.basis[0].x
  y2 = state.basis[0].y
  x4 = state.basis[1].x
  y4 = state.basis[1].y
  x3 = x2 + x4
  y3 = y2 + y4
  area = x2*y4 + x4*y2
  fill(color(0,0,0,20))
  noStroke()
  _quad(x1,y1,x2,y2,x3,y3,x4,y4)
  fill('black')
  _text(Math.round(area*1000)/100, 0, 0)
}

drawBasis = () => {
  state.basis.forEach( ({x,y}) => {
    stroke('blue')
    strokeWeight(2)
    _line(0,0,x,y)
    strokeWeight(10)
    _point(x,y)
  })
}

drawLattice = () => {
  stroke('black')
  strokeWeight(8)
  let n = 25
  let basis = state.basis
  for (let a0 = -n; a0 < n; a0++) {
    for (let a1 = -n; a1 < n; a1++) {
      let x = a0*basis[0].x + a1*basis[1].x
      let y = a0*basis[0].y + a1*basis[1].y
      _point(x,y)
    }
  }
}
