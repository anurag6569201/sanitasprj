import xml.etree.ElementTree as ET
import requests

api_call_url = f"https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=title:dengue"
response = requests.get(api_call_url)
xml_content = response.content.decode("utf-8")

root = ET.fromstring(xml_content)

for document in root.findall('document'):
    title = document.find('title').text
    overview = document.find('content[@name="overview"]').text
    mesh = document.find('content[@name="mesh"]').text
    groupName = document.find('content[@name="groupName"]').text
    snippet = document.find('content[@name="snippet"]').text

    print(f'Title: {title}')
    print(f'Overview: {overview}')
    print(f'Mesh: {mesh}')
    print(f'Group Name: {groupName}')
    print(f'Snippet: {snippet}')
    print('')