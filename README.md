# CeneoScraper
Ceneo Scraper Project

## selektory CSS

Opinia | opinion | div.js_product-review
ID opinii | opinion_id | ["data-entry-id"]
Autor | author | span.user-post__author-name
Rekomendacje | recommendation | span.user-post__author-recomendation > em
Liczba gwiazdek | score | span.user-post__score-count
Czy potw. zakupem | purchased| div.review-pz
data wystawienia | publish_date | span.user-post__published > time:nth-child(1)["datetime"]
data zakupu | purchase_date | span.user-post__published > time:nth-child(2)["datetime"]
ile przydatnych | thumbs_up | span[id="votes-yes"] // button.vote-yes["data-total-vote"] // button.vote-yes > span
ile nieprzydatnych | thumbs_down | span[id="votes-no"] // button.vote-no["data-total-vote"] // button.vote-no > span
treść opinii | content | div.user-post__text
lista wad | cons | div.review-feature__col:has(> div.reviev-feature title-negatives) > div.review-feature item
lista zalet | pros | div.review-feature__col:has(> div.reviev-feature title-positives) > div.review-feature item

## użyte biblioteki
- requests
- beautifulsoup4