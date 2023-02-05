const express = require('express')
const app = express()
const path = require('path')

app.use(express.static('public'))

app.get('/', (req, res) => {
  res.send("test")
})
app.listen(80)
console.log('Listening on port 80')
