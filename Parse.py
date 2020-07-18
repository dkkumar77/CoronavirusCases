from lxml import html
import requests


page = requests.get("https://www.worldometers.info/coronavirus/country/us/")
tree = html.fromstring(page.content)
currentStats = tree.xpath('//*[@id="maincounter-wrap"]/div/span/text()')

worldPage = requests.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%22")
tree1 = html.fromstring(worldPage.content)

currentWorldStats = tree1.xpath('//*[@id="maincounter-wrap"]/div/span/text()')

print('United States - Cases, Deaths, Recoveries in Current Time', currentStats)

print('Globally - Cases, Deaths, Recoveries in Current Time', currentWorldStats)



