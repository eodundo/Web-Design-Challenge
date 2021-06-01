import pandas as pd

data_html = pd.read_csv("Resources/cities.csv")

data_html.to_html("output.html")