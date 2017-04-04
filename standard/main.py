import webapp2
import jinja2

from models import PandasText

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates', ),
)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        notes = PandasText.query().fetch()
        template = JINJA_ENV.get_template('index.html')
        self.response.write(template.render(notes=notes))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
