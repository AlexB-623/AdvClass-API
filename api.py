import justpy as jp
import definition
from documentation import About
import json

class Api:
    """Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        defined = definition.Definition(word).get()

        response = {
            "word":word,
            "definition":defined
        }

        wp.html = json.dumps(response)
        return wp

jp.Route("/api", Api.serve)
jp.Route("/about", About.serve)
jp.justpy()
