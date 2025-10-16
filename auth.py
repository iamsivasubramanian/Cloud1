from flask import Flask, session, redirect, url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "qelmfeognmgeogn"

CLIENT_ID = "nKlXIKFXkqlX46DVlKgmGu6OrihP3Bbu"
CLIENT_SECRET = "2Hf3gEcntOAStPPd_DzL7vJush_2PH_uFsENRV1zNcmupGpLsdD57F8zI5c0ZCNd"
DOMAIN = "dev-j87nde2dibougnwd.us.auth0.com"
CALLBACK_URL = "http://localhost:3000/callback"

oauth = OAuth(app)
auth0 = oauth.register(
    name="auth0",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=f"https://{DOMAIN}/.well-known/openid-configuration"
)

@app.route("/")
def home():
    user = session.get("user")
    if user:
        return f"""
        <h1>Welcome, {user['name']}!</h1>
        <p>Email: {user['email']}</p>
        <a href='/out'>Logout</a>
        """
    return "<h1>Welcome, Guest!</h1><a href='/in'>Login</a>"

@app.route("/in")
def login():
    return auth0.authorize_redirect(redirect_uri=CALLBACK_URL)

@app.route("/callback")
def callback():
    token = auth0.authorize_access_token()
    session["user"] = token["userinfo"]
    return redirect(url_for("home"))

@app.route("/out")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=3000)

