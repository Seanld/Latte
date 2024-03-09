# Latte

`apt` for Pythonista.

## What's The Point?

When I was using [StaSh](https://github.com/ywangd/stash) on Pythonista, I found it really annoying that I had to constantly run self-extracting Python scripts to install various add-ons and commands for StaSh. Because of that, I decided to create a simple utility that allows the distribution of StaSh-based tools with less hassle.

Latte is also a platform for easily creating your own commands for StaSh.

## Installing

NOTICE: Latte is built to run on the StaSh shell. Make sure you have that installed before you run the installer code.

To install Latte to Pythonista, copy the below code, go to your Pythonista line-interpreter (the panel that swipes over on the right, that lets you type in Python code line-by-line), and paste the code, and run it. This should run the installer program provided in the repository. Once it starts running, you should start seeing your new package manager being installed to your StaSh.

```python
import requests as r; exec(r.get("https://raw.githubusercontent.com/Seanld/Latte/master/installer.py").text);
```
