import web
import os
from web import form
import datetime

db = web.database(dbn="mysql", db="blog_schema",host="localhost", port=3306, user="test", pw="123")

urls = (
'/','index',
'/add','add',
)
root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root, 'templates/'),cache=False
)

class index:
	def GET(self):
		blog = db.select('blog')
		blog_class = db.select('blog_class')
		bcs = dict()
		for bc in blog_class:
			bcs[bc["bc_id"]] = bc["bc_title"]
		data = [blog, bcs]
		return render.index(data)

class add:
	def GET(self):
		return render.index()

class add:
	def GET(self):
		blog_class = db.select('blog_class')
		data = [blog_class]
		return render.add(data)
	def POST(self):
		post = web.input()
		db.insert('blog',
			bc_id=post.bc_id,
			b_title=post.b_title,
			b_content=post.b_content,	
			b_createtime=datetime.datetime.now(),	
		)
		return render.index()

app = web.application(urls, globals())
application = app.wsgifunc()
