import flask
import json

api = flask.Blueprint('api', __name__, template_folder='templates')


@api.route('/api/v1/smoke/<drug>', methods=['SMOKE'])
def smoke_api(drug):
    if drug != 'cocaine' and drug != 'meth':
        msg = {'message': f'what is {drug}?'}
        return flask.Response(json.dumps(msg), status=200, mimetype='application/json')
    if flask.request.method == 'SMOKE':
        with open('backend/db.json', 'r') as f: smokes = json.load(f)
        smokes[drug] += 1
        with open('backend/db.json', 'w') as f: json.dump(smokes, f)
        msg = {'message': 'Smokin till the end of time...'}
        return flask.Response(json.dumps(msg), status=200, mimetype='application/json')

@api.route('/api/v1/drugs', methods = ['HOWMANYNIGGASSMOKIN'])
def get_drugs_api():
    if flask.request.method == 'HOWMANYNIGGASSMOKIN':
        with open('backend/db.json', 'r') as f: smokes = json.load(f)
        return flask.Response(json.dumps(smokes), status=200, mimetype='application/json')