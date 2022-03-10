N = 800
MaxQ = 17
intervals = 100
bound = 0.05
let state 
loc = x => ((x+1)/2)*N
loci = x => ((x/N)*2)-1
m = () => ({x:loci(mouseX),y:-loci(mouseY)})

S = f => (...args) => {
  f(...args.map((arg,i) => {
    if (i%2 == 0) {
      return loc(arg)
    } else {
      return loc(-arg) 
    }
  })
  )
}

U = (...cs) => f => state => {
  args = cs.reduce((acc,c) => {
    acc[c] = state[c]
    return acc
  }, {})
  f(args)(state)
}
C = v => _ => v

J = (...elems) => state => elems.forEach(elem => elem(state))

M = (...props) => (...ds) => elem => state => {
  if (props.length != ds.length) { throw 'M: props and ds must be same length' }
  state = {...state}
  for(let i = 0; i < props.length; i++) {
    state[props[i]] = ds[i](state[props[i]])
  }
  elem(state)
}
MC = props => elem => state => {
  state = {...state}
  for (const [key,value] of Object.entries(props)) {
    state[key] = value
  }
  elem(state)
}
P = elem =>
  U('_fill','_strokeWeight','_stroke')( ({_strokeWeight,_fill,_stroke}) => {
    strokeWeight(_strokeWeight)
    fill(_fill)
    stroke(_stroke)
    return elem
  })

// alter state
//A = elem => state => elem({...state, x: state.x + 100})

// terminal
Line = P(
  ({x1,y1,x2,y2}) => S(line)(x1,y1,x2,y2)
)
Quad = P(
  ({x1,y1,x2,y2,x3,y3,x4,y4}) => S(quad)(x1,y1,x2,y2,x3,y3,x4,y4)
)
Point = P(
  ({x,y}) => S(point)(x,y)
)
Circle = P(
  ({x,y,d}) => circle(loc(x),loc(-y),d*N)
)

// Non-terminal
Grid = 
  U('gap','showGrid','origin')
  ( ({gap,showGrid,origin:{x,y}}) => {
    if (!showGrid) { return J() }
    tLine = M('_stroke')(c=> color(red(c),green(c),blue(c),80))(Line)
    hLine = y => MC({x1:-1,x2:1,y1:y,y2:y})(tLine)
    vLine = x => MC({x1:x,x2:x,y1:-1,y2:1})(tLine)
    dy = (y+1)%gap
    dx = (x+1)%gap
    hLines = [...Array(1+ceil(2/gap))].map((_,i) => hLine(dy+i*gap-1))
    vLines = [...Array(1+ceil(2/gap))].map((_,i) => vLine(dx+i*gap-1))
    return J(
      ...vLines,
      ...hLines,
      M('_strokeWeight')(sw=>sw+2)(hLine(y)),
      M('_strokeWeight')(sw=>sw+2)(vLine(x)),
    )
  })

LatticeFundementalRegion =
  U('showFundementalRegion', 'basis','origin')
  ( ({showFundementalRegion,basis,origin:{x,y}}) => {
    if (!showFundementalRegion) { return J() }
    _fill = color('gray')
    _fill = color(red(_fill),green(_fill),blue(_fill),128)
    let props = {
      _fill: _fill,
      _strokeWeight: 0,
      x1: x,
      y1: y,
      x2: x+basis[0].x,
      y2: y+basis[0].y,
      x3: x+basis[1].x+basis[0].x,
      y3: y+basis[1].y+basis[0].y,
      x4: x+basis[1].x,
      y4: y+basis[1].y,
    }
    return MC(props)(Quad)
  })

BasisModQ =
  U('Q','showBasisModQ','basis','origin')
  ( ({Q,showBasisModQ,basis,origin:{x,y}}) => {
    if (!showBasisModQ) { return J() }
    modLine = MC({
      _stroke:color(200,50,50,128),
      _strokeWeight:2,
    })(Line)
    range = n => [...Array(n)].map((_,i)=>i)
    vLines = range(Q)
      .map(i=>i/Q)
      .map(v => ({x1:x+v*basis[0].x, y1:y+v*basis[0].y}) )
      .map( b => ({...b,x2:b.x1+basis[1].x, y2:b.y1+basis[1].y}))
      .map(props => MC(props)(modLine))
    hLines = range(Q)
      .map(i=>i/Q)
      .map(v => ({x1:x+v*basis[1].x, y1:y+v*basis[1].y}) )
      .map( b => ({...b,x2:b.x1+basis[0].x, y2:b.y1+basis[0].y}))
      .map(props => MC(props)(modLine))

    return J(
      ...vLines,
      ...hLines,
    )
  })

Basis =
  U('showBasis','basis','origin')
  ( ({showBasis,basis,origin:{x,y}}) => {
    if (!showBasis) { return J() }
    basisLine = MC({
      _stroke:color('blue'),
      _strokeWeight:3,
    })(Line)
    fromOrigin = MC({x1:x,y1:y})(basisLine)
    return J(
      MC({x2:x+basis[0].x,y2:y+basis[0].y})(fromOrigin),
      MC({x2:x+basis[1].x,y2:y+basis[1].y})(fromOrigin),
    )
  })

LatticeCoverCircle =
  U('showLatticeCover','coveringRadius')
  ( ({showLatticeCover,coveringRadius}) => {
    if (!showLatticeCover) { return J() }
    coverCirc = MC({_fill:color(200,0,0,50),_strokeWeight:0,d:coveringRadius})(Circle)
    return coverCirc
  })

LatticePoint = 
  U('showLatticePoints')
  ( ({showLatticePoints}) => {
    if (!showLatticePoints) { return J() }
    return M('_strokeWeight','_stroke')(sw=>sw+8,_=>color('black'))(Point)
  })

Lattice =
  U('basis','origin')
  ( ({showLattice,basis,origin:{x,y}}) => {
    let n = 10
    points = Array(n*4)
    for (let i = -n; i < n; i++) {
      for (let j = -n; j < n; j++) {
        points[(i+n)*(n*2)+(j+n)] = {
          x: x+ i*basis[0].x + j*basis[1].x,
          y: y+ i*basis[0].y + j*basis[1].y,
        }
      }
    }
    return J(
        ...points.map(cords => MC(cords)(LatticePoint)),
        ...points.map(cords => MC(cords)(LatticeCoverCircle)),
      )
  })

let coveringRadiusSldr
let gridSldr
let QSldr
setup = () => {
  createCanvas(N,N)

  state = {
    _strokeWeight: 1,
    _fill: color('black'),
    _stroke: color('black'),
    coveringRadius: .1,
    showGrid: true,
    showLatticePoints: true,
    showLatticeCover: false,
    showBasisModQ: false,
    showBasis: true,
    showFundementalRegion: false,
    origin: {x:-.5111,y:-.522},
    basis: [{x:.4,y:.2},{x:-.1,y:.3}],
    selected: -1,
    Q: 13,
    gap: 0.1,
  }

  createCheckbox('Grid', state.showGrid).changed( ({target:{checked}}) => state.showGrid = checked)
  gridSldr = createSlider(1,intervals,.15*intervals)
  createCheckbox('Basis', state.showBasis).changed( ({target:{checked}}) => state.showBasis = checked)
  createCheckbox('Fundemental Region', state.showFundementalRegion).changed( ({target:{checked}}) => state.showFundementalRegion = checked)
  createCheckbox('Lattice Points', state.showLatticePoints).changed( ({target:{checked}}) => state.showLatticePoints = checked)
  createCheckbox('Basis Mod Q', state.showBasisModQ).changed( ({target:{checked}}) => state.showBasisModQ = checked)
  QSldr = createSlider(0,MaxQ,ceil(MaxQ/4))
  createCheckbox('Lattice Cover', state.showLatticeCover).changed( ({target:{checked}}) => state.showLatticeCover = checked)
  coveringRadiusSldr = createSlider(0,intervals,intervals/6)
}

mousePressed = () => {
  let {origin} = state
  close = state.basis.map( ({x,y}, i) => {
    if (dist(origin.x + x,origin.y + y,m().x,m().y) < bound) {
      return i
    }
    return -1
  }).filter(idx => idx >= 0)
  if (close.length > 0) {
    state.selected = close[0]
  } else {
    state.selected = -1
  }
}
mouseReleased = () => {
  state.selected = -1
}

draw = () => {
  state.coveringRadius = (coveringRadiusSldr.value()/intervals)
  state.Q = (QSldr.value())
  state.gap = (gridSldr.value()/intervals)
  let {origin} = state
  if (state.selected != -1) {
    state.basis[state.selected].x = m().x - origin.x
    state.basis[state.selected].y = m().y - origin.y
  }
  background(220)
  Grid(state)
  LatticeFundementalRegion(state)
  Basis(state)
  BasisModQ(state)
  Lattice(state)
}
