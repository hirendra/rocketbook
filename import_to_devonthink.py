#!/usr/local/bin/python3

import applescript
import sys
import logging
#from gntp.notifier import mini
from pync import Notifier

# This script is to be called from Hazel which sets theFile to the file being
# processed in Hazel

logging.basicConfig(filename='/tmp/importtodevonthink.log',
                    level=logging.DEBUG)
scpt = applescript.AppleScript('''
    on ImportToDevonthink(theFile)
        tell application id "DNtp"
            set theRecord to import theFile to incoming group
            tell theRecord
                set tags to "Notes, Sales"
            end tell
        end tell
    end ImportToDevonthink
    ''')

fpath = sys.argv[1]

res = (scpt.call('ImportToDevonthink', fpath))
logging.debug('ImportToDevonthink called with %s ' % (fpath))
#mini('ImportToDevonthink called with %s ' % (fpath))
Notifier.notify('ImportToDevonthink called with %s ' % (fpath))
