var Dat = require('dat-node')

// 1. Tell Dat where to download the files
Dat('../recordings/', {
  // 2. Tell Dat what link I want
  key: 'e6ce719856e903693d4211a1f7d96d89753b639b4a3fa564de6f2e0009717963' // (a 64 character hash from above)
}, function (err, dat) {
  if (err) throw err

  // 3. Join the network & download (files are automatically downloaded)
  dat.joinNetwork()
})
