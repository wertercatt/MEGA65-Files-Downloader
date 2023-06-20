import requests
import json
from tqdm.auto import trange
from pathvalidate import sanitize_filepath
readfilespublic = "https://files.mega65.org/php/readfilespublic.php"
fileJSON = json.loads(requests.get(readfilespublic).text)

jsonbackup = open("./output/readfiles.json", "w")
json.dump(fileJSON, jsonbackup, sort_keys=True, indent=4)