# Latte

`apt-get` for Pythonista.

## Installing

NOTICE: Latte is built to run on the StaSh shell. Make sure you have that installed before you run the installer code.

To install Latte to your Pythonista application, copy the below code, go to your Pythonista line-interpreter (the panel that swipes over on the right, that lets you type in Python code line-by-line), and paste the code, and run it. This should run the installer program provided in the repository. Once it starts running, you should start seeing your new package manager being installed to your StaSh.

```
import requests as r; exec(r.get("https://raw.githubusercontent.com/Seanld/Latte/master/installer.py").text);
```

## Getting Started

Everything should have been successfully installed, and you should now be able to run your brand new `latte` command in the StaSh shell.

To install a new package from _https://github.com/Seanld/Latte/master/public-packages_, just run `latte install <package-name>`. If you want to remove that package that you have installed, just run `latte remove <package-name>`. In order to update Latte to the newest version, just run `latte update`.

Latte is compatible with more than just the default repository that I provide here on this GitHub repo. Anyone hosting a Latte repository can share their URL, and you can install packages from said repository.

To change the URL of the repository Latte is pointed at, just run `latte point <repo-url>`.

NOTE: Some of these commands are being pre-documented, meaning that they might not work yet. I'm just writing them down so that everyone has a general idea of how this system will turn out. 

## Congratulations

You now are set up to install packages from any compatible repository. If you want to create your own Latte package, just run `latte new <your-package-name>`, and you'll have a brand new folder in your current directory named whatever your called your package. Edit the `meta.latte` file inside of that new directory, and change the values to whatever your package requires.
