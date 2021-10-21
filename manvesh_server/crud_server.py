from flask import Flask, jsonify, request
import json
import os

from parent import logger


app = Flask(__name__)

@app.route('/')
def welcom():
    logger.info('*'*10)
    return jsonify({'message':'_/\_Welcome_/\_'})

@app.route('/<int:eid>', methods=['GET'])
def get_record(eid):
    f = open('data1.json', mode='r')
    data = f.read()
    records = json.loads(data)
    f.close()

    for i in range(0, len(records)):
        if records[i]['eid'] == eid:
            return jsonify(records[i])

    return jsonify({'message': 'no record found'})


@app.route('/', methods=['PUT'])
def put_records():

    try:
        record = json.loads(request.data)
    except Exception as ex:
        return jsonify({'status': 'unsuccessful',
                        'message': str(ex)})
    records = None
    success = True

    if os.path.exists('data1.json'):
        f = open('data1.json', mode='r')
        data = f.read()
        f.close()
        
        if not data:
            records = [record]
        else:
            records = json.loads(data)

    else:
        records = [record]

    for i in range(0, len(records)):
        if records[i]['eid'] == record['eid']:
            success = False
            break
    else:
        records.append(record)

    f1 = open('data1.json', mode='w')
    f1.write(json.dumps(records, indent=3))
    f1.close()

    if success == False:
        return jsonify({'status': 'unsuccessful',
                        'message': 'found duplicate data'})
    else:
        return jsonify({'status': 'successful',
                        'message': 'successfully added the data'})


@app.route('/', methods=['POST'])
def update_record():
    success = False
    record = json.loads(request.data)

    f = open('data1.json', mode='r')
    data = f.read()
    records = json.loads(data)
    f.close()

    for i in range(0, len(records)):
        if records[i]['eid'] == record['eid']:
            records[i]['name'] = record['name']
            records[i]['salary'] = record['salary']
            records[i]['night_shift'] = record['night_shift']
            records[i]['hobbies'] = record['hobbies']
            records[i]['age'] = record['age']
            success = True
            break


    f1 = open('data1.json', mode='w')
    f1.write(json.dumps(records, indent=3))
    f1.close()

    if success == True:
        return jsonify({'status':'successful',
                        'message': 'data updated successfully'})
    else:
        return jsonify({'status': 'unsuccessful',
                        'message': 'no relevant data found to update'})
     

@app.route('/<int:eid>', methods=['DELETE'])
def del_record(eid):

    f = open('data1.json', mode='r')
    data = f.read()
    records = json.loads(data)
    f.close()

    index_count = -1
    success = False

    for i in range(0, len(records)):
        if records[i]['eid'] == eid:
            index_count = i
            success = True
            break

    if index_count != -1:
        records.pop(index_count)

    f1 = open('data1.json', mode='w')
    f1.write(json.dumps(records, indent=3))
    f1.close()

    if success == True:

        return jsonify({'status': 'successful',
                        'message': 'successfully deleted'})
    else:
        return jsonify({'status': 'unsuccessful',
                        'message': 'no relevant data found to be deleted'})

    
if __name__ == "__main__":
    app.run(debug=True)