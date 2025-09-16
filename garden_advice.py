"""
Garden Advice (branch: refactor-inputs-functions)
Simple refactor: replace hardcoded values with input() and extract logic into functions.
"""

def get_user_input():
    """
    Prompt the user for season and plant type, normalize to lowercase.
    """
    season = input("Enter the current season (e.g. summer, winter, spring, autumn): ").strip().lower()
    plant_type = input("Enter the plant type (e.g. flower, vegetable, herb): ").strip().lower()
    return season, plant_type


def get_gardening_advice(season, plant_type):
    """
    Produce gardening advice based on season and plant type using the original condition logic.
    """
    advice = ""

    # Season advice 
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Plant-type advice 
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


def main():
    season, plant_type = get_user_input()
    advice = get_gardening_advice(season, plant_type)
    print("\n--- Gardening Advice ---")
    print(advice)


if __name__ == "__main__":
    main()
