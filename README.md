
# Simple example how to use together Google App Engine Standard and Flexible Environment in one project.

Lets imagine you have existing GAE application. And since Pandas library is not available in GAE Standard, we will create
another service (module) where we will do some work with Pandas and save data into Datastore and then fetch that data
in GAE standard.

few comments:
- in both services we are using webapp2 framework, they both run on Python 2
- in GAE Flex we creating entities in Datastore with client library
- with dispach.yaml file we are routing GAE Flex service to url /pandas/

you can run GAE Flex part locally by going into folder `flex` and run `python main`  (before that you need to install of 
course requirements.txt (best in virtual env)) 

To deploy everything at once
`gcloud app deploy dispatch.yaml flex/app.yaml standard/app.yaml --verbosity=debug --promote`

More info in this link [https://www.the-swamp.info/blog/google-app-engine-flexible/](https://www.the-swamp.info/blog/google-app-engine-flexible/)

If you want to receive weekly news, info, articles atc. regarding Google Cloud Platform, subscribe here [https://www.the-swamp.info/newsletter/](https://www.the-swamp.info/newsletter/)

