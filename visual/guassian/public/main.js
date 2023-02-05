let RENDER_OP
let pg;
let n = 8

function setup(){
  RENDER_OP = WEBGL
  createCanvas(800, 800, RENDER_OP);
  pg = createGraphics(n,n);
}
function draw(){
  if (RENDER_OP == p5) {
    translate(400, 400)
    scale(1,-1)
  }
  background(0)
  fill(255,255,255,128)
  rect(-150,-150,200,200)

  push()
  pg.strokeWeight(0)
  pg.loadPixels()
  let idx = 0
  for (let x = -8; x < 8; x++) {
    for (let y = -8; y < 8; y++) {
      pg.pixels[idx+0] = 255
      pg.pixels[idx+1] = 0
      pg.pixels[idx+2] = 0
      pg.pixels[idx+3] = 255*Math.exp(-PI*dist(0,0,x/n,y/n))
      idx += 4
    }
  }
  pg.updatePixels()
  texture(pg)
  strokeWeight(0)
  ellipse(-50,-50,200,200)
  pop()

  fill(255,255,255,128)
  rect(0,0,200,200)

}
