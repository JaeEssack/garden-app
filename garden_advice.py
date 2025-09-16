"""
Improvements:
- Store advice in dictionaries for seasons and plant types.
- Add detailed docstrings and a helper to recommend plants per season.
"""

# Advice dictionaries for seasons and plant types
season_advice = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "Start planting new seeds and prune old branches.",
    "autumn": "Collect fallen leaves for compost and prepare soil for winter."
}

plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Harvest regularly to encourage growth."
}


season_recommendations = {
    "summer": ["basil", "marigold", "tomato"],
    "spring": ["lettuce", "pansy", "cilantro"],
    "autumn": ["kale", "chard", "parsley"],
    "winter": ["cover crops (where suitable)"]
}


def get_user_input():
    """
    Prompt the user for season and plant type, normalize to lowercase.
    """
    season = input("Enter the current season (summer, winter, spring, autumn): ").strip().lower()
    plant_type = input("Enter the plant type (flower, vegetable, herb): ").strip().lower()
    return season, plant_type


def get_gardening_advice(season, plant_type):
    """
    Return combined gardening advice string based on season and plant_type.
    Falls back to a default message when the input isn't found.
    """
    advice_lines = []
    advice_lines.append(season_advice.get(season, "No advice for this season."))
    advice_lines.append(plant_advice.get(plant_type, "No advice for this type of plant."))
    return "\n".join(advice_lines)


def recommend_plants(season):
    """
    Return a short recommendation string of plants that do well in the given season.
    """
    recommended = season_recommendations.get(season)
    if not recommended:
        return "No plant recommendations for this season."
    return "Recommended plants for {}: {}".format(season, ", ".join(recommended))


def main():
    """Main entry point: collect input, show advice and recommendations."""
    season, plant_type = get_user_input()
    advice = get_gardening_advice(season, plant_type)
    recommendations = recommend_plants(season)

    print("\n--- Gardening Advice ---")
    print(advice)
    print("\n--- Recommendations ---")
    print(recommendations)


if __name__ == "__main__":
    main()
