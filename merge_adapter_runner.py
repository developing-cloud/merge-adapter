from merge_adapter import lambda_handler
import json

with open('meta-data.json', 'r') as input:
	print(lambda_handler(json.load(input), None))