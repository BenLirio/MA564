function Option (v,t) { this.v = v; this.t = t }
None = () => new Option(null,false)
Some = v => new Option(v,true)
DoIf = (f,{v,t}) => { if (t) { f(v) } }

drawWithEnv = elems => env => elems.map(elem => elem(env))

bind = c => f => env => {
  let {v,t} = c(env)
  if (t) {
    return f(v)(env)
  } else {
    return None()
  }
}

res = v => _env => Some(v)
err = () => _env => None()

update = c => d => env => {
  let {v,t} = c(env)
  if (t) {
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

let env = extendEnv({
  basis: [{x:-.2,y:.5},{x:.9,y:.1}],
  selected: None(),
})(emptyEnv)

updateGlobalEnv = envp => env = envp(env)

run = f => f(env)
using = c => d => env => {
  let {v,t} = c(env)
  if (t) {
    return d(v)
  } else {
    return None()
  }
}

loc = x => ((x+1)/2)*N
locx = x => loc(x)
locy = y => loc(-y)
loc_inv = x => ((x/N)*2) - 1
locy_inv = y => -loc_inv(y)
locx_inv = x => loc_inv(x)

range = (n) => [...Array(n).keys()]
_point = (x,y) => point(locx(x), locy(y))
_line = (x1,y1,x2,y2) => line(locx(x1), locy(y1),locx(x2), locy(y2))
_triangle = (x1,y1,x2,y2,x3,y3) => triangle(locx(x1), locy(y1), locx(x2), locy(y2), locx(x3), locy(y3))

let mousePos = () => ({x:locx_inv(mouseX),y:locy_inv(mouseY)})
