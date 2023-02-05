N = 800
_WEBGL = true
intervals = 100
bound = 0.05
let state 
let loc
if (_WEBGL) {
  loc = x => ((x)/2)*N
} else {
  loc = x => ((x+1)/2)*N
}

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
Point = P(
  ({x,y}) => S(point)(x,y)
)
Circle = P(
  ({x,y,d}) => {
    shader(simpleShader)
    //circle(loc(x),loc(-y),d*N)
    beginShape()
    vertex(loc(x),loc(-y),-100)
    vertex(loc(x-.1),loc(-y),-100)
    vertex(loc(x),loc(-y-.1),-100)
    endShape()
    resetShader()
  }
)

// Non-terminal
Grid = 
  U('showGrid','origin')
  ( ({showGrid,origin:{x,y}}) => {
    if (!showGrid) { return J() }
    fromOrigin = MC({x1:x,y1:y})(Line)
    return J(
      MC({x2:x-1,y2:y})(fromOrigin),
      MC({x2:x+1,y2:y})(fromOrigin),
      MC({x2:x,y2:y-1})(fromOrigin),
      MC({x2:x,y2:y+1})(fromOrigin),
    )
  })

Basis =
  U('showBasis','basis','origin')
  ( ({showBasis,basis,origin}) => {
    if (!showBasis) { return J() }
    fromOrigin = M('x1','y1')(...[origin.x,origin.y].map(C))(Line)
    return J(
      M('x2','y2')(...[basis[0].x,basis[0].y].map(C))(fromOrigin),
      M('x2','y2')(...[basis[1].x,basis[1].y].map(C))(fromOrigin),
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
    return M('_strokeWeight')(sw=>sw+5)(Point)
  })


Lattice =
  U('basis','origin')
  ( ({showLattice,basis,origin}) => {
    let n = 10
    points = Array(n*4)
    for (let i = -n; i < n; i++) {
      for (let j = -n; j < n; j++) {
        points[(i+n)*(n*2)+(j+n)] = {
          x: i*basis[0].x + j*basis[1].x,
          y: i*basis[0].y + j*basis[1].y,
        }
      }
    }
    return J(
        ...points.map(cords => MC(cords)(LatticePoint)),
        ...points.map(cords => MC(cords)(LatticeCoverCircle))
      )
  })

let simpleShader
let coveringRadiusSdr

preload = () => {
  simpleShader = loadShader('basic.vert', 'basic.frag');
}
setup = () => {
  if (_WEBGL) {
    createCanvas(N,N,WEBGL)
  } else {
    createCanvas(N,N)
  }

  state = {
    _strokeWeight: 1,
    _fill: color('black'),
    _stroke: color('black'),
    coveringRadius: .1,
    showGrid: true,
    showLatticePoints: true,
    showLatticeCover: true,
    showBasis: true,
    origin: {x:0,y:0},
    basis: [{x:.4,y:.2},{x:-.1,y:.3}],
    selected: -1,
  }

  createCheckbox('Grid', state.showGrid).changed( ({target:{checked}}) => state.showGrid = checked)
  createCheckbox('Basis', state.showBasis).changed( ({target:{checked}}) => state.showBasis = checked)
  createCheckbox('Lattice Points', state.showLatticePoints).changed( ({target:{checked}}) => state.showLatticePoints = checked)
  createCheckbox('Lattice Cover', state.showLatticeCover).changed( ({target:{checked}}) => state.showLatticeCover = checked)

  coveringRadiusSdr = createSlider(0,intervals,intervals/6)

}

mousePressed = () => {
  close = state.basis.map( ({x,y}, i) => {
    if (dist(x,y,m().x,m().y) < bound) {
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
  state.coveringRadius = (coveringRadiusSdr.value()/intervals)
  if (state.selected != -1) {
    state.basis[state.selected].x = m().x
    state.basis[state.selected].y = m().y
  }
  background(220)
  Grid(state)
  Basis(state)
  Lattice(state)
}
