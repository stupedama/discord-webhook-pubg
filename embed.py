import json

class Embed:
    def __init(self):
        pass

    def make_embed(self, link, title, image):
        inline = False
        return [{"title": title,
                 "description": link,
                 "thumbnail": {'url': image},
                 }]

