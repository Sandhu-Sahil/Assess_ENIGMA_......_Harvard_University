import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import datetime
from pytz import timezone


from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    return redirect("/login")



@app.route("/WelcomeUser", methods=["GET", "POST"])
@login_required
def indexu():

    c = db.execute("SELECT class FROM users WHERE id = ? ", session["user_id"])

    if (c[0]['class'] == "CREATOR"):

        return redirect("/WelcomeCreator")

    elif (c[0]['class'] == "USER"):

        n = db.execute("SELECT username FROM users WHERE id = ? ", session["user_id"])

        n = n[0]['username']

        return render_template("indexu.html", name=n)

    else:

        return redirect("/WelcomeUser")



@app.route("/WelcomeCreator", methods=["GET", "POST"])
@login_required
def indexc():

    c = db.execute("SELECT class FROM users WHERE id = ? ", session["creator_id"])

    if (c[0]['class'] == "CREATOR"):

        n = db.execute("SELECT username FROM users WHERE id = ? ", session["creator_id"])

        n = n[0]['username']

        return render_template("indexc.html", name=n)

    elif (c[0]['class'] == "USER"):

        return redirect("/WelcomeUser")

    else:

        return redirect("/WelcomeCreator")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    if request.method == "POST":

        if not request.form.get("type"):
            return apology("must provide type")

        elif not request.form.get("username"):
            return apology("must provide username")

        elif not request.form.get("password"):
            return apology("must provide password")

        rows = db.execute("SELECT * FROM users WHERE (username = ? AND class = ?)", request.form.get("username") , request.form.get("type"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):

            return apology("invalid type, username and/or password")

        if request.form.get("type") == 'USER':

            session["user_id"] = rows[0]["id"]

            return redirect("/WelcomeUser")

        elif request.form.get("type") == 'CREATOR':

            session["creator_id"] = rows[0]["id"]

            return redirect("/WelcomeCreator")

    else:

        return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    if request.method == "POST":

        if not request.form.get("type"):
            return apology("must provide type")

        elif not request.form.get("username"):
            return apology("must provide username")

        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password")

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password and password confirmation must match")

        x = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if x:
            if (x[0]["username"] == request.form.get("username")):
                return apology("username is already registered")

        username = request.form.get("username")

        hash = request.form.get("password")

        cl = request.form.get("type")

        result = db.execute("INSERT INTO users (username, hash, class) VALUES (?, ?, ?)", username, generate_password_hash(hash), cl)

        if (cl == 'USER'):

            session["user_id"] = result

            return redirect("/WelcomeUser")

        elif (cl == 'CREATOR'):

            session["creator_id"] = result

            return redirect("/WelcomeCreator")

    else:

        return render_template("register.html")



@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    session.clear()

    return redirect("/WelcomeUser")



@app.route("/create", methods=["GET", "POST"])
@login_required
def create():

    if request.method == "POST":

        if not request.form.get("title"):
            return apology("must provide title")

        if not request.form.get("pass"):
            return apology("must provide pass for opening")

        o = db.execute("SELECT paper_id FROM papers WHERE (title = ? AND creator_id = ?)", request.form.get("title"), session["creator_id"])

        if o:
            return apology("title already exist, either edit that or create with another title")

        passs = request.form.get("pass")

        title = request.form.get("title")

        paper_id = db.execute("INSERT INTO papers (creator_id, title, pass) VALUES (?, ?, ?)", session["creator_id"], request.form.get("title"), passs)

        return render_template("creates.html", title=title, paper_id=paper_id)

    else:

        return render_template("create.html")



@app.route("/createsO", methods=["GET", "POST"])
@login_required
def createsO():

    if request.method == "POST":

        if not request.form.get("question"):
            return apology("must provide question")

        elif not request.form.get("o1"):
            return apology("must provide option A")

        elif not request.form.get("o2"):
            return apology("must provide option B")

        elif not request.form.get("o3"):
            return apology("must provide option C")

        elif not request.form.get("o4"):
            return apology("must provide option D")

        elif not request.form.get("correct"):
            return apology("must provide correct option")

        paper_id = request.form["button1"]

        db.execute("INSERT INTO Questions_o (paper_id, question, o1, o2, o3, o4, correct) VALUES ( ?, ?, ?, ?, ?, ?, ?)", paper_id, request.form.get("question"), request.form.get("o1"), request.form.get("o2"), request.form.get("o3"), request.form.get("o4"), request.form.get("correct"))
        t = db.execute("SELECT title FROM papers WHERE paper_id = ?", paper_id)

        return render_template("creates.html", title=t[0]['title'], paper_id=paper_id)

    else:
        return render_template("creates.html")



@app.route("/createsS", methods=["GET", "POST"])
@login_required
def createsS():

    if request.method == "POST":

        if not request.form.get("questionsub"):
            return apology("must provide question")

        paper_id = request.form["button2"]

        db.execute("INSERT INTO Questions_s (paper_id, question) VALUES ( ?, ?)", paper_id, request.form.get("questionsub"))

        t = db.execute("SELECT title FROM papers WHERE paper_id = ?", paper_id)

        return render_template("creates.html", title=t[0]['title'], paper_id=paper_id)

    else:
        return render_template("creates.html")



@app.route("/opened", methods=["GET", "POST"])
@login_required
def opened():

    if request.method == "POST":

        paper_id = request.form["button3"]

        t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", paper_id)

        o = db.execute("SELECT title FROM papers WHERE paper_id = ?", paper_id)

        r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", paper_id)

        if not t:
            t = 'Nonee'

        if not r:
            r = 'Nonee'

        return render_template("open.html", t=t, o=o, r=r, p=paper_id)

    else:
        return render_template("open.html")



@app.route("/created", methods=["GET", "POST"])
@login_required
def created():

    t = db.execute("SELECT * FROM papers WHERE creator_id = ?", session["creator_id"])

    if not t:
        return apology("Not created any forum")

    return render_template("created.html", t=t)



@app.route("/deleteQuestionO", methods=["GET", "POST"])
@login_required
def deleteQuestionO():

    question_id = request.form["button5"]

    p = db.execute("SELECT paper_id FROM Questions_o WHERE Question_id = ?", question_id)

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", p[0]['paper_id'])

    db.execute("DELETE FROM Questions_o WHERE Question_id = ?", question_id)

    db.execute("DELETE FROM responses_o WHERE Question_id = ?", question_id)

    t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", p[0]['paper_id'])

    r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", p[0]['paper_id'])

    if not t:
            t = 'Nonee'

    if not r:
            r = 'Nonee'

    return render_template("open.html", t=t, o=o, r=r, p=p[0]['paper_id'])



@app.route("/deleteQuestionS", methods=["GET", "POST"])
@login_required
def deleteQuestionS():

    question_id = request.form["button5"]

    p = db.execute("SELECT paper_id FROM Questions_s WHERE Question_id = ?", question_id)

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", p[0]['paper_id'])

    db.execute("DELETE FROM Questions_s WHERE question_id = ?", question_id)

    db.execute("DELETE FROM responses_s WHERE question_id = ?", question_id)

    t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", p[0]['paper_id'])

    r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", p[0]['paper_id'])

    if not t:
            t = 'Nonee'

    if not r:
            r = 'Nonee'

    return render_template("open.html", t=t, o=o, r=r, p=p[0]['paper_id'])



@app.route("/add", methods=["GET", "POST"])
@login_required
def add():

    paper_id = request.form["button5"]

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", paper_id)

    r = db.execute("SELECT pass FROM papers WHERE paper_id = ?", paper_id)

    paper_id_n = db.execute("INSERT INTO papers (creator_id, title, pass) VALUES (?, ?, ?)", session["creator_id"], o[0]['title'], r[0]['pass'])

    r = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", paper_id)

    for i in range(len(r)):
        db.execute("INSERT INTO Questions_o (paper_id, question, o1, o2, o3, o4, correct) VALUES (?, ?, ?, ?, ?, ?, ?)", paper_id_n, r[i]['question'], r[i]['o1'], r[i]['o2'], r[i]['o3'], r[i]['o4'], r[i]['correct'])

    h = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", paper_id)

    for i in range(len(h)):
        db.execute("INSERT INTO Questions_s (paper_id, question) VALUES (?, ?)", paper_id_n, h[i]['question'])

    return render_template("creates.html", title=o[0]['title'], paper_id=paper_id_n)



@app.route("/deleteF", methods=["GET", "POST"])
@login_required
def deleteF():

    paper_id = request.form["button5"]

    db.execute("UPDATE papers SET creator_id = 0 WHERE paper_id = ?", paper_id)

    t = db.execute("SELECT * FROM papers WHERE creator_id = ?", session["creator_id"])

    if not t:
        return apology("You have not created any FORM")

    return render_template("created.html", t=t)



@app.route("/editO", methods=["GET", "POST"])
@login_required
def editO():

    question_id = request.form["button5"]

    o = db.execute("SELECT paper_id FROM Questions_o WHERE Question_id = ?", question_id)

    t = db.execute("SELECT title FROM papers WHERE paper_id = ?", o[0]['paper_id'])

    r = db.execute("SELECT * FROM Questions_o WHERE Question_id = ?", question_id)

    return render_template("editO.html", t=t, r=r)



@app.route("/editingO", methods=["GET", "POST"])
@login_required
def editingO():

    if not request.form.get("tpe"):
        return apology("must provide type")

    elif not request.form.get("change"):
        return apology("must provide something to change")

    o = request.form["question_id"]

    t = request.form.get("tpe")

    c = request.form.get("change")

    db.execute("UPDATE Questions_o SET ? = ? WHERE Question_id = ?", t, c, o)

    p = db.execute("SELECT paper_id FROM Questions_o WHERE Question_id = ?", o)

    t = db.execute("SELECT title FROM papers WHERE paper_id = ?", p[0]['paper_id'])

    p = db.execute("SELECT * FROM Questions_o WHERE Question_id = ?", o)

    return render_template("editO.html", t=t, r=p)



@app.route("/editingOO", methods=["GET", "POST"])
@login_required
def editingOO():

    o = request.form["question_id"]

    p = db.execute("SELECT paper_id FROM Questions_o WHERE Question_id = ?", o)

    t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", p[0]['paper_id'])

    r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", p[0]['paper_id'])

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", p[0]['paper_id'])

    if not t:
            t = 'Nonee'

    if not r:
            r = 'Nonee'

    return render_template("open.html", t=t, o=o, r=r, p=p[0]['paper_id'])



@app.route("/editS", methods=["GET", "POST"])
@login_required
def editS():

    question_id = request.form["button5"]

    o = db.execute("SELECT paper_id FROM Questions_s WHERE question_id = ?", question_id)

    t = db.execute("SELECT title FROM papers WHERE paper_id = ?", o[0]['paper_id'])

    r = db.execute("SELECT * FROM Questions_s WHERE question_id = ?", question_id)

    return render_template("editS.html", t=t, r=r)



@app.route("/editingS", methods=["GET", "POST"])
@login_required
def editingS():

    if not request.form.get("change"):
        return apology("must provide something to change")

    o = request.form["question_id"]

    c = request.form.get("change")

    db.execute("UPDATE Questions_s SET question = ? WHERE question_id = ?", c, o)

    p = db.execute("SELECT paper_id FROM Questions_s WHERE question_id = ?", o)

    t = db.execute("SELECT title FROM papers WHERE paper_id = ?", p[0]['paper_id'])

    p = db.execute("SELECT * FROM Questions_s WHERE question_id = ?", o)

    return render_template("editS.html", t=t, r=p)



@app.route("/editingSS", methods=["GET", "POST"])
@login_required
def editingSS():

    o = request.form["question_id"]

    p = db.execute("SELECT paper_id FROM Questions_s WHERE question_id = ?", o)

    t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", p[0]['paper_id'])

    r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", p[0]['paper_id'])

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", p[0]['paper_id'])

    if not t:
            t = 'Nonee'

    if not r:
            r = 'Nonee'

    return render_template("open.html", t=t, o=o, r=r, p=p[0]['paper_id'])




@app.route("/attempt", methods=["GET", "POST"])
@login_required
def attempt():

    if request.method == "POST":

        if not request.form.get("id"):
            return apology("must provide title")

        if not request.form.get("pass"):
            return apology("must provide pass for opening")

        user_id = db.execute("SELECT * FROM attempted WHERE (paper_id = ? AND user_id = ?)", request.form.get("id"), session["user_id"])

        if user_id:
            return apology("Form already submitted, check responses")

        rows = db.execute("SELECT * FROM papers WHERE (paper_id = ? AND pass = ?)", request.form.get("id") , request.form.get("pass"))

        if len(rows) != 1 or not (rows[0]["pass"] == request.form.get("pass")):

            return apology("invalid paper_id or pass")

        db.execute("INSERT INTO attempted (user_id, paper_id) VALUES (?, ?)",session["user_id"], request.form.get("id"))

        o = db.execute("SELECT title FROM papers WHERE paper_id = ?", request.form.get("id"))

        t = db.execute("SELECT * FROM Questions_o Where paper_id = ?", request.form.get("id"))

        r = db.execute("SELECT * FROM Questions_s Where paper_id = ?", request.form.get("id"))

        p = request.form.get("id")

        lo = len(t)
        ls = len(r)

        if not t:
            t = 'Nonee'

        if not r:
            r = 'Nonee'

        return render_template("/attempting.html", o=o, t=t, r=r, lo=lo, ls=ls, p=p)

    else:

        return render_template("attempt.html")



@app.route("/submitted", methods=["GET", "POST"])
@login_required
def submitted():

    p = request.form["paper_id"]

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", p)

    t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", request.form.get("paper_id"))

    r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", request.form.get("paper_id"))

    lo = len(t)
    ls = len(r)

    if not t:
            t = 'Nonee'

    if not r:
            r = 'Nonee'

    if (t != 'Nonee'):
        for i in range(lo):
            db.execute("INSERT INTO responses_o (question_id, paper_id, user_id, response) VALUES (?, ?, ?, ?)",t[i]['Question_id'], p, session["user_id"], request.form.get(f"{i}"))

    if (r != 'Nonee'):
        for i in range(ls):
            db.execute("INSERT INTO responses_s (question_id, paper_id, user_id, response) VALUES (?, ?, ?, ?)",r[i]['question_id'], p, session["user_id"], request.form.get(f"{lo + i}"))

    r1 = db.execute("SELECT response FROM responses_o WHERE (paper_id = ? AND user_id = ?)", request.form.get("paper_id"), session["user_id"])

    r2 = db.execute("SELECT response FROM responses_s WHERE (paper_id = ? AND user_id = ?)", request.form.get("paper_id"), session["user_id"])

    return render_template("submitted.html", o=o, t=t, r=r, lo=lo, ls=ls, p=p, r1=r1, r2=r2)



@app.route("/responsesU", methods=["GET", "POST"])
@login_required
def responsesU():

    t = db.execute("SELECT * FROM attempted WHERE user_id = ?", session["user_id"])

    if not t:
        return apology("You have not attempted any forum yet")

    listt = []

    for paper_id in t:
        o = db.execute("SELECT title FROM papers WHERE paper_id = ?", paper_id['paper_id'])

        listt.append(o[0]['title'])

        r = len(listt)

    return render_template("responsesU.html", t=t, l=listt, r=r)



@app.route("/viewU", methods=["GET", "POST"])
@login_required
def viewU():

    paper_id = request.form.get("button5")

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", paper_id)

    t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", paper_id)

    r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", paper_id)

    lo = len(t)
    ls = len(r)

    if t:
        u = t[0]['Question_id']

    if r:
        y = r[0]['question_id']

    if not t:
            t = 'Nonee'

    if not r:
            r = 'Nonee'

    r1 = db.execute("SELECT response FROM responses_o WHERE (paper_id = ? AND user_id = ?)", paper_id, session["user_id"])

    r2 = db.execute("SELECT response FROM responses_s WHERE (paper_id = ? AND user_id = ?)", paper_id, session["user_id"])

    return render_template("viewU.html", o=o, t=t, r=r, lo=lo, ls=ls, p=paper_id, r1=r1, r2=r2)



@app.route("/responsesC", methods=["GET", "POST"])
@login_required
def responsesC():

    t = db.execute("SELECT * FROM papers WHERE creator_id = ?", session["creator_id"])

    return render_template("responses.html", t=t)



@app.route("/search", methods=["GET", "POST"])
@login_required
def search():

    p = request.form.get("paper_id")

    o = db.execute("SELECT user_id FROM attempted WHERE paper_id = ?", p)

    l = []

    for user_id in o:
        t = db.execute("SELECT username FROM users WHERE id = ?", user_id['user_id'])

        l.append(t[0]['username'])

    r = len(l)

    return render_template("search.html", l=l, o=o, p=p, r=r)



@app.route("/viewC", methods=["GET", "POST"])
@login_required
def viewC():

    paper_id = request.form.get("paper_id")

    user_id = request.form.get("user_id")

    u = db.execute("SELECT username FROM users WHERE id = ?", user_id)

    o = db.execute("SELECT title FROM papers WHERE paper_id = ?", paper_id)

    t = db.execute("SELECT * FROM Questions_o WHERE paper_id = ?", paper_id)

    r = db.execute("SELECT * FROM Questions_s WHERE paper_id = ?", paper_id)

    lo = len(t)
    ls = len(r)

    if not t:
            t = 'Nonee'

    if not r:
            r = 'Nonee'

    r1 = db.execute("SELECT response FROM responses_o WHERE (paper_id = ? AND user_id = ?)", paper_id, user_id)

    r2 = db.execute("SELECT response FROM responses_s WHERE (paper_id = ? AND user_id = ?)", paper_id, user_id)

    return render_template("viewC.html", o=o, t=t, r=r, lo=lo, ls=ls, p=paper_id, r1=r1, r2=r2, u=u)



def errorhandler(e):

    if not isinstance(e, HTTPException):
        e = InternalServerError()

    return apology(e.name, e.code)



for code in default_exceptions:
    app.errorhandler(code)(errorhandler)