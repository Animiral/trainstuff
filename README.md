Train Game
==========

This is a railway operator economic simulation game. Found and buy companies operating railways. Lay tracks that connect cities and operate your trains on them to earn money. Keep upgrading your trains to the newest technology to make sure that your business does not fall behind the competition on the stock market. Earn dividends or sell shares to increase your personal wealth and win the game.

Getting Started
---------------

This game requires [Python 3](https://www.python.org/) and the `pygame` library.

```
$ pip install pygame
```

There are no releases yet. Download the source code using the green button above and extract it.

```
$ unzip trainstuff-main.zip && cd trainstuff-main
```

Run the main module.

```
$ python -m traingame.main
```

How to Play
-----------

There is not yet a lot of gameplay, so consider this information more aspirational than informational.

The game shows the map in a grid layout, with grey cities and green land tiles.

Click on land to buy a new piece of railway track. The track always connects two edges of the tile. Click right to rotate through the available options and click left to accept. New track must always connect to existing infrastructure: either a city or an open end of track.

When two cities are connected by tracks, all companies with depots in either city can run their trains between them and earn income.
