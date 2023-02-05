class Point {
  constructor(state,x,y) {
    this.state = state
    this.x = x
    this.y = y
    this._x = ((this.x+1)/2)*state.N
    this._y = ((this.y+1)/2)*state.N
  }
}

class Line {
  constructor(state,p1,p2) {
    this.state = state
    this.p1 = p1
    this.p2 = p2
  }
  draw() {
    let {p1,p2} = this
    line(p1._x,p1._y,p2._x,p2._y)
  }
}

class Grid {
  constructor(state) {
    this.state = state
    this.hLine = new Line(this.state,new Point(this.state,0,1),new Point(this.state,0,-1))
    this.vLine = new Line(this.state,new Point(this.state,1,0),new Point(this.state,-1,0))
  }
  draw() {
    this.hLine.draw()
    this.vLine.draw()
  }
}

class Canvas {
  constructor(N) {
    this.state = {
      N: N,
    }
    createCanvas(this.state.N, this.state.N)
    this.grid = new Grid(this.state)
  }
  draw() {
    background(220)
    this.grid.draw()
  }
}

setup = () => {
  canvas = new Canvas(800)
}

draw = () => {
  canvas.draw()
}
