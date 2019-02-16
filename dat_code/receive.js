var Dat = require('dat-node')

// 1. Tell Dat where to download the files
Dat('./recordings/', {
  // 2. Tell Dat what link I want to sync with
  key: 'f1877ad69194f200226ac9f66c679acd0e11c4278a48b69fb6042680767c5ee0' // (a 64 character hash from above)
}, function (err, dat) {
  if (err) throw err

  // 3. Join the network & download (files are automatically downloaded)
  dat.joinNetwork()
})
