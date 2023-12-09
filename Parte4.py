import requests

def download_csv_from_url(url):

    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        print(response.text)
        filename = url.split('/')[-1]
        with open(filename, "wb") as heart_failure_ds:
            heart_failure_ds.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

url_ds = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
download_csv_from_url(url_ds)