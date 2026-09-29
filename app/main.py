from flask import Flask, jsonify, request

app = Flask(__name__)

def add(a, b):
  return a + b

@app.route("/")
def hello():
  return jsonify(message="Hello from CI/CD starter!")

@app.route("/add")
def add_endpoint():
  try:
    a = float(request.args.get("a", "0"))
    b = float(request.args.get("b", "0"))
  except ValueError:
    return jsonify(error="Invalid input"), 400
    return jsonify(result=add(a, b))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)