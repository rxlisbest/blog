import web
import os

urls = (
'/','index',
)
root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root, 'templates/'),cache=False
)

class index:
	def GET(self):
		return render.index()

app = web.application(urls, globals())
application = app.wsgifunc()
