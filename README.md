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
* "What additional tooling would you use or recommend to create and maintain the code for real if it isn’t already included (testing, API tools, linting, build files etc.)?"  
  I would love to add more testing, specifically unit tests for edge cases as well as some integration / end-to-end API tests.  I would also add a swagger page.  Similarly, I'd like to add robust CI/CD around it to run these tests on all developer changes before going to production.  I'd also like to add static security analysis for underlying packages and the resulting docker images to check for vulnerabilities.  
* "Would it eventually be deployable to an orchestration platform such as Kubernetes or similar - what else would need to be provided to make this work?"
  I think it would work in its current state in an orchestration platform.  However, I might like to put a more robust data store in place in production, for example using AWS Elasticache for the backend so that we could do backups, automated replication and failover, etc.  That would, of course, require a refactor to how the app connects to the data backend.  
* "What are the most obvious missing technical requirements for the service and do you have some thoughts on those?"  
  It seems like a miss that the prompt doesn't make any requirement that these reminders be functional.  It seems odd to have a reminders app that can't act on the reminders.  Depending upon the functional requirements, I might change this app to register a job that can send reminders to the user via text/email/Slack/etc.  That job could be an EventBridge rule in AWS, a Job in k8s, or some other implementation.  
  It might also be nice to know what user to send such a reminder to, currently all users are registering to the same data store.  Depending on the requirement, we would need to refactor the code to write the objects such that we can identify the user who submitted the reminder.  
* I really enjoyed this challenge, thanks for the exercise.
* I have actually never written a Python -> Redis implementation before today, so this was a fun new thing to learn!  