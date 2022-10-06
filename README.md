# Predict Cuisine from Ingredients
This classification model can predict cuisine from the recipe's ingredients. It's trained on the [whats-cooking](https://www.kaggle.com/competitions/whats-cooking/data) dataset which contains more than 30,000 recipes.

Check this [link](https://predict-cuisine.herokuapp.com/) to see if you can guess the origin of the dish!

<a href="url"><img src="https://lh3.googleusercontent.com/UinAfNkpFBPmYVR07UQFHuOQmXboaSwPCcT_hDo2Fy36PhCEhtxVVNXRzKZSqj7Ci8Eisn4FBw32QtY-TizrAA=w1280-h1280-c-rw-v1-e365" height="500" width="600" ></a>

For example, the recipe of [Fettucine Alfredo](https://www.yummly.com/recipe/Fettuccine-Alfredo-9045701) requires fairly simple ingredients: 
```1 lb. boneless skinless chicken breast halves
1 Tbsp. Bertolli® Classico Olive Oil
1 onions (small, thinly sliced)
2 cloves clove garlic, fine chop
1 jar Bertolli® Alfredo Sauce
1/2 cup chicken broth
2 Tbsp. fresh basil leaves (finely chopped, optional)
16 oz. fettucine (1 box, cooked and drained)
```
The model correctly identifies Fettucine Alfredo as a dish typical of Italian cuisine.

To the model, a partial list of ingredients like ```garlic, basil leaves, fettucine``` is still enough to determine that an Italian meal is in the works.

