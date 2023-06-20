import requests
import json
from tqdm.auto import trange
from pathvalidate import sanitize_filepath
import os

readfilespublic = "https://files.mega65.org/php/readfilespublic.php"
fileJSON = json.loads(requests.get(readfilespublic).text)
os.makedirs(sanitize_filepath("output"), exist_ok=True)
jsonbackup = open("./output/readfiles.json", "w")
json.dump(fileJSON, jsonbackup, sort_keys=True, indent=4)

for _ in trange(len(fileJSON), desc="Getting Files"):
    print(fileJSON[_]['title'])
    LocalFileLocation = sanitize_filepath("output/" + fileJSON[_]['location'])
    os.makedirs("/".join(LocalFileLocation.split("/")[:-1]), exist_ok=True)
    with requests.get("https://files.mega65.org/" + fileJSON[_]['location']) as RawFileContent, open(
        LocalFileLocation, "wb"
        ) as LocalFile, open(
            sanitize_filepath(LocalFileLocation + ".headers.json"), "w"
        ) as LocalContentHeadersOutput:
            LocalFile.write(RawFileContent.content)
            json.dump(
                dict(RawFileContent.headers),
                LocalContentHeadersOutput,
                sort_keys=True,
                indent=4,
            )