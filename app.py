from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    destination = request.form["destination"]
    budget = request.form["budget"]
    days = request.form["days"]

    itinerary = [
        f"Day 1: Visit famous attractions in {destination}",
        "Day 2: Explore local markets and food",
        "Day 3: Sightseeing and relaxation"
    ]

    return render_template(
        "index.html",
        destination=destination,
        budget=budget,
        days=days,
        itinerary=itinerary
    )

if __name__ == "__main__":
    app.run(debug=True)