import json
import os

DATA_DIR = "src/data"

DATA_FILE = os.path.join(DATA_DIR, "reviews.json")


def save_review(review_data):

    # Create folder automatically
    os.makedirs(DATA_DIR, exist_ok=True)

    # Create file if not exists
    if not os.path.exists(DATA_FILE):

        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    # Read existing data
    with open(DATA_FILE, "r") as f:

        data = json.load(f)

    # Append new review
    data.append(review_data)

    # Save updated data
    with open(DATA_FILE, "w") as f:

        json.dump(data, f, indent=4)


def load_reviews():

    if not os.path.exists(DATA_FILE):

        return []

    with open(DATA_FILE, "r") as f:

        return json.load(f)