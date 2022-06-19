# reminder-service
## initial commit - 6/19/22 1:27 PM EST
## bar met at - 6/19/22 2:22 PM EST

The easiest way to run this application is to leverage docker-compose.  You can run:
`docker-compose up -d`

Then query the application with curl, for example using the commands provided in the prompt:
`curl -H"Content-Type: application/json" -XPOST -d '{"time": "07:30", "message": "hello world"}' http://localhost/api/reminders`
`curl http://localhost/api/reminders`