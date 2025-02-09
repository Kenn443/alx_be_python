#  Prompts the user for the current weather and provides clothing recommendations.

weather = input("Please enter the weather condition (sunny/rainy/cold): ")
if weather == "sunny":
    print("Please wear a t-shirt and sunglasses.")

elif weather == "rainy":
    print("Please don't forget your umbrella and a raincoat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")  

else:
    print("Sorry, I don't have recommendations for this weather.") 