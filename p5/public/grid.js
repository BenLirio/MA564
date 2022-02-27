
initGrid = () => {
  return () => {
    createCanvas(800,800)
  }
}


gridBackground =
  bind(lookup('background'))
  (bg => res(background(bg)))

Eline = (x1,y1,x2,y2) => _ => {
  res(Line(x1,y1,x2,y2))
}

  

/*
gridMain = env => {
  stroke('black')

  // Small grid lines
  strokeWeight(.25)
  let n = 10
  range(n)
    .map(x => (2*x-n)/n)
    .forEach(x => _line(-1,x,1,x))

  range(n)
    .map(x => (2*x-n)/n)
    .forEach(x => _line(x,1,x,-1))
}
*/

//allGrid = fork(initGrid)

//grid = pair(gridBackground, Eline(1,0,-1,0))

grid = _env => {
  Line(1,0,-1,0)
  return () => {}
}
