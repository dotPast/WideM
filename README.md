# WideM

Remake of Yahiamice's "M" Resource Pack. But worse. (and with content for newer versions!)

[Check out the original resource pack! (its a youtube video, check the description for downloads)](https://www.youtube.com/watch?v=DULJPtZCcVA)  
[And the Moroccan man who made it!](https://twitch.tv/yahiamice)

## Building

The resource pack is created with [Beet](https://github.com/mcbeet/beet).

Install the requirements and build the project to get the resource pack.

```sh
# Setting up a virtual environment is recommended
python -m venv .venv

source .venv/bin/activate
# or use your OS specific method

pip install -r requirements.txt

beet build
```

The resource pack is saved to `out/`.

## Credits

- Yahiamice - The original resource pack
- [Yann](https://commons.wikimedia.org/wiki/User:Yann) - [Classic baguette](https://commons.wikimedia.org/wiki/File:Baguette_de_pain,_WikiCheese_Lausanne.jpg) (CC BY-SA 4.0) (Cropped background, downscaled)
