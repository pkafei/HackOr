import os
import pandas
 
def load_xls(pth, sheet):
	mats = []
	for f in os.listdir(pth):
		if f.endswith('.xls'):
			try:
				mats.append(pandas.read_excel(os.path.join(pth, f), sheet, index_col=0))
			except Exception:
				continue
	return pandas.concat(mats)
 
fins = load_xls('fins', 'ORESTAR Export')
comms = load_xls('comms', 'Committee Search Result')
all = pandas.merge(fins, comms, left_on='Contributor/Payee Committee ID', right_index=True)