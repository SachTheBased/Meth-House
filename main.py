import flask
import views
import api

app = flask.Flask('Meth')
app.register_blueprint(views.views)
app.register_blueprint(api.api)

app.run('0.0.0.0', port = 6900)