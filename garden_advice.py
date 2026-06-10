# garden_advice.py
# Provides gardening tips based on the current month (1-12).

def get_gardening_tip(month):
    # TODO: Replace hardcoded month numbers with a dictionary or list.
    # TODO: Add docstring to explain the function.
    # TODO: Improve comments to follow PEP 8.
    if month == 1:
        return "January: Prune dormant trees and plan your vegetable garden."
    elif month == 2:
        return "February: Start seeds indoors for tomatoes and peppers."
    elif month == 3:
        return "March: Prepare soil and plant cool-season crops."
    elif month == 4:
        return "April: Plant summer bulbs and mulch flower beds."
    elif month == 5:
        return "May: Water regularly and watch for pests."
    elif month == 6:
        return "June: Harvest early vegetables and deadhead flowers."
    elif month == 7:
        return "July: Water deeply during heat waves."
    elif month == 8:
        return "August: Collect seeds and divide perennials."
    elif month == 9:
        return "September: Plant autumn vegetables and add compost."
    elif month == 10:
        return "October: Rake leaves and protect tender plants."
    elif month == 11:
        return "November: Clean garden tools and plant spring bulbs."
    elif month == 12:
        return "December: Plan next year's garden and order seeds."
    else:
        return "Invalid month. Please enter a number between 1 and 12."

if __name__ == "__main__":
    # TODO: Replace hardcoded month with user input.
    month = 5
    print(get_gardening_tip(month))