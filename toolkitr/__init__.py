from toolkitr import __storage__
from toolkitr.__depend__ import *

__version__ = "0.1"
__downloads__ = "toolkitr/downloads.json"

def download(vers: str) -> None:
  if vers not in toolkitr.__storage__.initz():
    return "Unknown download name."
  else:
    with open(__downloads__, "r") as downloaded:
      data = json.load(downloaded)

    data[vers] = True

    with open(__downloads__, "w") as downloader:
      json.dump(data, downloader, indent = 4)
      print(f"Download Update: {vers} has successfully been added to installed downloads.")
      
  return vers

def remove(vers: str) -> None:
  if vers not in toolkitr.__storage__.initz():
    return "Unknown download name."
  else:
    with open(__downloads__, "r") as downloaded:
      data = json.load(downloaded)

    data[vers] = False

    with open(__downloads__, "w") as downloader:
      json.dump(data, downloader, indent = 4)
      print(f"Download Update: {vers} has successfully been removed from installed downloads.")
      
  return vers

def depend():
  from toolkit.__depend__ import files
  return files
