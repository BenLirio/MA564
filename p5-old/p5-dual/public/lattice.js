
genDualBasis = basis => {
  let {x,y} = basis
  let v = -x/y
  let w = -(x*v)/y
  return {x:v,y:w}
}

drawDualBasis = basis => {
  let b0 = genDualBasis(basis[0])
  let b1 = genDualBasis(basis[1])
  drawBasis([b0,b1])
}

basisUsing = env => basis => {
  DoIf(stroke, env('stroke'))
  DoIf(strokeWeight, env('strokeWeight'))
  basis.forEach( ({x,y}) => {
    _line(0,0,x,y)
    _point(x,y)
  })
}

drawLattice = basis => {
  stroke('black')
  strokeWeight(8)
  let n = 25
  for (let a0 = -n; a0 < n; a0++) {
    for (let a1 = -n; a1 < n; a1++) {
      let x = a0*basis[0].x + a1*basis[1].x
      let y = a0*basis[0].y + a1*basis[1].y
      _point(x,y)
    }
  }
}
