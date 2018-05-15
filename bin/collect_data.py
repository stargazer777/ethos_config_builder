#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))))
import zpool.get_zpool_data as zpool
rows_added = 0

print "Polling Zpool:"
rows_added = zpool.start_poll()

print "Number of records added: " + str(rows_added)

