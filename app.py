from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def file_downloads():
    return '''
        <html>
            <a href="http://127.0.0.1:5000/">Home</a><br>
            <a href="/file"><button>Download</button></a>
        </html>
        '''


@app.route('/file')
def return_files():
    return send_file(
        'test.csv',
        mimetype='text/csv',
        attachment_filename='test.csv',
        as_attachment=True
    )


if __name__ == '__main__':
    app.run()
