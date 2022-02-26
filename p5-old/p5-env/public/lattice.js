drawBasis = () => {
  state.basis.forEach( ({x,y}) => {
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
