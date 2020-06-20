from .models import Booking, MEAL

def change_price(meal_plan):
        if meal_plan == MEAL[0][0]:  
            booking_fee = 100 # breakfast
        elif meal_plan == MEAL[1][0]:
            booking_fee = 200 # lunch  
        elif meal_plan == MEAL[2][0]:
            booking_fee = 300 # dinner
        
        return booking_fee