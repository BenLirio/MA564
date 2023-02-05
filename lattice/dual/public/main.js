const width = 500
const height = 500

loc = (x) => x*width + width/2

init = () => {
  const backgroundColor = color(200,200,200)
  createCanvas(width,height)
  background(backgroundColor)
  strokeWeight(5)
}

abs = (x) => {
  if(x > 0) { return x }
  return -x
}

drawLattice = (basis) => {
  for (let a0 = 0;;a0++) {
    let x1 = a0*basis[0][0]
    let y1 = a0*basis[0][1]
    for (let a1 = 0;;a1++) {
      let x2 = x1 + a1*basis[1][0]
      let y2 = y1 + a1*basis[1][1]
      if (abs(x2) > 1 || abs(y2) > 1) {
        break
      }
      point(loc(x2),loc(y2))
    }
    for (let a1 = -1;;a1--) {
      let x2 = x1 + a1*basis[1][0]
      let y2 = y1 + a1*basis[1][1]
      if (abs(x2) > 1 || abs(y2) > 1) {
        break
      }
      point(loc(x2),loc(y2))
    }
    if (abs(x1) > 1 || abs(y1) > 1) {
      break
    }
  }
  for (let a0 = -1;;a0--) {
    let x1 = a0*basis[0][0]
    let y1 = a0*basis[0][1]
    for (let a1 = 0;;a1++) {
      let x2 = x1 + a1*basis[1][0]
      let y2 = y1 + a1*basis[1][1]
      if (abs(x2) > 1 || abs(y2) > 1) {
        break
      }
      point(loc(x2),loc(y2))
    }
    for (let a1 = -1;;a1--) {
      let x2 = x1 + a1*basis[1][0]
      let y2 = y1 + a1*basis[1][1]
      if (abs(x2) > 1 || abs(y2) > 1) {
        break
      }
      point(loc(x2),loc(y2))
    }
    if (abs(x1) > 1 || abs(y1) > 1) {
      break
    }
  }
}

let slider
setup = () => {
  init()
  basis = [
    [.1,0],
    [0,.1]
  ]
  slider = createSlider(0,100,0)
  drawLattice(basis)
}

let step = 0
draw = () => {
  clear()
  b0 = slider.value()/50 -1
  basis = [
    [b0,0],
    [0,.1]
  ]
  drawLattice(basis)
}
