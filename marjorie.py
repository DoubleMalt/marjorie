import re;
import os;
import json;

from flask import Flask, request, abort
from flask_cors import CORS

from uuid import uuid4

pattern = re.compile('[\W_]+', re.UNICODE)

BASE_DIR = os.getenv("MARJORIE_DATA_DIR", '/var/lib/marjorie/data')

app = Flask(__name__)
CORS(app)

@app.route('/api/dump/<key>', methods=['POST'])
def data_dump(key):
    sanitized_key = pattern.sub('', key)

    target_path = os.path.join(BASE_DIR, sanitized_key)

    if os.path.isdir(target_path):
        json_data = request.get_json(force=True)
        with open(os.path.join(target_path, "%s.json" % uuid4()), "w") as json_file:
            json.dump(json_data, json_file, indent=True)

        return '{"result": "ok"}'

    else:
        abort(404)
