'use strict'

const Hapi = require('hapi')
const server = new Hapi.Server()

server.connection({
  host: 'localhost',
  port: Number(process.argv[2] || 8080)
})

server.route({
  path: '/',
  method: 'GET',
  handler: function(request, reply) {
    reply(`Hello hapi`)
  }
})

server.route({
  path: '/{name}',
  method: 'GET',
  handler: function(request, reply) {
    reply(`Hello ${encodeURIComponent(request.params.name)}`)
  }
})

server.start((err) => {
  if (err) { throw err }
  console.log(`Server running at ${server.info.uri}`)
})
