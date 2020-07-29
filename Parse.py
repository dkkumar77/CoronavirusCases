from lxml import html
import requests


page = requests.get("https://www.worldometers.info/coronavirus/country/us/")
treeStat = html.fromstring(page.content)
currentStats = treeStat.xpath('//*[@id="maincounter-wrap"]/div/span/text()')

worldPage = requests.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%22")
treeStatWorld = html.fromstring(worldPage.content)

currentWorldStats = treeStatWorld.xpath('//*[@id="maincounter-wrap"]/div/span/text()')
desc = ["Cases", "Deaths", "Recoveries"]


print("Current Number of Coronavirus Cases:\n\n\n")

print("US CASES")
i = 0
while i<3:
    print(desc[i], currentStats[i])
    i+=1


print("\nGLOBAL CASES")
i = 0
while i<3:
    print(desc[i], currentWorldStats[i])
    i+=1



