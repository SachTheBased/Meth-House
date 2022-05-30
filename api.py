import flask
import json

api = flask.Blueprint('api', __name__, template_folder='templates')


@api.route('/api/v1/smoke', methods=['SMOKE', 'HOWMANYNIGGASSMOKIN'])
def smoke_api():
    if flask.request.method == 'SMOKE':
        with open('backend/db.json', 'r') as f: smokes = json.load(f)
        smokes["Meth"] += 1
        with open('backend/db.json', 'w') as f: json.dump(smokes, f)
        return flask.Response("{'message':'Smokin till the end of time...'}", status=200, mimetype='application/json')
    elif flask.request.method == 'HOWMANYNIGGASSMOKIN':
        with open('backend/db.json', 'r') as f: smokes = json.load(f)
        return flask.Response(json.dumps(smokes), status=200, mimetype='application/json')