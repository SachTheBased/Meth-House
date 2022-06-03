import websocket
import flask
import json

api = flask.Blueprint('api', __name__, template_folder='templates')
ws = websocket.WebSocket()
ws.connect('ws://127.0.0.1:9999')

@api.route('/api/v1/smoke/<drug>', methods=['SMOKE'])
def smoke_api(drug):
    if drug != 'cocaine' and drug != 'meth':
        msg = {'message': f'what is {drug}?'}
        return flask.Response(json.dumps(msg), status=404, mimetype='application/json')
    if flask.request.method == 'SMOKE':
        with open('backend/db.json', 'r') as f: smokes = json.load(f)
        if smokes['available'][drug] > 0:
            smokes['smoked'][drug] += 1
            smokes['available'][drug] -= 1
            with open('backend/db.json', 'w') as f: json.dump(smokes, f)
            ws.send(json.dumps({'type': 'smoke', 'drug': drug, 'secret_key': 'METH_HOUSE-9999'}))
            msg = {'message': 'Smokin till the end of time...'}
            return flask.Response(json.dumps(msg), status=200, mimetype='application/json')
        else:
            msg = {'message': 'Sorry we\'re out'}
            return flask.Response(json.dumps(msg), status=418, mimetype='application/json')

@api.route('/api/v1/drugs', methods = ['HOWMANYNIGGASSMOKIN'])
def get_drugs_api():
    if flask.request.method == 'HOWMANYNIGGASSMOKIN':
        with open('backend/db.json', 'r') as f: smokes = json.load(f)
        return flask.Response(json.dumps(smokes), status=200, mimetype='application/json')

@api.route('/api/v1/grow/<drug>', methods = ['GROW'])
def grow_drugs_api(drug):
    if drug != 'cocaine' and drug != 'meth':
        msg = {'message': f'I asked pablo escobar for {drug}, but he said he aint got no {drug}'}
        return flask.Response(json.dumps(msg), status=404, mimetype='application/json')
    if flask.request.method == 'GROW':
        with open('backend/db.json', 'r') as f: smokes = json.load(f)
        smokes['grown'][drug] += 1
        smokes['available'][drug] += 1
        smokes['totals'][drug] += 1
        with open('backend/db.json', 'w') as f: json.dump(smokes, f)
        ws.send(json.dumps({'type': 'grow', 'drug': drug, 'secret_key': 'METH_HOUSE-9999'}))
        msg = {'message': 'Funding addictions since 2007...'}
        return flask.Response(json.dumps(msg), status=200, mimetype='application/json')