import argparse
from kestra import Kestra

def parse_api():
  # argparse
  parser = argparse.ArgumentParser(description='Welcome to my Python X Kestra argument parsing')

  # Define the key from parser
  parser.add_argument('--key', help='Parse the Places API key here:')

  # Get API Key for Google Places API
  args = parser.parse_args()
  key = args.key

  logger = Kestra.logger()
  logger.info("Hello from Python, your API is loaded successfully!")
  return key

places_api = str(parse_api())

Kestra.outputs({"Places API": places_api})