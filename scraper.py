import requests as req
from bs4 import BeautifulSoup

def get_cos(ancestor, selector = None, attribute = None, return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None

product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = req.get(url)
page = BeautifulSoup(response.text, 'html.parser')
opinions = page.select("div.js_product-review")

all_opinions = []

for opinion in opinions:
    single_opinion = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recommendation": opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "score": opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased": opinion.select_one("div.review-pz").text.strip(),
        "publish_date": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchase_date": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "thumbs_up": opinion.select_one("button.vote-yes > span").text.strip(),
        "thumbs_down": opinion.select_one("button.vote-no > span").text.strip(),
        "content": opinion.select_one("div.user-post__text").text.strip(),
        "pros": [pros.text.strip() for pros in opinion.select("div.review-feature__col:has(> div.reviev-feature title-positives) > div.review-feature item")],
        "cons": [cons.text.strip() for cons in opinion.select("div.review-feature__col:has(> div.reviev-feature title-negatives) > div.review-feature item")],
    }
    
    all_opinions.append(single_opinion)
    
print(all_opinions)

# Opinia | opinion | div.js_product-review
# ID opinii | opinion_id | ["data-entry-id"]
# Autor | author | span.user-post__author-name
# Rekomendacje | recommendation | span.user-post__author-recomendation > em
# Liczba gwiazdek | score | span.user-post__score-count
# Czy potw. zakupem | purchased| div.review-pz
# data wystawienia | publish_date | span.user-post__published > time:nth-child(1)["datetime"]
# data zakupu | purchase_date | span.user-post__published > time:nth-child(2)["datetime"]
# ile przydatnych | thumbs_up | span[id="votes-yes"] // button.vote-yes["data-total-vote"] // button.vote-yes > span
# ile nieprzydatnych | thumbs_down | span[id="votes-no"] // button.vote-no["data-total-vote"] // button.vote-no > span
# treść opinii | content | div.user-post__text
# lista wad | cons | div.review-feature__col:has(> div.reviev-feature title-negatives) > div.review-feature item
# lista zalet | pros | div.review-feature__col:has(> div.reviev-feature title-positives) > div.review-feature item
