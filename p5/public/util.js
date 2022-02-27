ERROR = 1
VALID = 2
function Result (v,t) { this.v = v; this.t = t }
None = () => new Result(null,ERROR)
Some = v => new Result(v,VALID)
res = v => _env => Some(v)
err = () => _env => None()

update = c => d => env => {
  let {v,t} = c(env)
  if (t != ERROR) {
    return d(v)
  } else {
    return None()
  }
}
bind = c => f => env => {
  let {v,t} = c(env)
  if (t != ERROR) {
    return f(v)(env)
  } else {
    return None()
  }
}
using = c => d => env => {
  let {v,t} = c(env)
  if (t != ERROR) {
    return d(v)
  } else {
    return None()
  }
}

emptyEnv = _ => None()
extendEnv = v => env => k => {
  if (v.hasOwnProperty(k)) { return Some(v[k]) }
  return env(k)
}
lookup = k => env => env(k)
updateGlobalEnv = ext => env = extendEnv(ext)(env)
let env = emptyEnv

applyGlobalEnv = (...elems) => () => elems.forEach(elem => elem(env)())

baseEnv = updateGlobalEnv({
  basis: [{x:-.2,y:.5},{x:.9,y:.1}],
  selected: None(),
  N: 800,
  stroke: 'black',
  background: 220,
})


loc = x => ((x+1)/2)*N
locx = x => loc(x)
locy = y => loc(-y)
loc_inv = x => ((x/N)*2) - 1
locy_inv = y => -loc_inv(y)
locx_inv = x => loc_inv(x)

range = (n) => [...Array(n).keys()]
_point = (x,y) => point(locx(x), locy(y))
Line = (x1,y1,x2,y2) => _env => res(line(locx(x1), locy(y1),locx(x2), locy(y2)))
_triangle = (x1,y1,x2,y2,x3,y3) => triangle(locx(x1), locy(y1), locx(x2), locy(y2), locx(x3), locy(y3))

let mousePos = () => ({x:locx_inv(mouseX),y:locy_inv(mouseY)})
