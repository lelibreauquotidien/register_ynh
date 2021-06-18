import re
from flask import Flask, render_template, request, Response
import sys
import os

# regex patterns
unamePattern = re.compile(r"^[a-z0-9_]+$")
namePattern = re.compile(r"^([^\W\d_]{1,30}[ ,.'-]{0,3})+$")
passwordPattern = re.compile(r"^.{3,}$")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create_user/', methods=['POST'])
def create_user():
    form = request.form
    unameMatch = unamePattern.match(str(form["username"]))
    fnameMatch = namePattern.match(str(form["firstname"]))
    lnameMatch = namePattern.match(str(form["lastname"]))
    passwordMatch = passwordPattern.match(str(form["password"]))
    if bool(unameMatch) == True and bool(fnameMatch) == True and bool(lnameMatch) == True and bool(passwordMatch) == True:

        if form["username"] and form["firstname"] and form["lastname"] and form["password"] and len(form["password"]) >= 8:
            # user_create(username=form["username"], firstname=form["firstname"],
            #            lastname=form["lastname"], domain="saphir.eu.org", password=form["password"])
            os.system("sudo yunohost user create" + form["username"] + "-f " + form["firstname"] +
                      "-l " + form["lastname"] + "-p " + form["password"] + "-d saphir.eu.org")
        else:
            return 'Error while saving user information'
    else:
        return Response(
            "Bip-bop",
            status=500,
        )


if __name__ == "__main__":
    app.run()
