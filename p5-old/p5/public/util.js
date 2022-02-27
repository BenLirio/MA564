function Option (v,t) { this.v = v; this.t = t }
None = () => new Option(null,false)
Some = v => new Option(v,true)
DoIf = (f,{v,t}) => { if (t) { f(v) } }

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
_quad = (x1,y1,x2,y2,x3,y3,x4,y4) => quad(locx(x1), locy(y1), locx(x2), locy(y2), locx(x3), locy(y3),locx(x4),locy(y4))
_text = (s,x1,y1) => text(s,locx(x1),locy(y1))

let mousePos = () => ({x:locx_inv(mouseX),y:locy_inv(mouseY)})
