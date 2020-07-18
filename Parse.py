from lxml import html
import requests


page = requests.get("https://www.worldometers.info/coronavirus/country/us/")
tree = html.fromstring(page.content)
currentStats = tree.xpath('//*[@id="maincounter-wrap"]/div/span/text()')

worldPage = requests.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%22")
tree1 = html.fromstring(worldPage.content)

currentWorldStats = tree1.xpath('//*[@id="maincounter-wrap"]/div/span/text()')
print("US CASES")
desc = ["Cases", "Deaths", "Recoveries"]

i = 0
while i<3:
    print(desc[i], currentStats[i])
    i+=1


print("\nGLOBAL CASES")
i = 0
while i<3:
    print(desc[i], currentWorldStats[i])
    i+=1


