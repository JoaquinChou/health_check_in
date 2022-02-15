import requests
import wget
import zipfile
import os

def updateChromeDriver(extract_path=None):
    # 1、get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    # 2、build the donwload url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    # 3、download the zip file using the url built above
    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    # 4、extract the zip file
    if extract_path is None:
        print("Please check your extract_path!!")
        return

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_path) # you can specify the destination folder path here

    # 5、delete the zip file downloaded above
    os.remove(latest_driver_zip)
    print("\nFinishing chromedriver update!")
