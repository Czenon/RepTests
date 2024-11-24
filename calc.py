from configparser import ConfigParser
import json

# Test function to calculate remaining lifespan
def calcLifespan():
    config = ConfigParser()
    results = []

    config.read("testvalues.ini")                                   # External file containing test values to check against
    testvals = json.loads(config.get('test', 'testvalues'))         # Get test values to check in function
    expectedvals = json.loads(config.get('test', 'expectedvalues')) # Get expected result list
    for x in testvals:
        if x > 20:
            results.append(0)
        else:
            results.append(20 - x)

    # Return exit code 0 if expected values match test variables
    if results == expectedvals: return 0
    else: return 1

calcLifespan()