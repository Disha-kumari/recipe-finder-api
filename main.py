import requests

ingredient = input("Enter an ingredient: ")

url = "https://www.themealdb.com/api/json/v1/1/filter.php"

params = {
    "i": ingredient
}

response = requests.get(url, params=params)
data = response.json()

if data["meals"]:
    print("\n🍳 Recipes Found:\n")

    meals = data["meals"]

    for i, meal in enumerate(meals, start=1):
        print(f"{i}. {meal['strMeal']}")

    choice = int(input("\nChoose a recipe number: "))

    selected_meal = meals[choice - 1]

    print("\nSelected Recipe:")
    print(selected_meal["strMeal"])
else:
    print("\nNo recipes found.")