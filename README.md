# reminder-service
initial commit - 6/19/22 1:27 PM EST  
bar met at - 6/19/22 2:22 PM EST  

## Instructions to run
The easiest way to run this application is to leverage docker-compose.  You can run:  
`docker-compose up -d`

Then query the application with curl, for example using the commands provided in the prompt:   
```
curl -H"Content-Type: application/json" -XPOST -d '{"time": "07:30", "message": "hello world"}' http://localhost/api/reminders
```
`curl http://localhost/api/reminders`  

If you must run it with docker alone, use the following commands:  
```
docker network create app-tier  
docker run -d --rm --name redis --network app-tier redis:alpine  
docker build -t reminders:latest .  
docker run -d --rm -p 80:5000 --network app-tier reminders:latest  
```  

## Developer notes  
* Test suite can be found in `reminders_test.py` with commentary around other tests I might have run with more time  
* This implementation uses a redis container backend, so as long as the redis container is not destroyed, the data survives a restart of the application  