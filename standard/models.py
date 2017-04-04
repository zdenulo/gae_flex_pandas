from google.appengine.ext import ndb


class PandasText(ndb.Model):
    text = ndb.StringProperty()
