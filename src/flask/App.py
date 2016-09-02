from flask import Flask,redirect,request,url_for,send_from_directory
import json
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['apk'])


def allowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']
    if file and allowedFile(file.filename):
        file.save(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), app.config['UPLOAD_FOLDER'], file.filename))
        return '{"status":{"message":true}}'


@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
def home(path):

    return redirect('http://cprakashagr.xyz')

@app.route('/uploads/<path:path>', methods=['GET'])
def catch_all(path):

    data = {}
    err = 0

    path = '{' + path + '}'

    json_acceptable_string = path.replace("'", "\"")
    path = json.loads(json_acceptable_string)

    # try:
    # except Exception as e:
    #     pass

    try:
        appName = path['app']
    except Exception:
        appName = None
        status = {'errorCode': 507, 'errorName': 'appName not found'}
        data['status'] = status
        json_data = json.dumps(data)
        return str(json_data)

    try:
        channel = path['channel']
    except KeyError:
        err += 1
        channel = 'dev'

    try:
        variant = path['variant']
    except KeyError:
        err += 1
        variant = 'var'

    try:
        build = path['build']
    except KeyError:
        err += 1
        build = 7


    if err is 3:
        return redirect('http://cprakashagr.xyz')

    if appName == 'glider':
        if channel == 'dev':
            return send_from_directory(directory='uploads', filename='app-debug.apk')

        elif channel == 'qa':
            return send_from_directory(directory='uploads', filename='app-debug.apk')

        else:
            return send_from_directory(directory='uploads', filename='app-debug.apk')

    else:
        return 'Haa haa'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
