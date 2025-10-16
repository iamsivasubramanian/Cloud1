from flask import Flask, session, redirect
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "qelmfeognmgeogn"

oauth = OAuth(app)

# --- 🔧 Replace these with your actual Auth0 app details ---
cid = "cTJ8G7lQZzqYUn1oneWCGmbSMZy4nDof"           #"YOUR_CLIENT_ID"
csec ="0eelKNWIsf_8Ey-Wd3ZVeu0YrQbuDFKS2F6OEyWHwhfLTGJCVatarwHWeU3RywWg"    #"YOUR_CLIENT_SECRET"
cdom ="dev-qdi7zq20rhbbdayj.us.auth0.com"            #"YOUR_DOMAIN" 
cb = "http://localhost:3000"
# ------------------------------------------------------------

auth0 = oauth.register(
    "auth0",
    client_id=cid,
    client_secret=csec,
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=f"https://{cdom}/.well-known/openid-configuration"
)

@app.route("/")
def home():
    u = session.get("u")
    if u:
        return f"<h1>Welcome {u['name']} <a href='/out'>Logout</a></h1>"
    return "<h1>Welcome Guest <a href='/in'>Login</a></h1>"

@app.route("/in")
def login():
    return oauth.auth0.authorize_redirect(redirect_uri=cb)

@app.route("/callback")
def callback():
    t = auth0.authorize_access_token()
    session["u"] = t["userinfo"]
    return redirect("/")

@app.route("/out")
def out():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=3000)









#Install dependencies:

#pip install flask authlib



#python app.py
