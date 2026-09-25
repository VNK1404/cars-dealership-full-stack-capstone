from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DEALERS = [
    {
        "id": 1,
        "full_name": "Downtown Motors",
        "city": "Wichita",
        "state": "Kansas",
        "st": "KS",
        "address": "100 Main Street",
        "zip": "67202",
        "lat": "37.6872",
        "long": "-97.3301",
        "short_name": "Downtown",
    },
    {
        "id": 2,
        "full_name": "Prairie Auto Center",
        "city": "Topeka",
        "state": "Kansas",
        "st": "KS",
        "address": "450 Prairie Ave",
        "zip": "66603",
        "lat": "39.0473",
        "long": "-95.6752",
        "short_name": "Prairie",
    },
    {
        "id": 3,
        "full_name": "Metro Cars",
        "city": "Dallas",
        "state": "Texas",
        "st": "TX",
        "address": "789 Commerce St",
        "zip": "75201",
        "lat": "32.7767",
        "long": "-96.7970",
        "short_name": "Metro",
    },
    {
        "id": 4,
        "full_name": "Austin Speedways",
        "city": "Austin",
        "state": "Texas",
        "st": "TX",
        "address": "200 Congress Ave",
        "zip": "78701",
        "lat": "30.2672",
        "long": "-97.7431",
        "short_name": "Austin",
    },
]

CAR_MAKES = [
    {"name": "Toyota", "models": ["Camry", "Corolla", "RAV4"]},
    {"name": "Honda", "models": ["Civic", "Accord", "CR-V"]},
    {"name": "Ford", "models": ["F-150", "Mustang", "Explorer"]},
    {"name": "Audi", "models": ["A4", "Q5", "A6"]},
    {"name": "BMW", "models": ["3 Series", "5 Series", "X5"]},
]

REVIEWS = {
    1: [
        {
            "id": 1,
            "name": "John Doe",
            "dealership": 1,
            "review": "Fantastic services and great buying experience!",
            "purchase": True,
            "purchase_date": "02/15/2026",
            "car_make": "Toyota",
            "car_model": "Camry",
            "car_year": 2024,
            "sentiment": "positive",
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "dealership": 1,
            "review": "The dealership staff was polite and helpful.",
            "purchase": False,
            "sentiment": "positive",
        },
    ],
    2: [
        {
            "id": 3,
            "name": "Robert Brown",
            "dealership": 2,
            "review": "Average wait times during service inspection.",
            "purchase": True,
            "purchase_date": "01/10/2026",
            "car_make": "Honda",
            "car_model": "CR-V",
            "car_year": 2023,
            "sentiment": "neutral",
        }
    ],
    3: [],
    4: [
        {
            "id": 4,
            "name": "Alice Miller",
            "dealership": 4,
            "review": "Exceptional customer care and fast transaction.",
            "purchase": True,
            "purchase_date": "03/01/2026",
            "car_make": "Ford",
            "car_model": "Mustang",
            "car_year": 2025,
            "sentiment": "positive",
        }
    ],
}


def analyze_sentiment(text: str) -> str:
    text_lower = text.lower()
    pos_terms = ["great", "fantastic", "amazing", "good", "helpful", "exceptional", "excellent", "love", "best"]
    neg_terms = ["bad", "terrible", "horrible", "awful", "poor", "slow", "disappointed", "rude", "worst"]

    pos = sum(1 for w in pos_terms if w in text_lower)
    neg = sum(1 for w in neg_terms if w in text_lower)

    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    return "neutral"


@app.get("/")
def health_check():
    return jsonify({"status": 200, "message": "Cars Dealership Microservice API is running"})


@app.get("/api/dealers")
def dealers():
    state = request.args.get("state")
    if state:
        filtered = [
            d for d in DEALERS
            if d["state"].lower() == state.lower() or d["st"].lower() == state.lower()
        ]
        return jsonify({"status": 200, "dealers": filtered})
    return jsonify({"status": 200, "dealers": DEALERS})


@app.get("/api/dealers/<int:dealer_id>")
def dealer(dealer_id):
    d = next((x for x in DEALERS if x["id"] == dealer_id), None)
    if d:
        return jsonify({"status": 200, "dealer": [d]})
    return jsonify({"status": 404, "error": "Dealer not found"}), 404


@app.get("/api/dealers/<int:dealer_id>/reviews")
def reviews(dealer_id):
    revs = REVIEWS.get(dealer_id, [])
    return jsonify({"status": 200, "dealer_id": dealer_id, "reviews": revs})


@app.get("/api/dealers/state/<state>")
def by_state(state):
    matched = [
        d for d in DEALERS
        if d["state"].lower() == state.lower() or d["st"].lower() == state.lower()
    ]
    return jsonify({"status": 200, "state": state, "dealers": matched})


@app.get("/api/cars")
def get_car_makes():
    return jsonify({"status": 200, "CarMakes": CAR_MAKES})


@app.post("/api/analyze")
def analyze():
    body = request.get_json(silent=True) or {}
    text = body.get("text", "")
    sentiment_result = analyze_sentiment(text)
    return jsonify({"status": 200, "text": text, "sentiment": sentiment_result})


@app.post("/api/dealers/<int:dealer_id>/reviews")
def post_review(dealer_id):
    body = request.get_json(silent=True) or {}
    review_text = body.get("review", "")
    sentiment_result = body.get("sentiment") or analyze_sentiment(review_text)

    new_rev = {
        "id": len(REVIEWS.get(dealer_id, [])) + 100,
        "name": body.get("name", "Anonymous"),
        "dealership": dealer_id,
        "review": review_text,
        "purchase": body.get("purchase", False),
        "purchase_date": body.get("purchase_date", ""),
        "car_make": body.get("car_make", ""),
        "car_model": body.get("car_model", ""),
        "car_year": body.get("car_year", ""),
        "sentiment": sentiment_result,
    }

    if dealer_id not in REVIEWS:
        REVIEWS[dealer_id] = []
    REVIEWS[dealer_id].append(new_rev)

    return jsonify({"status": 200, "message": "Review added successfully", "review": new_rev})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
