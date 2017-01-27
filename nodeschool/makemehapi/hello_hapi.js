'use strict'

const Hapi = require('hapi')
const server = new Hapi.Server()

function handlerFn(request, reply) {
  reply('Hello hapi')
}

server.connection({
  host: 'localhost',
  port: Number(process.argv[2] || 8080)
})

server.route({
  path: '/',
  method: 'GET',
  handler: handlerFn
})

server.start((err) => {
  if (err) { throw err }
  console.log(`Server running at ${server.info.uri}`)
})
