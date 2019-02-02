#!/usr/bin/env python

"""Load Martello json data to pandas DataFrame
"""

import pandas as pd
import json
import sys


def main(arguments):

    with open("./martello_data/ExperimentalData.json", "r") as read_file:
        data = json.load(read_file)
    
    mart_df = pd.DataFrame.from_dict(data).T
    
    print(mart_df)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
