import time

mexLagIngredients = ["olive oil" , "ground chicken breast" , "chilli powder" , "ground cumin" , "red onions" , "black beans" , "taco sauce" , "corn kernels", "salt" , "spinach flour tortillas" , "shredded cheddar" , "scallions"]

mexLagInstructions = ["Preheat the oven to 425 degrees F." , "Preheat a large skillet over medium high heat." , "Add 2 tablespoons extra-virgin olive oil - twice around the pan." , "Add chicken and season with chili powder, cumin, and red onion." , "Brown the meat, 5 minutes." , "Add taco sauce or stewed or fire roasted tomatoes." , "Add black beans and corn." , "Heat the mixture through, 2 to 3 minutes then season with salt, to your taste." , "Coat a shallow baking dish with remaining extra-virgin olive oil, about 1 tablespoon oil." , "Cut the tortillas in half or quarters to make them easy to layer with." , "Build lasagna in layers of meat and beans, then tortillas, then cheese." , "Repeat: meat, tortilla, cheese again." , "Bake lasagna 12 to 15 minutes until cheese is brown and bubbly." , "Top with the scallions and serve."]

browniesIngredients = ["vegetable oil" , "sugar" , "vanilla" , "eggs" , "baking powder" , "cocoa powder" , "salt" , "flour"]

browniesInstructions = ["Preheat oven to 350°F." , "Mix oil and sugar until well blended." , "Add eggs and vanilla; stir just until blended." , "Mix all dry ingredients in a separate bowl." , "Stir dry ingredients into the oil/sugar mixture." , "Pour into greased 9 x 9 square pan." , "Bake for 20 minutes or until sides just start to pull away from the pan." , "Cool completely before cutting."]

lemonadeIngredients = ["sugar" , "ice cubes" , "lemon juice" , "julienned mint" , "lemon"]

lemonadeInstructions = ["In a small saucepan, combine sugar and 1/4 cup water." , "Bring mixture to a boil, stirring until the sugar has dissolved." , "Remove from heat. Let stand until completely cool." , "In a large pitcher half-filled with ice, add 2 cups water, lemon juice, simple syrup, mint, and lemon slices." , "Stir to combine. Serve over ice." , "Garnish with mint leaves and lemon slices."]

def recipe():
    choice = input("What would you like to cook? a) Mexican lasagna, b) Brownies, c) Mint Lemonade, d) Exit")
    if choice == "a":
        time.sleep(1)
        print("These are the ingredients you will need:")
        time.sleep(2)
        for item in mexLagIngredients:
            print(item)
            time.sleep(.2)
        time.sleep(2)
        print("Here are your instructions:")
        time.sleep(2)
        for item in mexLagInstructions:
            print(item)
            time.sleep(.2)
        time.sleep(3)
    if choice == "b":
        time.sleep(1)
        print("These are the ingredients you will need:")
        time.sleep(2)
        for item in browniesIngredients:
            print(item)
            time.sleep(.2)
        time.sleep(2)
        print("Here are your instructions:")
        time.sleep(2)
        for item in browniesInstructions:
            print(item)
            time.sleep(.2)
        time.sleep(3)
    if choice == "c":
        time.sleep(1)
        print("These are the ingredients you will need:")
        time.sleep(2)
        for item in lemonadeIngredients:
            print(item)
            time.sleep(.2)
        time.sleep(2)
        print("Here are your instructions:")
        time.sleep(2)
        for item in lemonadeInstructions:
            print(item)
            time.sleep(.2)
        time.sleep(3)
    if choice == "d":
        time.sleep(1)
        print("Thanks for visiting! Come again!")
        time.sleep(2)
        exit()
    else:
        time.sleep(1)
        print("Incorrect choice. Try again.")
        time.sleep(2)



recipe()
recipe()
recipe()
