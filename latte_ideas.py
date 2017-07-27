# A package manager meant for Pythonista, built on StaSh.

import argparse
import os
import requests
import sys
from shutil import rmtree

# noqa: W191

ROOT = os.path.join(os.path.expanduser('~'), 'Documents')


class ansi:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def Orange(text):
    return ansi.ORANGE + text + ansi.ENDC


def Green(text):
    return ansi.GREEN + text + ansi.ENDC


def Red(text):
    return ansi.RED + text + ansi.ENDC


class SWConfig(object):  # Parser for config files like the repository listing
    def __init__(self, content):
        self.data = {}
        for line in content.splitlines():
            key, _, value = line.partition("=")
            self.data[key.strip()] = value.strip()

    def __getitem__(self, key):
        return self.data[key]

    def keys(self):
        return self.data.keys()


def get_repositories():
    if not os.path.exists(".latte-repos.swconf"):
        print(Orange("PROBLEM") + ": Repository listing doesn't exist, "
              "rebuilding to default...")
        with open(".latte-repos.swconf", "w") as out_file:
            out_file.write("universe=https://raw.githubusercontent.com/Seanld/"
                           "latte-universe/master")
    with open(".latte-repos.swconf", "r") as in_file:
        return SWConfig(in_file.read())


def download_package(url, package_name):
    """Handles the installation of packages directories (since they're no
       longer tarfiles)."""
    content_listing = ("bin.py", "meta.latte")
    package_path = os.path.join(ROOT, package_name)
    os.mkdir(package_path)
    for item in content_listing:
        with open(os.path.join(package_path, item), "w") as out_file:
            out_file.write(requests.get(url + "/" + package_name + "/" +
                                        item).text)


def action_install(args):
    repo_name, _, package_name = args.package.split("/")
    if not package_name:  # if no slash was found...
        print(Orange("WARNING") + ": Repository was not specified, using "
              "universe repository instead.")
        package_name = repo_name
        repo_name = "universe"
    repo_to_use = get_repositories()[repo_name]
    print("Downloading {}/{}".format(repo_to_use, package_name))
    try:
        download_package(repo_to_use, package_name)
    except:  # avoid bare exceptions
        print(Red("ERROR") + ": Couldn't find package")
    # Move to correct locations
    print("Installing")
    srce_path = os.path.join(ROOT, package_name)
    stash_ext = os.path.join(ROOT, "stash_extensions")
    latte_path = os.path.join(stash_ext, "latte")
    if not os.path.exists(latte_path):
        os.mkdir(latte_path)
    os.rename(os.path.join(srce_path, "meta.latte"),
              os.path.join(latte_path, package_name + ".latte"))
    os.rename(os.path.join(srce_path, "bin.py"),
              os.path.join(stash_ext, "bin", package_name + ".py"))
    rmtree(srce_path)
    print(Green("SUCCESS") + ": Package installed!")


def action_remove(args):
    stash_ext = os.path.join(ROOT, "stash_extensions")
    os.remove(os.path.join(stash_ext, "bin", args.package + ".py"))
    os.remove(os.path.join(stash_ext, "latte", args.package + ".latte"))
    print(Green("SUCCESS") + ": Removed " + args.package + " successfully!")


def action_update(args):
    print("Jeez! Sorry, but we are currently working on self-update "
          "capabilities. For now, just redo the install process to update.")


def action_new(args):
    package_path = os.path.join(ROOT, args.package)
    if os.path.exists(package_path):
        print(Red("ERROR") + ": Couldn't build, directory already exists.")
        return
    os.mkdir(package_path)
    with open(os.path.join(package_path, "meta.latte"), "w") as out_file:
        out_file.write("developer=Your name here\n"
                       "description=Enter description of your app here\n"
                       "version=0.1")
    with open(os.path.join(package_path, "bin.py"), "w") as out_file:
        out_file.write("# This is just an example template. You can change it "
                       "as you wish.\n\n"
                       "import sys\n"
                       "import argparse\n\n"
                       "def main(sargs):\n"
                       "\tparser = argparse.ArgumentParser()\n"
                       "\tparser.add_argument('echo', help='What you want the "
                       "command to echo back.')\n"
                       "\targs = parser.parse_args(sargs)\n\n"
                       "\tprint('Echoing back: '+args.echo)\n\n"
                       "if __name__ == '__main__':\n"
                       "\tmain(sys.argv[1:])")
    print(Green("SUCCESS") +
          ": Made new package template '" + args.package + "'!")


def action_add_repo(args):
    try:
        data = SWConfig(requests.get(args.package + "/init.latte").text)
        nickname = data["NICKNAME"]
        with open(".latte-repos.swconf", "a") as append_file:
            append_file.write("\n" + nickname + "=" + args.package)
        print(Green("SUCCESS") + ": '" + nickname + "' added to repositories!")
    except:  # avoid bare exceptions
        print(Orange("REPO ISSUE") + ": Either repository doesn't exist, or "
              "does not contain an 'init.latte' file.")


def action_list_repos(args):
    if args.package == "all":
        with open(".latte-repos.swconf") as in_file:
            as_config = SWConfig(in_file.read())
        for repo in as_config.keys():
            print(Green(repo) + ": " + Orange(as_config[repo]))


def main(sargs):
    parser = argparse.ArgumentParser()
    parser.add_argument("method", type=str,
                        help="What action to perform (install, remove, etc)")
    parser.add_argument("package", help="Name of package", type=str)
    args = parser.parse_args(sargs)
    func = locals().get('action_' + args.method.replace('-', '_'))
    if func:  # if there is a local 'action_' function then call it...
        func(args)
    else:
        print(Red("SYNTAX ERROR") + ": Unknown command '" + args.method + "'!")


if __name__ == "__main__":
    main(sys.argv[1:])
