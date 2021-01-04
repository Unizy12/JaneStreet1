import pandas as pd
class Process:
    def __init__(self, df:pd.DataFrame):
        self._df = df

    def pDist(self, p:float, weight = True, targetName = 'resp') -> dict:
        data = self._df
        if (weight == True):
            data = data.query('weight > 0').reset_index(drop = True)
        data.loc[:,'action'] = data.apply(lambda x : 1 if x[targetName] > p else 0, axis = 1)
        respmean = data[['date', 'resp', 'action']].groupby('action')['resp'].mean().to_dict()
        for key in list(respmean.keys()):
            respmean[str(key) + '_respmean'] = respmean.pop(key)
        actioncount = data['action'].value_counts().to_dict()
        for key in list(actioncount.keys()):
            actioncount[str(key) + '_count'] = actioncount.pop(key)
        name = {'p':p}
        result = dict(name, **respmean)
        result = dict(result, **actioncount)
        return result