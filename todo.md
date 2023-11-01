## TODO notes

- Can we use a database? What for? SQL or NoSQL?
  - With infinite budget, I would go for primary PostgreSQL database into which to download this information on a daily basis and an ElasticSearch secondary database for handling the search.
  - On a limited budget, since the content of gists have a chance of changing, the only viable storage option would be short term cache like storing the information on REDIS and expiring it after a fixed period.
- How can we protect the api from abusing it?
  - Since there is no way to authenticate and identify the origin behind each request according to the current code, we can set rate limits on the web server(like Nginx) on an IP level to ensure one user does not make too many calls within the same time period.
  - If we can authenticate the requests using access tokens like an api key or a JWT, we can set rate limits on the access token level.
  - In either of the above workflows, sending out an alert when we notice a user consistently exceeding the rate limit will help identify such issues earlier.
- How can we deploy the application in a cloud environment?
  - I have only deployed applications on Heroku and Fly.io, and that was using the tutorials they have provided.
  - In either of these cases, it was with Dockerfile, so as to isolate the environment the application needs to run in.
- How can we be sure the application is alive and works as expected when deployed into a cloud environment?
  - we can setup a montoring system using tools like `Pingdom` to hit an endpoint like `/ping` to check if the application server is still receiving requests.
  - For performance, we can use tools like `New Relic` to monitor and benchmark the individual requests and analyse the logs. 