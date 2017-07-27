# Latte

`apt-get` for Pythonista.

*NOTE:* _There is a ton of introductory documentation located over at http://seanld.me/latte!_

## What's The Point?

When I was using (StaSh)[https://github.com/ywangd/stash] on Pythonista, I found it really annoying that I had to constantly run self-extracting Python scripts to install various add-ons and commands for StaSh. Because of that, I decided to create a simple utility that allows the creation, hosting, and sharing of software without hassle.

Now users of StaSh can easily communicate their software to other users. No more transfer problems.

Latte is also a platform for easily creating your own commands for StaSh. It allows you to install packages that install programs to StaSh's `stash_extensions/bin` directory. Now you can create your own commands!

## Installing

NOTICE: Latte is built to run on the StaSh shell. Make sure you have that installed before you run the installer code.

To install Latte to your Pythonista application, copy the below code, go to your Pythonista line-interpreter (the panel that swipes over on the right, that lets you type in Python code line-by-line), and paste the code, and run it. This should run the installer program provided in the repository. Once it starts running, you should start seeing your new package manager being installed to your StaSh.

```python
import requests as r; exec(r.get("https://raw.githubusercontent.com/Seanld/Latte/master/installer.py").text);
```

## Getting Started

If you want to learn how to properly use Latte, you can head over to http://seanld.me/latte. There's plenty of information over there to get you started!