var Dat = require('dat-node')

// 1. Tell Dat where to download the files
Dat('./recordings/', {
  // 2. Tell Dat what link I want to sync with
  key: '' // (a 64 character hash from above)
}, function (err, dat) {
  if (err) throw err

  // 3. Join the network & download (files are automatically downloaded)
  dat.joinNetwork()
})
