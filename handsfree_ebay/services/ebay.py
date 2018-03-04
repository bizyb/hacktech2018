import requests
import json


def get_basic_info(item_summary):
    basic_info_string = item_summary.get('title')
    price = item_summary.get('price')
    basic_info_string += ', selling for ' + price.get('value') + ' ' + price.get('currency') + '.'
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
    token = "v^1.1#i^1#r^0#p^3#f^0#I^3#t^H4sIAAAAAAAAAOVYeWwUVRhnu9vCphQNQbAWzGa8Iji7b47t7gx0cctC2kAP2UIKBpo53rRjZ2eWeW/aLlQtTUSi0cSDGA6lhggRkGDEBDRgwh8mYAAvjAdGDRKPYKIRAggR32y77bZG6MEfTdxkM/Pe+67f7/u+N/MGdBX5Z2+o2nCpxDOxoKcLdBV4PEwx8BcVzpniLbircALIE/D0dN3b5ev2/jwPSSkjLS6FKG2ZCAY6UoaJxOxkBeXYpmhJSEeiKaUgErEiJuM1S0Q2CMS0bWFLsQwqUJ2ooJQIBILAaFEWgvIwp5BZM2ezwaqgouVhCLioLHCCJDFkFSEHVpsISyauoFjARGnA0YBvAIzIRkTABgWWX0kFlkMb6ZZJRIKAimWDFbO6dl6kNw5UQgjamBihYtXxRcm6eHViYW3DvFCerVgfC0ksYQcNHi2wVBhYLhkOvLEblJUWk46iQISoUKzXw2CjYjwXzCjCzxLNceU8x7OSKstahFH5W0LlIstOSfjGcbgzukprWVERmljHmZsxStiQH4MK7hvVEhPViYB7ecSRDF3ToV1BLayMr1iWXLiUCiTr622rTVeh6iJlOE7gWKacp2IYIkIhtJtaJKUVQ6XFHfT56zXax/YQhwssU9Vd7lCg1sKVkAQPh1LE5FFEhOrMOjuuYTewfDkuRyUTXunmtjeZDm4x3fTCFOEjkB3ePBG5yhiohVtVGxFWlSNcOCoAXuDDQji/NtxeH219xNwUxevrQ24sUJYydEqyWyFOG5ICaYXQ66SgrasiF9ZYLqpBWi0XNJoXNI2Ww2o5zWgQAghlWRGi/8MywdjWZQfD/lIZupDFWkElFSsN6y1DVzLUUJHsDtRXGB2ogmrBOC2GQu3t7cF2LmjZzSEWACbUWLMkqbTAlET1y+o3F6b1bNUqkGghXcSZNImmg1QgcW42UzHOVuslG2cqnQwZJ6FhkEuuigdFGBs6+x9QkQt1fIF09RExIKX1oFvkQcVKhSyJNLU71ZSNODAcoZDsZIh/FdpBG0qqZRqZ4es1O6SIe7WHp4RINoK9/UhgZD26vT58r4MNjEBHN9tILVt2ZoQwByuPQEdSFMsx8Wjc9amOQENzDE03DLddR+MwT30kYZqSkcG6gkbjMm9TJvQivbkFD9gZU7fG0+lqdXx1a6W+1mm37Fa6qm+vp5OVjTSvauXkz0FaFsJQUSPhMeFWYZuuwCZ9nGE3HcPIIXB7fVTYErBtvOVUkSUGskCgAWDJ64PMKbQgsALNCpIG+WhY4QAzpnzWNI+3VNaG4mNCtMDQyQ7TkBlvD9MqC2Gojg0aebUdX6DcHSa3wUSVaJSOhtkIzXMRcseFGRryKhwu5CETea+G/zochHJHdN/E3gN1bEL2x3R7DoNuzyFyzgcRQDNzwINF3mU+72QK6RgGkWSqstUR1CUtSB4GJjmF2jDYCjNpSbcLijyPlv06/1re54GeVeDO/g8Efi9TnPe1AMwcWClkbptRwkQBB3jAsBHArgT3DKz6mOm+aYu3CvrqHWejgbmHW++5/vj2o3+1PQ9K+oU8nsIJvm7PhJ5PHqhinijb+PrXuNP36pP8lUvnXtn30huHWvxzv/v95FVvIv6ZsDZx1ltTcnL9pvC2vfvngGWHXkucYF68v3bPnqkzV+y6fnCy81762LpjTWveOV089csDz5mnkhfvOHisZ8r04ou+dVu3TTp1puOhu9nOzs1tP6xv6DofLdjvObozufuX95v8911Ozm/8afNvMz7oqtn46dT0V/6jH85cumsG/LMhgV749vhHpR3f336EW3zt3Zd/vLrqm9Vbnv24vgyc331hw2njqemXS+uS54zuic3w+ryds2rKni494GVLv9i76dLDkzpPHD85u+yZaeofm/37/BnpyoW3lM+3e2c5nX8bbzYmjpzZscZ6e0tvGv8B+sil6bgRAAA="

    header = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type": "application/json",
        "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>"}

    response = requests.get(uri, headers=header)

    return json.loads(response.text)
