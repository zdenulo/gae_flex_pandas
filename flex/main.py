import os

import webapp2
import pandas as pd
import numpy as np
from webapp2_extras import routes

from google.cloud import datastore

client = datastore.Client(project=os.environ['APP_ID'])


class PandasHandler(webapp2.RequestHandler):
    def get(self):
        s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
        df = s.to_frame()
        html = df.to_html()
        key = client.key('PandasText')
        entity = datastore.Entity(key=key)
        entity['text'] = html

        client.put(entity)
        self.response.write(html)


app = webapp2.WSGIApplication([
    routes.PathPrefixRoute('/pandas', [
        webapp2.Route('/', PandasHandler),
    ])
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8081')


if __name__ == '__main__':
    main()
