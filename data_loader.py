#!/usr/bin/env python

"""Load Martello json data to pandas DataFrame
"""

import pandas as pd
import json
import sys
#from IPython import display


def main(arguments):

    with open("ExperimentalData.json", "r") as read_file:
        data = json.load(read_file)
    
    mart_df = pd.DataFrame.from_dict(data, orient='index')

    mart_df = mart_df.drop(labels = 'timestamp', axis=1)

    mart_df = pd.concat([mart_df.drop(['acme'], axis=1), mart_df['acme'].apply(pd.Series)], axis=1)
    mart_df.rename(index=str, columns={"bandwidth_kbps": "acme_bandwidth_kbps", "jitter_ms": "acme_jitter_ms", "loss_percent" : "atma_loss_percent", "rssi_dbm" : "acme_rssi_dbm", "rtt_ms" : "acme_rtt_ms"}, inplace='True')

    #option2
    #mart_df = pd.concat([mart_df.drop(['acme'], axis=1), pd.DataFrame(mart_df['acme'].tolist())], axis=1)

    mart_df = pd.concat([mart_df.drop(['globex'], axis=1), mart_df['globex'].apply(pd.Series)], axis=1)
    mart_df.rename(index=str, columns={"bandwidth_kbps": "globex_bandwidth_kbps", "jitter_ms": "globex_jitter_ms", "loss_percent" : "globex_loss_percent", "rssi_dbm" : "globex_rssi_dbm", "rtt_ms" : "globex_rtt_ms"}, inplace='True')

    mart_df = pd.concat([mart_df.drop(['octan'], axis=1), mart_df['octan'].apply(pd.Series)], axis=1)
    mart_df.rename(index=str, columns={"bandwidth_kbps": "octan_bandwidth_kbps", "jitter_ms": "octan_jitter_ms", "loss_percent" : "rssi_loss_percent", "rssi_dbm" : "octan_rssi_dbm", "rtt_ms" : "octan_rtt_ms"}, inplace='True')

    pd.set_option('display.expand_frame_repr', False)
    print(mart_df)

    mart_df.to_csv("data.csv", index=False)

    #with pd.option_context('display.max_rows', 10, 'display.max_columns', 5):
        #print(mart_df)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
