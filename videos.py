import requests
import json

class video:
  def __init__(self, id, thumb, title, description):
    self.id = id
    self.thumb = thumb
    self.title = title
    self.description = description

  def to_json(self):
    return {
      "id": self.id,
      "thumb": self.thumb,
      "title": self.title,
      "description": self.description
    }

url = 'https://www.youtube.com/@leadster_/videos' # Replace with your URL
response = requests.get(url)

fullContent = response.text
startExpression = 'var ytInitialData = '
startIndex = fullContent.index(startExpression)
endIndex = fullContent.index(';', startIndex)

jsonText = fullContent[startIndex + startExpression.__len__() : endIndex]

obj = json.loads(jsonText)

contents = obj['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents']

arr = []

for content in contents:
  if 'richItemRenderer' not in content:
    continue
  
  item = content['richItemRenderer']['content']['videoRenderer']

  id = item['videoId']
  thumb = item['thumbnail']['thumbnails'][-1]['url']
  title = item['title']['runs'][0]['text']
  description = item['descriptionSnippet']['runs'][0]['text']

  arr.append(video(id, thumb, title, description))
  #print((id, thumb, title, description)) # Print the response body as text
  #break

json_videos = [p.to_json() for p in arr]

#print(json.dumps(json_videos))
with open('videos.json', 'w') as f:
    json.dump(json_videos, f, indent=4)

print('Foi!')
