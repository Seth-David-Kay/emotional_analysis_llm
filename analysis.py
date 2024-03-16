import analysis_lib

def choose_least_failed(tweet, amount_run_compute_average, times_run_when_computing_average):
	least_failed = 11 # Start with a number it can't ever reach to make sure it is overriden (times run + 1)
	least_failed_average_scale = 0
	for i in range(amount_run_compute_average):
		# Run each iteration 10 times and compute the average each time
		return_values = analysis_lib.compute_average_of_ten(tweet, times_run_when_computing_average, False, False)
		average_scale = return_values[0]
		num_failed = return_values[1]

		if num_failed < least_failed:
			least_failed = num_failed
			least_failed_average_scale = average_scale

	print(f"Least Failed Responses: {least_failed} Reponses Failed")
	print(f"Average Scale Of Least Failed: {least_failed_average_scale}")

def choose_all(tweet, amount_run):
	return_values = analysis_lib.compute_average_of_ten(tweet, amount_run, False, False)
	average_scale = return_values[0]
	num_failed = return_values[1]

	print(f"Average Scale: {average_scale}")
	print(f"Num Responses Failed: {num_failed}")

tweet = "North Korea, please cease this douchebaggery. China doesn't even like you anymore. http://bit.ly/NeHSl"

# choose_least_failed(tweet, 10, 10)

choose_all(tweet, 100)