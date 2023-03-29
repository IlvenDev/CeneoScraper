import requests as req
from bs4 import BeautifulSoup

product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = req.get(url)
page = BeautifulSoup(response.text, 'html.parser')
opinions = page.select("div.js_product-review")

for opinion in opinions:
    print(opinion["data-entry-id"])

# Opinia | opinion | div.js_product-review
# ID opinii | opinion_id | ["data-entry-id"]
# Autor | author | div.user-post__author-name
# Rekomendacje | recommendation | div.user-post__author-recomendation
# Liczba gwiazdek | score | div.user-post__score-count
# Czy potw. zakupem | purchased| div.review-pz
# data wystawienia | publish_date | div.user-post__published
# data zakupu | purchase_date | div.user-post__published
# ile przydatnych | thumbs_up | div.vote-yes js_product-review-vote js_vote-yes
# ile nieprzydatnych | thumbs_down | div.vote-no js_product-review-vote js_vote-no
# treść opinii | content | div.user-post__text
# lista wad | cons | div.
# lista zalet | pros | div.review-feature__col
