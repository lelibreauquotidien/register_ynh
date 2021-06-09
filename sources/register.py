from flask import Flask,render_template, request
import sys
sys.path.append("/usr/lib/moulinette/")
import yunohost
yunohost.init_i18n()
from yunohost.user import user_create


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    #return 'Works !'

@app.route('/create_user/', methods=['POST'])
def create_user():
    form = request.form
    if form["username"] and form["firstname"] and form["lastname"] and form["password"] and if len(form["password"]) >= 8:
        user_create(username= form["username"], firstname=form["firstname"], lastname=form["lastname"],domain="saphir.eu.org", password=form["password"])
    else:
        return 'Error while saving user information'
if __name__ == "__main__":
    app.run()

