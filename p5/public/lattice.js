/*
trackMouseIfSelected =
  using(bind(lookup('selected'))
  (maybeSelected =>
    bind(lookup('basis'))
    (basis => {
      let {v:selected,t} = maybeSelected
      if (t != ERROR) {
        let basisp = [{x:0,y:0},{x:0,y:0}]
        basisp[0].x = basis[0].x
        basisp[1].x = basis[1].x
        basisp[0].y = basis[0].y
        basisp[1].y = basis[1].y
        basisp[selected].x = mousePos().x
        basisp[selected].y = mousePos().y
        return res({
          basis: basisp,
        })
      } else {
        return err()
      }
    })
  ))(updateGlobalEnv)

deselectBasis = using(_ => Some({selected: None()}))(updateGlobalEnv)

selectBasis =
  using(bind(lookup('basis'))
  (basis => {
    let dists = basis
      .map( ({x,y}) => dist(mousePos().x,mousePos().y,x,y))
    let bound = .1
    let close = x => x < bound
    let findClosest = ({cd,ci},d,i) => d <= cd ? ({cd:d,ci:Some(i)}) : ({cd,ci})
    let closest = dists.reduce(findClosest, {cd:bound,ci:None()}).ci
    return res({
      selected: closest,
    })
  }))(updateGlobalEnv)

basis =
  bind(lookup('basis'))
  (basis => 
    res(
      basis.forEach(({x,y}) => {
        stroke('blue')
        strokeWeight(2)
        _line(0,0,x,y)
        strokeWeight(10)
        _point(x,y)
      })
    )
  )

lattice = 
  bind(lookup('basis'))
  (basis => {
    strokeWeight(8)
    let n = 10
    for (let a0 = -n; a0 < n; a0++) {
      for (let a1 = -n; a1 < n; a1++) {
        let x = a0*basis[0].x + a1*basis[1].x
        let y = a0*basis[0].y + a1*basis[1].y
        _point(x,y)
      }
    }
    return res(None())
  })

allLattice = join(lattice,basis)
*/
