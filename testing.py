import pandas as pd
demand_data = pd.read_excel('SampleData.xlsx','Demand')
dem1=demand_data.values.tolist()
keyNames = ['Customer', 'Product']
keyToValues = {}
for row in dem1:
	keyTuple = tuple(row[:len(keyNames)])
	valueList = row[len(keyNames):]
	keyToValues[keyTuple] = valueList 

fieldToIndex = {'DemandMin': 0, 'DemandMax': 1, 'DemandMode': 2, 'AssignedStore': 3}

keyToValues[('C_05', 'P_C_20')][fieldToIndex['DemandMin']]

for key, valueList in self.keyToValues.items():
        (custName, prodName) = key
    # get values from value list
        demandMin = valueList[fieldToIndex['DemandMin']]
        demandMax = valueList[fieldToIndex['DemandMax']]
        demandMode = valueList[fieldToIndex['DemandMode']]
        storeName = valueList[fieldToIndex['AssignedStore']]