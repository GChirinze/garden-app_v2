# garden_advice.py
# Provides gardening tips based on the current month (1-12).

# Month-to-tip mapping
MONTH_TIPS = {
    1: "January: Prune dormant trees and plan your vegetable garden.",
    2: "February: Start seeds indoors for tomatoes and peppers.",
    3: "March: Prepare soil and plant cool-season crops.",
    4: "April: Plant summer bulbs and mulch flower beds.",
    5: "May: Water regularly and watch for pests.",
    6: "June: Harvest early vegetables and deadhead flowers.",
    7: "July: Water deeply during heat waves.",
    8: "August: Collect seeds and divide perennials.",
    9: "September: Plant autumn vegetables and add compost.",
    10: "October: Rake leaves and protect tender plants.",
    11: "November: Clean garden tools and plant spring bulbs.",
    12: "December: Plan next year's garden and order seeds.",
}

def get_gardening_tip(month):
    # TODO: Add docstring
    return MONTH_TIPS.get(month, "Invalid month. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    # TODO: Replace hardcoded month with user input.
    month = 5
    print(get_gardening_tip(month))