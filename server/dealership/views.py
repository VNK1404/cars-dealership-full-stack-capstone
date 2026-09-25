import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Dealer database mock / local state
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

USERS = {
    "testuser": {
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
    }
}


def analyze_review_sentiment(text: str) -> str:
    """Analyze sentiment locally based on keywords (or upstream microservice)."""
    text_lower = text.lower()
    positive_words = ["great", "fantastic", "amazing", "good", "helpful", "exceptional", "excellent", "love", "best"]
    negative_words = ["bad", "terrible", "horrible", "awful", "poor", "slow", "disappointed", "rude", "worst"]

    pos_score = sum(1 for word in positive_words if word in text_lower)
    neg_score = sum(1 for word in negative_words if word in text_lower)

    if pos_score > neg_score:
        return "positive"
    elif neg_score > pos_score:
        return "negative"
    return "neutral"


def index(request):
    return JsonResponse({"status": 200, "message": "Cars Dealership Backend Service Active", "dealers": DEALERS})


def get_dealers(request):
    """Return all dealership records."""
    state = request.GET.get("state")
    if state:
        dealers_list = [
            d for d in DEALERS
            if d["state"].lower() == state.lower() or d["st"].lower() == state.lower()
        ]
        return JsonResponse({"status": 200, "dealers": dealers_list})
    return JsonResponse({"status": 200, "dealers": DEALERS})


def get_dealer(request, dealer_id):
    """Return specific dealer by dealer_id."""
    dealer = next((d for d in DEALERS if d["id"] == int(dealer_id)), None)
    if dealer:
        return JsonResponse({"status": 200, "dealer": [dealer]})
    return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)


def dealers_by_state(request, state):
    """Return dealers located in a specific state."""
    matched = [
        d for d in DEALERS
        if d["state"].lower() == state.lower() or d["st"].lower() == state.lower()
    ]
    return JsonResponse({"status": 200, "state": state, "dealers": matched})


def get_reviews(request, dealer_id):
    """Return reviews for a given dealer id."""
    dealer_reviews = REVIEWS.get(int(dealer_id), [])
    return JsonResponse({"status": 200, "dealer_id": int(dealer_id), "reviews": dealer_reviews})


def get_cars(request):
    """Return available car makes and models."""
    return JsonResponse({"status": 200, "CarMakes": CAR_MAKES})


@csrf_exempt
def add_review(request):
    """Add a new review for a dealership."""
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            dealer_id = int(data.get("dealership", 1))
            review_text = data.get("review", "")
            sentiment = data.get("sentiment") or analyze_review_sentiment(review_text)

            new_review = {
                "id": len(REVIEWS.get(dealer_id, [])) + 100,
                "name": data.get("name", "Anonymous"),
                "dealership": dealer_id,
                "review": review_text,
                "purchase": data.get("purchase", False),
                "purchase_date": data.get("purchase_date", ""),
                "car_make": data.get("car_make", ""),
                "car_model": data.get("car_model", ""),
                "car_year": data.get("car_year", ""),
                "sentiment": sentiment,
            }

            if dealer_id not in REVIEWS:
                REVIEWS[dealer_id] = []
            REVIEWS[dealer_id].append(new_review)

            return JsonResponse({"status": 200, "message": "Review added successfully", "review": new_review})
        except Exception as e:
            return JsonResponse({"status": 400, "error": str(e)}, status=400)
    return JsonResponse({"status": 405, "error": "Method not allowed"}, status=405)


@csrf_exempt
def analyze_review_sentiment_view(request):
    """Sentiment analysis endpoint."""
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            text = data.get("text", "")
            sentiment = analyze_review_sentiment(text)
            return JsonResponse({"status": 200, "text": text, "sentiment": sentiment})
        except Exception as e:
            return JsonResponse({"status": 400, "error": str(e)}, status=400)
    elif request.method == "GET":
        text = request.GET.get("text", "")
        sentiment = analyze_review_sentiment(text)
        return JsonResponse({"status": 200, "text": text, "sentiment": sentiment})
    return JsonResponse({"status": 405, "error": "Method not allowed"}, status=405)


@csrf_exempt
def login_user(request):
    """Login handler mock."""
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            username = data.get("userName")
            if username:
                return JsonResponse({"status": True, "userName": username})
            return JsonResponse({"status": False, "error": "Username required"}, status=400)
        except Exception as e:
            return JsonResponse({"status": False, "error": str(e)}, status=400)
    return JsonResponse({"status": False, "error": "Method not allowed"}, status=405)


@csrf_exempt
def logout_user(request):
    """Logout handler."""
    return JsonResponse({"status": True, "userName": ""})


@csrf_exempt
def registration(request):
    """User registration handler."""
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            username = data.get("userName")
            if not username:
                return JsonResponse({"status": False, "error": "Username required"}, status=400)
            if username in USERS:
                return JsonResponse({"status": False, "error": "Already Registered"}, status=400)

            USERS[username] = {
                "username": username,
                "firstName": data.get("firstName", ""),
                "lastName": data.get("lastName", ""),
                "email": data.get("email", ""),
            }
            return JsonResponse({"status": True, "userName": username})
        except Exception as e:
            return JsonResponse({"status": False, "error": str(e)}, status=400)
    return JsonResponse({"status": False, "error": "Method not allowed"}, status=405)
