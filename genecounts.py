from collections import defaultdict
import re
import os
import pandas as pd
from functools import reduce


def countfeatures(replicate_name, nickname):
	count_dict = defaultdict(int)
	with os.popen(f"samtools view {replicate_name}.sorted.bam") as cmd:
	    for line in cmd:
	        res = (re.split('[\|\s]', line))
	        count_dict[res[2]] = count_dict[res[2]]+1

	df = pd.DataFrame(list(count_dict.items()),columns = [f'gene',f'{replicate_name}_cnt'])
	df.to_csv(f'{nickname}_genecounts.csv', index=False)

#drought_1 = countfeatures("drought_1", "d1")
#drought_2 = countfeatures("drought_2", "d2")
drought_3 = countfeatures("drought_3", "d3")
#control_1 = countfeatures("control_1", "c1")
#control_2 = countfeatures("control_2", "c2")
#control_3 = countfeatures("control_3", "c3")
