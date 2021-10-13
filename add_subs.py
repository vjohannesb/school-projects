import os
""" Lazy me - write a script to do simple (but repetitive) things... """

cmd = "git submodule add {url} {folder}"
folders = [f for f in os.listdir() if "." not in f]

projects = [
    {
        "url": "aspnet-api-asgmt",
        "folder": "ASPNET-API",
        "n": 1
    },
    {
        "url": "aspnet-mvc-asgmt",
        "folder": "ASPNET-MVC",
        "n": 1
    },
    {
        "url": "cs-asgmt",
        "folder": "C#",
        "n": 5
    },
    {
        "url": "dotnet-data-storage",
        "folder": "Data-Storage",
        "n": 2
    },
    {
        "url": "html-css-asgmt",
        "folder": "HTML-CSS",
        "n": 2
    },
    {
        "url": "js-asgmt",
        "folder": "JavaScript",
        "n": 2
    },
    {
        "url": "scrum-group-asgmt",
        "folder": "SCRUM",
        "n": 0
    },
]

def main():
    for project in projects:
        if project["n"] < 1:
            url = f"https://github.com/vjohannesb/{project['url']}.git"
            folder = f"{project['folder']}/assignment-1"
            os.system(cmd.format(url=url, folder=folder))
            # print(cmd.format(url=url, folder=folder))
            continue

        for i in range(1, project["n"] + 1):
            url = f"https://github.com/vjohannesb/{project['url']}-{i}.git"
            folder = f"{project['folder']}/assignment-{i}"
            # print(cmd.format(url=url, folder=folder))
            os.system(cmd.format(url=url, folder=folder))

if __name__ == "__main__":
    submodules = sum([project["n"] for project in projects])
    if "y" in input(f"Adding {submodules} submodules - are you sure you want to continue? [y/N] ").lower():
        main()