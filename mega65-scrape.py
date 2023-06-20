import requests
import json
from tqdm.auto import trange
from pathvalidate import sanitize_filepath
readfilespublic = "https://files.mega65.org/php/readfilespublic.php"
