from flask import Flask, jsonify, request
import json
import os

from common import logger

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Hello Python Guru"})

@app.route('/<int:eid>', methods=['GET'])
def query_records(eid):

    response = {"status": "failed",
                "data": 'error: record not found'}

    with open('data.json') as f:
        data = f.read()
        records = json.loads(data)

    for record in records:
        if record['eid'] == eid:
            response["status"] = "success"
            response["data"] = record
            break
    logger.info("#########################3")
    logger.debug(response)
    logger.info("#########################3")
    return jsonify(response)


@app.route('/', methods=['PUT'])
def create_record():
    try:
        record = json.loads(request.data)
    except Exception as ex:
        return jsonify({"status": "failed", "data": "error:" + str(ex)})
    
    records = None
    
    if os.path.exists('data.json'):

        with open('data.json') as f:
            data = f.read()
    
        if not data:
            records = [record]
        else:
            records = json.loads(data)
            records.append(record)
    else:
        records = [record]

    with open('data.json', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify({"status": "success", "data": "message: Record has been created!"})


@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    response = {'status': "failed", "data": "error: Record not found!"}
    with open('data.json') as f:
        data = f.read()
        records = json.loads(data)

    for r in records:
        if r['eid'] == record['eid']:
            r['name'] = record['name']
            r['salary'] = record['salary']
            r['full_time'] = record['full_time']
            r['age'] = record['age']
            response = {'status': "success", "data": "message: Record has been updated!"}
            break

    with open('data.json', 'w') as f:
        f.write(json.dumps(records, indent=2))

    return jsonify(response)
    
@app.route('/<int:eid>', methods=['DELETE'])
def delete_record(eid):
    new_records = []
    reponse = {"status": "failed",
               "data": 'error: record not found'}
    with open('data.json') as f:
        data = f.read()
        records = json.loads(data)

    for idx, r in enumerate(records):
        if r['eid'] == eid:
            reponse = {"status": "success",
                        "data": "message: record has been deleted!"}
            records.pop(idx)

            with open('data.json', 'w') as f:
                f.write(json.dumps(records, indent=2))
            break

        
    return jsonify(reponse)

if __name__ == '__main__':
    app.run(debug=True)

# [client]   ---->   [NGINX  --> (WSGI <=> APP)]