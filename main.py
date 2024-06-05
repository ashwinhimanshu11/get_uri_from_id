import os
import json
import requests

ids = ["risbvjen", "rnrlcqlb", "hicyvtms", "pelkqozy", "tpkwawgk", "vpkczoqx", "njqytrex", "rzbmlgcs", "cpaoqlxb", "bwrhbbfz"]

json_data = []
directory = '/run/media/ashwinhimanshu11/New Volume/Work/Work/get_uri_from_id/Batches'
pdf_download_folder = "/run/media/ashwinhimanshu11/New Volume/Work/Work/get_uri_from_id/downloaded_pdfs"

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = os.path.join(directory, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            json_data.extend(data)

# print(data)

uri_list = []
for single_data in json_data:
    if (single_data["document_id"] in ids):
        uri_list.append(single_data["uri"])

# print(uri_list)

for uri in uri_list:
    file_name = uri.split('/')[-1]
    response = requests.get(uri, stream=True)

    if response.status_code == 200:

        if not os.path.exists("downloaded_pdfs"):
            os.mkdir("downloaded_pdfs")

        file_path = f"{pdf_download_folder}/{file_name}"

        with open(file_path, "wb") as pdf_file:
            for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            pdf_file.write(chunk)
            print(f"Downloaded: {file_name}")




