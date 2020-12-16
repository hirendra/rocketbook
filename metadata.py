#!/usr/local/bin/python3

import sys
import re

infile = sys.argv[1]
outfile = sys.argv[2]
print(infile, outfile)
metadata_template = """
[ /Contents ( %s )
   /Rect [ 10 10 388 588 ]
   /Subtype /FreeText
   /DA ([0 0 0] rg /Helv 16 Tf)
   /Name /Note
   /SrcPg 1
   /Open true
   /ModDate (D:20101220193344)
   /Title (A Comment on Page 2)
   %s /Color [.5 .5 0]
   /ANN pdfmark
"""

txt = open(infile, 'r').read()
# in case our text contains () or %
escaped = txt.translate(txt.maketrans({"-":  r"\-",
                                          "]":  r"\]",
                                          "\\": r"\\",
                                          "^":  r"\^",
                                          "$":  r"\$",
                                          "*":  r"\*",
                                          "%":  r"\%",
                                          "(":  r"\(",
                                          ")":  r"\)",
                                          ".":  r"\."}))

# print(txt)
# having trouble with the % in the template, hence this workaround
metadata = metadata_template % (escaped, '%')
outf = open(outfile, 'w')
outf.write(metadata)
outf.close()
