# Course Project

Simply run model.ipynb in jupyter notebook to re-run the model

Note:
- You need to create a new /data folder and put the data files into the data folder. Make sure this folder is at the same location with the model.ipynb
- I keep a /data folder, and put the relevant data inside that folder except Rating.csv because of its size
- In current /data foler, Rating_generated is the new feature generated using map and reduce prorgrams. I then attach it with Teleplay.csv in making new pandas data frame.
- map.py and reduce.py are the map reduce programs.
- I put all preprocessing/training/recommendation steps in model.ipynb. To use my model, simply run the cells in model.ipynb in order.
