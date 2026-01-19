from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orange", methods=["GET"])
def orange():
    return jsonify({
        "status": "UP",
        "message": "End point creation successfull"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

