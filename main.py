# run: dev_appserver.py app.yaml
import webapp2
import jinja2
import os

# Dyanmic things => use main.py to add in page links

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template("templates/start.html")
        self.response.write(template.render()) #the response

class JumpIn(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template("templates/jumpin.html")
        self.response.write(template.render()) #the response

class Run(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template("templates/run.html")
        self.response.write(template.render()) #the response

class Accept(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/accept.html")
        self.response.write(template.render()) #the response

class Reject(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/reject.html")
        self.response.write(template.render()) #the response

class Email(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/email.html")
        self.response.write(template.render()) #the response

app = webapp2.WSGIApplication([
    ("/", MainPage), #this maps the root url to the Main Page Handler
    ("/jumpin", JumpIn),
    ("/run", Run),
    ("/accept", Accept),
    ("/reject", Reject),
    ("/email", Email),
], debug=True)
