from mesa.batchrunner import batch_run
from conways_game_of_life.model import ConwaysGameOfLife
from multiprocessing import freeze_support
import pandas as pd

if __name__ == '__main__':
	freeze_support()
	params = {
		"height": 50, 
		"width": 50, 
		"initial_chance": 0.15,
		"ambition_ceil": [0.1,0.3,0.5],
		"opinion_ceil" : [0.1,0.3,0.5],
		"polarization" : [1,  2,  4],
	}

	results = batch_run(
		ConwaysGameOfLife,
		parameters=params,
		iterations=15,
		max_steps=300,
		display_progress=True
	)

	import matplotlib.pyplot as plt
	results = pd.DataFrame(results)
	results.to_csv('results.csv')
	plt.clf()
	plt.hist(df['Ideologies Quantity'], edgecolor='black', bins=60)
	plt.savefig("images" + os.sep + "Ideologies Quantity.png")
	plt.clf()
	df['Local Variety Index'] = df['Local Variety Index'].astype(float)
	plt.hist(df['Local Variety Index'], edgecolor='black', bins=60)
	plt.savefig("images" + os.sep + "Local Variety Index.png")
	plt.clf()
	df['Group Size Index'] = df['Group Size Index'].astype(float)
	plt.hist(df['Group Size Index'], edgecolor='black', bins=60)
	plt.savefig("images" + os.sep + "Group Size Index.png")

