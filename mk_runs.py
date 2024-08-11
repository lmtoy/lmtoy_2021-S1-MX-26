# Using /home/teuben/LMT/lmtoy/data_lmt/unity/data_lmt.log
# 2021-S1-MX-26 - Science
#   script generated by source_obsnum.sh
import os
import sys

from lmtoy import runs

project="2021-S1-MX-26"

# Dictionary of sources, each with a list of obsnum's in this project
# negative obsnums are ignored in the combinations. See also comments.txt
# for obsnum specific comments and parameters!
on = {}

on["IRAS13349+2438"] = \
 [ 100398, 100399, 100400, 100402, 100403, 100404, 100406, 100407, 100408,]

on["PG_1448+273"] = \
 [ 100431, 100432, 100433, 100435, 100436, 100437, 100439, 100440, 100441,]

# parameters for the first pass of the pipeline (restart=1 is automatically enforced here)
pars1 = {}

pars1["IRAS13349+2438"] = ""
pars1["PG_1448+273"] = ""

# parameters for the (optional) second pass of the pipeline (e.g. for bank=0)
pars2 = {}

pars2["IRAS13349+2438"] = ""
pars2["PG_1448+273"] = ""

# parameters for the (optional) third pass of the pipeline (usually for bank=1)
pars3 = {}

pars3["IRAS13349+2438"] = ""
pars3["PG_1448+273"] = ""

# Found 2 source(s) for 2021-S1-MX-26

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
