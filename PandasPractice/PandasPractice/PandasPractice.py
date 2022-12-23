from curses import keyname
from pandas import Series, DataFrame
import pandas as pd
import wget
import numpy as np
import sys
import csv
def main():
    """
    obj = pd.Series([4, 7, -5, 3])
    print(obj[obj > 0]) # 4 7 3
    print(obj * 2) # 8 14 -10 6
    print(np.exp(obj)) # 54.5981500331 1096.63315843 0.00673794699909 20.0855369232
    sdata = {'Ohio' : 35000, 'Texas' : 71000, 'Oregon' : 16000, 'Utah' : 5000}
    states = ['California', 'Ohio', 'Oregon', 'Texas']
    obj2 = pd.Series(sdata, index=states)
    print(obj2)
    print(pd.isnull(obj2))
    print(pd.notnull(obj2))
    obj2.name = 'population'
    obj2.index.name = 'state'
    print(obj2)
    data = {'state' : ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year' : [2000, 2001, 2002, 2001, 2002],
            'pop' : [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    print(frame)
    print(frame['state'])
    frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt']
                       , index=['one', 'two', 'three', 'four', 'five'])
    frame2['debt'] = 16.5
    print(frame2)
    # set debt of first row equal to 18.07
    frame2.loc[(frame2['state'] == "Ohio") & (frame2['year'] == 2000), 'debt'] = 18.09
    frame2.loc[(frame2['state'] == "Ohio") & (frame2['year'] == 2001), 'debt'] = 18.87
    frame2.loc[(frame2['state'] == "Ohio") & (frame2['year'] == 2002), 'debt'] = 20.31
    frame2.loc[(frame2['state'] == "Nevada") & (frame2['year'] == 2001), 'debt'] = 10.52
    frame2.loc[(frame2['state'] == "Nevada") & (frame2['year'] == 2002), 'debt'] = 10.91
    # sort frame2 from high to low by debt
    print(frame2)
    frame3 = frame2.sort_values(by='debt', ascending=False)
    print(frame3)
    val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    frame2['debt'] = val
    frame2['eastern'] = frame2.state == 'Ohio'
    print(frame2)
    """
    """
    pop = {'Nevada': {2001: 2.4, 2002: 2.9},
           'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
    frame4 = pd.DataFrame(pop)
    print(frame4.T)
    pdata = {'Ohio': frame4['Ohio'][:-1], 'Nevada': frame4['Nevada'][:2]}
    print(pd.DataFrame(pdata))
    frame5 = pd.DataFrame(pop, index=[2001, 2002, 2003])
    frame5.index.name = 'year' ; frame5.columns.name = 'state'
    print(frame5)
    print(frame5.values)
    """
    """
    obj = pd.Series(range(3), index=['a', 'b', 'c'])
    index = obj.index
    print(index)
    obj2 = pd.Series([1.5, -2.5, 0], index=index)
    print(obj2)
    obj3 = obj2.reindex(['b', 'a', 'c'])
    print(obj3)
    frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns = ['Ohio', 'Texas', 'California'])
    print(frame)
    states = ['Texas', 'Utah', 'California']
    frame2 = frame.reindex(columns=states)
    print(frame2)
    obj4 = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    print(obj4)
    new_obj4 = obj4.drop(['c', 'd'])
    print(new_obj4)
    s1 = pd.Series([7.3, -2.5, 3.4, 1.5])
    print(s1)
    s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1])
    print(s2)
    print(s1 + s2)
    frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print(frame)
    df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
    df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
    print(df1)
    print(df2)
    print(df1 + df2)
    """
    """
    frame = pd.DataFrame(np.random.randn(12).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print(frame)
    series = frame.iloc[0]
    print(series)
    print(frame - series)
    series2 = pd.Series(range(3), index=['b', 'e', 'f'])
    print(series2)
    print(frame + series2)
    series3 = frame['d']
    print(series3)
    print(frame.sub(series3, axis=0))
    """
    #f = lambda x : x.max() - x.min()
    #print(frame.applymap(f))
    #print(frame['e'].map(format))
    """
    obj = pd.Series(range(4), index = ['d', 'a', 'b', 'c'])
    print(obj)
    print(obj.sort_index())
    obj = Series([7, -5, 4, -8, 2, 0, 4])
    print(obj)
    print(obj.rank())
    print(obj.rank(method = 'first'))
    print(obj.rank(ascending = False, method = 'max'))
    df = pd.read_csv('mindex.txt', chunksize = 5)
    chunks = Series([], dtype=float)
    for chunk in df:
        chunks = chunks.add(chunk['key'].value_counts(), fill_value = 0)
    chunks = chunks.sort_values(ascending = False)
    print(chunks)
    data = pd.read_csv('ex5.txt')
    data.to_csv(sys.stdout, index = False, columns = ['a', 'b', 'c'])
    dates = pd.date_range('1/1/2000', periods = 7)
    print(dates)
    ts = pd.Series(np.arange(7), index = dates)
    print(ts)
    f = open('ex7.txt')
    lines = list(csv.reader(f))
    header, values = lines[0], lines[1:]
    data_dict = {h: v for h, v in zip(header, zip(*values))}
    print(data_dict)
    df = pd.read_csv("ex1.txt")
    # binary data format
    df.to_pickle('frame_pickle')
    # load binary file
    df2 = pd.read_pickle('frame_pickle')
    print(df2)
    """
if __name__ == "__main__":
    main()
