
setup = () => {
  createCanvas(N,N)
}

trackMouseIfSelected =
  bind(lookup('selected'))
  (maybeSelected =>
    bind(lookup('basis'))
    (basis => {
      let {v:selected,t} = maybeSelected
      if (t) {
        let basisp = basis
        basisp[selected].x = mousePos().x
        basisp[selected].y = mousePos().y
        return res(extendEnv({
          basis: basisp,
        }))
      } else {
        return err()
      }
    })
  )

draw = () => {
  background(220)
  let tasks = [
    basis,
    lattice,
    grid,
    trackMouseIfSelected,
  ]

  tasks.forEach(run)
}

selectBasis =
  bind(lookup('basis'))
  (basis => {
    let dists = basis
      .map( ({x,y}) => dist(mousePos().x,mousePos().y,x,y))
    let bound = .1
    let close = x => x < bound
    let findClosest = ({cd,ci},d,i) => d <= cd ? ({cd:d,ci:Some(i)}) : ({cd,ci})
    let closest = dists.reduce(findClosest, {cd:bound,ci:None()}).ci
    return res(extendEnv({
      selected: closest,
    }))
  })

mousePressed = () => {
  let tasks = [
    using(selectBasis)(updateGlobalEnv),
  ]
  tasks.forEach(run)
}

deselectBasis = _ => Some(extendEnv({selected: None()}))

mouseReleased = () => {
  let tasks = [
    using(deselectBasis)(updateGlobalEnv),
  ]
  tasks.forEach(run)
}
