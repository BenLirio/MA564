
let State = () => {
  this.basis = [{x:-.2,y:.5},{x:.9,y:.1}]
  this.selected =  None()
  this.setSelected = v => this.selected = v
  return this
}

let state = State()

setup = () => {
  createCanvas(N,N)
}

draw = () => {
  DoIf(i => {
    state.basis[i].x = mousePos().x
    state.basis[i].y = mousePos().y
  }, state.selected)

  background(220)
  drawLattice()
  drawGrid()
  drawBasis()
  drawRect()
}

mousePressed = () => {
  let {basis,setSelected} = state
  let dists = basis
    .map( ({x,y}) => dist(mousePos().x,mousePos().y,x,y))
  let bound = .1
  let close = x => x < bound
  let findClosest = ({cd,ci},d,i) => d <= cd ? ({cd:d,ci:Some(i)}) : ({cd,ci})
  let closest = dists.reduce(findClosest, {cd:bound,ci:None()}).ci
  setSelected(closest)
}

mouseReleased = () => {
  state.setSelected(None())
}
