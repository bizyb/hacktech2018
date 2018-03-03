import requests
import json


def get_basic_info(item_summary):
    basic_info_string = item_summary.get('title')
    price = item_summary.get('price')
    basic_info_string += ' selling for ' + price.get('value') + ' ' + price.get('currency') + '.'
    return basic_info_string


def get_details(item_summary):
    details_string = 'condition is ' + item_summary.get('condition') + '.'
    details_string += ' ships from ' + item_summary.get('itemLocation').get('country')
    shipping_cost = item_summary.get('shippingOptions')[0].get('shippingCost')
    details_string += ' for ' + shipping_cost.get('value') + ' ' + shipping_cost.get('currency') + '.'
    return details_string


def search_for(search_text):
    search_string = search_text.replace(' ', '+')
    uri = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?q={}&limit=3".format(search_string)
    token = "v^1.1#i^1#r^0#p^3#f^0#I^3#t^H4sIAAAAAAAAAOVYe2wURRjv9a7VAkUTGhQheCyIAtm72dc9Nr2Da2ltA5SDKwRBhbnd2Xbp3u65O9v2SiRnJRASRQmYWHykJkY0gimPACaiRDGCkaDEmKgJagxqVCJ/AAYhxtnrtb3WCH3wRxMvd9mb2e/1+77fNzuzIFtaNn9r3dY/y113FHdnQbbY5WImgrLSkgWT3cX3lRSBAgFXd3ZO1tPp/qXSgiktLa5EVtrQLeRtT2m6JeYmI5Rt6qIBLdUSdZhCloglMRFbtlRkfUBMmwY2JEOjvPWLI5TAcjzHMUEWcmEYYFkyq/fZbDQiFGIUEGAkOQgBy4QCzn3LslG9bmGo4wjFAiZEA458G1lOBKzICz4+EFxLeVcj01INnYj4ABXNhSvmdM2CWG8eKrQsZGJihIrWx2oTy2P1i2saGiv9Bbai+TwkMMS2NXhUbcjIuxpqNrq5GysnLSZsSUKWRfmjvR4GGxVjfcGMIvxcqnnEwwAXQoIkBIUgvD2prDXMFMQ3j8OZUWVayYmKSMcqztwqoyQbyY1IwvlRAzFRv9jrXFbYUFMVFZkRqqYq9siqRM1KypuIx02jVZWR7CBlOC7MsUyAp6IYWSSFyFzfDKUWjKRmZ5D312s0n+0hDqsNXVad3FneBgNXIRI8GpwiVhQKUkSEluvLzZiCncD65fhGwPSlkhfWOrXtLaaNm3WnvChF8uHNDW9diD5mDHDhtnFDDnHhQFLhQgLDI0Ye4IbT66PnR9QpUSwe9zuxoCTM0ClotiCc1qCEaImk104hU5VFTlBYLqQgWg6EFZoPKwqdFOQAzSgIAYSSSSkc+h/SBGNTTdoY9VNl6I0c1giVkIw0ihuaKmWooSK5FShPjHYrQjVjnBb9/ra2Nl8b5zPMJj8LAONfs2xpQmpGKUj1y6q3FqbVHGslRLQsVcSZNImmnTCQONebqChnynFo4kyVnSHjBNI0culj8aAIo0Nn/wOq5UAdXyAdfYsYgGnV55DcJxkpvwFJUztT63MRe4cj5E/aGeJfRqbPRFA2dC0zfL0mm5C4V3t4Shaphq+3HwkM4tHp9ZF4HWxgBDqq3kq4bJiZEcIcrDwCHShJhq3j0bjLq45AQ7E1RdU0p11H47BAfSRh6lDLYFWyRuOyYFEm6bXUpmY8YGdM3RpLp+vl8dWtVWqH3WaYLXRdfq2nE1VraF5WAuTHIToZFhDZcApjwi2jVlVC69Vxhl23Na0XgdPro8S2GLWOt5pKScggFoRpAFiyfUhyEh0Os2GaDUMF8SFB4gAzpnouaxpvpWzwx8aEqFpTyQrTmBlvD9M6w8JIHhs0srUdX6CcFaZvgQlJoRAdEtggzXNB8o8TGBrxMhou5CETBVvDfx0O8udIT1nfkTpalPswna7joNP1LjnpgyCgmQVgXql7lcc9ibJUjHwW1OWk0e5ToeIjDwOdnEJN5GtBmTRUzeJS17rpvy68UfCCoPsxcG//K4IyNzOx4H0BmDFwp4S5655yJgQ4wLEcYMlOF8weuOthpnoqHpWnv73rzi1vTQiZl+k515rUzbungfJ+IZerpMjT6Sp6ataTtT8d+fbcq5/vmOep2wYOxBW165Mb1XTtFWlXVwfccLJuavnmQHHPzosRzwOu3RcWLT1a87B2dcvZpwXXNtfVx4+cz3ad/GKK7J7A7WG7Ojb2PL/3j9ff3CGddz+zQs7ePfPalMP7P3wmeyn+1ezvvp8/98S0aSc+61x3oWXRdffh3S///pFv0v3bT+MXv4nPrjmzYeEx/4z02QUTXpi+8svnKtkDh/ecqri+fX/Xj/XHDr3TcPR0xQ8HL57cd+jBur2b/l7S+emsi/ymbrPplaKOJe8dO/XsB6kVM+e8/5Byfu7XG5LtpT8rh56ofOm1Sz0V88/Qb/x2/MrlzsolYLLcs+/gzr/KZqh1/Dnz494y/gOw4/mTuhEAAA=="

    header = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type": "application/json",
        "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"}

    response = requests.get(uri, headers=header)

    return json.loads(response.text)
