var Dat = require('dat-node')

Dat('../recordings', function (err, dat) {
  if (err) throw err

  // 2. Import the files
  var progress = dat.importFiles({watch: true})

  progress.on('put', function (src, dest) {
    console.log('Importing ', src.name, ' into archive')
  })

  // 3. Share the files on the network!
  dat.joinNetwork()

  // (And share the link)
  console.log('My Dat link is: dat://', dat.key.toString('hex'))
})
