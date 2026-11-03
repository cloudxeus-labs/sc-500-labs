from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/")
def home():

    try:
        response = urllib.request.urlopen(
            "http://localhost:5000",
            timeout=2
        )

        backend_status = response.read().decode()

    except Exception:
        backend_status = "Backend service is currently unavailable"

    return f"""
    <html>
        <head>
            <title>CloudXeus Secure Web App</title>
        </head>

        <body>
            <h1>CloudXeus Technology Services</h1>

            <h2>Welcome to container-based applications</h2>

            <h3>Backend Response</h3>

            <p>{backend_status}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)