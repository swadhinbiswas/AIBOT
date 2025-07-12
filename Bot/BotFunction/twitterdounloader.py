
import os
import requests
import bs4



def download_video(url,filename):

  """

  Arguments:
  This function downloads a video from a given URL.
  url: str: The URL of the video to be downloaded.
  filename: str: The name of the file to be saved.
  return: str: The name of the file saved.
  """

  responce = requests.get(url,stream=True)
  # total_size = int(responce.headers.get('content-length',0))
  block_size = 1024
  # t=tqdm(total=total_size,unit='B',unit_scale=True)
  with open(filename,'wb') as file:
    for data in responce.iter_content(block_size):
      # t.update(len(data))
      file.write(data)
  # t.close()
  # if total_size!=0 and t.n!=total_size:
  #   print('ERROR, something went wrong')
  # else:
  #   print('Downloaded successfully')
  return filename



def twitter_download(url):
   api_url=f"https://twitsave.com/info?url={url}"

   responce=requests.get(api_url)
   data = bs4.BeautifulSoup(responce.text, "html.parser")
   download_button = data.find_all("div", class_="origin-top-right")[0]
   quality_buttons = download_button.find_all("a")
   highest_quality_url = quality_buttons[0].get("href")
   filepath = os.path.join(os.path.dirname(__file__), "videos")
   filename = f"{filepath}/video.mp4"
   download_video(highest_quality_url,filename)

   return filename
