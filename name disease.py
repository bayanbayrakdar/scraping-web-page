

from bs4 import BeautifulSoup
import requests
import json

# Replace with the URL you're scraping from
url = 'https://www.healthline.com/conditions'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the condition links
condition_links = soup.find_all('a', {'class': 'css-2fdibo'})
print(condition_links)
data = []

for link in condition_links:
    name = link.find('h3', {'class': 'css-1lgashx'})
    if name:
        disease_name = name.text.strip()  # Extract the name text
        data.append({'tag': disease_name})
    else:
        data.append({'tag': 'Unknown Disease'})  # Fallback for missing name

# Save the extracted data to a JSON file
with open('healthcare_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data scraped and saved to healthcare_data.json")

     
[<a aria-label="COVID-19" class="css-2fdibo" data-element-event="INTERNALLINK|SECTION|Landing Page Engagement|Hub_of_hubs|LINK||lp1" data-event="Landing Page Engagement|Link Click_Hub_of_hubs_1|https://www.healthline.com/coronavirus" href="https://www.healthline.com/coronavirus"><div class="css-gi27li"><img alt="" class="css-1u513s7" src="https://media.post.rvohealth.io/wp-content/uploads/2022/01/coronavirus-hub-2021-key-art-2.png"/><div class="css-3pnppr"><div><h3 class="css-1lgashx">COVID-19</h3><p class="css-1hvc4v2">Latest Updates, Prevention Tips, and Resources on COVID-19</p></div><span class="css-1lijowq">Go to Condition<svg class="css-1awxqnt" height="40" viewbox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg"><path d="m24.87 37-2.23-2.3 11.83-13.14H.15V18.5h34.2L22.64 5.24 24.87 3 40 20z"></path></svg></span></div></div></a>, <a aria-label="Breast Cancer" class="css-2fdibo" data-element-event="INTERNALLINK|SECTION|Landing Page Engagement|Hub_of_hubs|LINK||lp2" data-event="Landing Page Engagement|Link Click_Hub_of_hubs_2|https://www.healthline.com/breast-cancer" href="https://www.healthline.com/breast-cancer"><div class="css-gi27li"><img alt="" class="css-1u513s7" src="https://media.post.rvohealth.io/wp-content/uploads/2022/10/Breast-Cancer-Hub-crops-700x350-hub-crop.jpg"/><div class="css-3pnppr"><div><h3 class="css-1lgashx">Breast Cancer</h3><p class="css-1hvc4v2">Supporting you through every stage of your breast cancer experience</p></div><span class="css-1lijowq">Go to Condition<svg class="css-1awxqnt" height="40" viewbox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg"><path d="m24.87 37-2.23-2.3 11.83-13.14H.15V18.5h34.2L22.64 5.24 24.87 3 40 20z"></path></svg></span></div></div></a>, <a aria-label="Inflammatory Bowel Disease" class="css-2fdibo" data-element-event="INTERNALLINK|SECTION|Landing Page Engagement|Hub_of_hubs|LINK||lp3" data-event="Landing Page Engagement|Link Click_Hub_of_hubs_3|https://www.healthline.com/inflammatory-bowel-disease" href="https://www.healthline.com/inflammatory-bowel-disease"><div class="css-gi27li"><img alt="" class="css-1u513s7" src="https://media.post.rvohealth.io/wp-content/uploads/2021/10/hoh_ibd.png"/><div class="css-3pnppr"><div><h3 class="css-1lgashx">Inflammatory Bowel Disease</h3><p class="css-1hvc4v2">Tips and tools to support your health &amp; wellbeing with IBD</p></div><span class="css-1lijowq">Go to Condition<svg class="css-1awxqnt" height="40" viewbox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg"><path d="m24.87 37-2.23-2.3 11.83-13.14H.15V18.5h34.2L22.64 5.24 24.87 3 40 20z"></path></svg></span></div></div></a>, <a aria-label="Migraine" class="css-2fdibo" data-element-event="INTERNALLINK|SECTION|Landing Page Engagement|Hub_of_hubs|LINK||lp4" data-event="Landing Page Engagement|Link Click_Hub_of_hubs_4|https://www.healthline.com/migraine" href="https://www.healthline.com/migraine"><div class="css-gi27li"><img alt="" class="css-1u513s7" src="https://media.post.rvohealth.io/wp-content/uploads/2022/09/Migraine-Hub-hub-crop-700x350-1.jpg"/><div class="css-3pnppr"><div><h3 class="css-1lgashx">Migraine</h3><p class="css-1hvc4v2">Tips, tools, and support for living and thriving with migraine</p></div><span class="css-1lijowq">Go to Condition<svg class="css-1awxqnt" height="40" viewbox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg"><path d="m24.87 37-2.23-2.3 11.83-13.14H.15V18.5h34.2L22.64 5.24 24.87 3 40 20z"></path></svg></span></div></div></a>, <a aria-label="Multiple Sclerosis" class="css-2fdibo" data-element-event="INTERNALLINK|SECTION|Landing Page Engagement|Hub_of_hubs|LINK||lp5" data-event="Landing Page Engagement|Link Click_Hub_of_hubs_5|https://www.healthline.com/multiple-sclerosis" href="https://www.healthline.com/multiple-sclerosis"><div class="css-gi27li"><img alt="" class="css-1u513s7" src="https://media.post.rvohealth.io/wp-content/uploads/2021/10/hoh_ms.png"/><div class="css-3pnppr"><div><h3 class="css-1lgashx">Multiple Sclerosis</h3><p class="css-1hvc4v2">Tools, support, and clarity for your MS Journey</p></div><span class="css-1lijowq">Go to Condition<svg class="css-1awxqnt" height="40" viewbox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg"><path d="m24.87 37-2.23-2.3 11.83-13.14H.15V18.5h34.2L22.64 5.24 24.87 3 40 20z"></path></svg></span></div></div></a>, <a aria-label="Rheumatoid Arthritis" class="css-2fdibo" data-element-event="INTERNALLINK|SECTION|Landing Page Engagement|Hub_of_hubs|LINK||lp6" data-event="Landing Page Engagement|Link Click_Hub_of_hubs_6|https://www.healthline.com/rheumatoid-arthritis" href="https://www.healthline.com/rheumatoid-arthritis"><div class="css-gi27li"><img alt="" class="css-1u513s7" src="https://media.post.rvohealth.io/wp-content/uploads/2021/10/hoh_ra.png"/><div class="css-3pnppr"><div><h3 class="css-1lgashx">Rheumatoid Arthritis</h3><p class="css-1hvc4v2">Tools, support, and clarity for your RA journey</p></div><span class="css-1lijowq">Go to Condition<svg class="css-1awxqnt" height="40" viewbox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg"><path d="m24.87 37-2.23-2.3 11.83-13.14H.15V18.5h34.2L22.64 5.24 24.87 3 40 20z"></path></svg></span></div></div></a>, <a aria-label="Type 2 Diabetes" class="css-2fdibo" data-element-event="INTERNALLINK|SECTION|Landing Page Engagement|Hub_of_hubs|LINK||lp7" data-event="Landing Page Engagement|Link Click_Hub_of_hubs_7|https://www.healthline.com/type-2-diabetes" href="https://www.healthline.com/type-2-diabetes"><div class="css-gi27li"><img alt="" class="css-1u513s7" src="https://media.post.rvohealth.io/wp-content/uploads/2021/10/hoh_t2d.png"/><div class="css-3pnppr"><div><h3 class="css-1lgashx">Type 2 Diabetes</h3><p class="css-1hvc4v2">Tools, support, and clarity for your type 2 diabetes journey</p></div><span class="css-1lijowq">Go to Condition<svg class="css-1awxqnt" height="40" viewbox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg"><path d="m24.87 37-2.23-2.3 11.83-13.14H.15V18.5h34.2L22.64 5.24 24.87 3 40 20z"></path></svg></span></div></div></a>]
Data scraped and saved to healthcare_data.json
1
