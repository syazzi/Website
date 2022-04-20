from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def add_Drop_Modules():
    page = render_template('add_Drop_Modules.html')
    return page

if __name__ == '__main__':
    app.debug = True
    app.run()