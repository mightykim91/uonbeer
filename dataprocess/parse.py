import pandas as pd

beers = pd.read_csv('src/beers.csv')
reviews = pd.read_csv('src/asd.csv')
print(beers.columns)
print(reviews.columns)

beer_review = pd.merge(left=beers, right=reviews, left_on="id", right_on="beer_id")
print(beer_review.head())