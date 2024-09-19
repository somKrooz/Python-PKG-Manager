import click
import requests
import os
import zipfile
from .env import TOKEN

OWNER = "somKrooz"
REPO = "Personal_Packages"
BRANCH = "main"

URL = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/?ref={BRANCH}"


HEADERS = {
    "Authorization": f"token {TOKEN}"
}

def DisplayPackages()->None:
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code == 200:
        items = response.json()
        for item in items:
            if item['type'] == "file":
                if str(item['name']).endswith((".py", ".json", ".bat")):
                    continue
                else:
                    print(f":🗃️ {item['name']}:")
            elif item['type'] == "dir":
                print(f"📂: {item['name']}")
    else:
        print(f"Failed to retrieve files. Status code: {response.status_code}")


def downloadFiles(url:str, Filename:str)->None:
    response = requests.get(url,headers=HEADERS)

    if response.status_code == 200:
        files = response.json()
        print("Getting Your Package...")
        for file in files:
            if file['name'] == f"{Filename}.zip":
                download_url = file['download_url']
                file_response = requests.get(download_url, stream=True)

                if file_response.status_code == 200:
                    zip_file_path = f"{Filename}.zip"
                    with open(zip_file_path, "wb") as f:
                        f.write(file_response.content)

                    try:
                        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                            zip_ref.extractall('.')
                    except zipfile.BadZipFile as e:
                        print(f"Error: {e} - The file may not be a valid zip file.")
                    except Exception as e:
                        print(f"An error occurred while extracting {Filename}.zip: {e}")

                    os.remove(zip_file_path)
        
        print("Process Completed....")

    else:
        print(f"Failed to list files. Status code: {response.status_code}")


@click.group()
def cli():
    pass

@cli.command()
def list():
    """List Packages"""
    DisplayPackages()

@cli.command()
@click.option('--pkg', is_flag=True, help='Download Package with --pkg flag')
@click.option('--pre', is_flag=True, help='Download Preset with --pre flag')
@click.option('--name', required=True, help='Name of the package to Download')
def download(name, pkg, pre):
    if pkg:
        downloadFiles(URL, name)
    if pre:
        print("i will implement this one day :-} ......")

if __name__ == "__main__":
    cli()




