import random

# for such a trivial problem a class is maybe overkill but I figured better to demonstrate usage anyway
class ContestantRun(object):
	def __init__(self):
		pass

	def doRun(self):		
		# 1 is the car
		doors = [0,0,1]
		random.shuffle(doors)

		# contestant makes a choice
		first_choice = random.randint(0,2)

		# find a door that is not the choice that has a goat
		# interestingly no need to simulate this part but I wrote it anyway to ensure I understood the problem
		# goat_door_index = None
		# for i in range(0,3):
		# 	if i != first_choice and doors[i] == 0:
		# 		goat_door_index = i
		# 		break

		# two doors left, either the contestant wins by changing or keeping their selection
		if doors[first_choice] == 1:
			return 'kept'
		else:
			return 'changed'
		


if __name__ == "__main__":
	cr = ContestantRun()

	#a place to store results of the runs
	results = {
		'changed': 0,
		'kept': 0
	}

	# run for x times
	num_runs = 10000
	print('Executing {runs} runs...'.format(runs=num_runs))
	print('')
	for i in range(0, num_runs):
		results[cr.doRun()] += 1

	# report results
	for key in results:
		print('{key}:{value}'.format(key=key, value=results[key]))