import requests
from module.check import deb

name = "obsidian"

release_url = "https://github.com/obsidianmd/obsidian-releases/releases"

res = requests.head(release_url + "/latest", allow_redirects=False)
vversion = requests.Session().get_redirect_target(res).split("/")[-1]  # v1.1.1
version = vversion[1:]  # 1.1.1
# print(vversion, version)

# /v1.6.7/obsidian_1.6.7_amd64.deb
x64_deb_url = (
    release_url + "/download/" + vversion + "/" + name + "_" + version + "_amd64.deb"
)

deb(name, version, x64_deb_url)