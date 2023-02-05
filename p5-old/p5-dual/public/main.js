
let State = () => {
  this.basis = [{x:-.2,y:.5},{x:.9,y:.1}]
  this.selected =  None()
  this.setSelected = v => this.selected = v
  return this
}

let state = State()
let env = emptyEnv
let blue = env => extendEnv('stroke')('blue')(env)
let thick = env => extendEnv('strokeWeight')(4)(env)
wit = env => f => f(env)
comb = (...args) => base => args.reduce((acc,arg) => arg(acc),base)
show = (...args) => f => wit(comb(...args)(env))(f)

setup = () => {
  env = extendEnv('stroke')('black')(env)
  env = extendEnv('strokeWeight')(1)(env)
  createCanvas(N,N)
}

draw = () => {
  let {basis} = state
  DoIf(i => {
    basis[i].x = mousePos().x
    basis[i].y = mousePos().y
  }, state.selected)

  background(220)
  drawGrid()
  show(blue,thick)(basisUsing)(basis)
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
