Two primary data structures in pandas: Series (1-D) and DataFrame(2-D)

### Series 
    1. Creation:
        s = pd.Series(data, index = index)
        dates = pd.date_range('20130101', periods = 6)
        
    2. "Series is ndarray-like":
        s[0]
        s[ s > s.median() ]
        s[[4,3,1]]
        np.exp(s)
        s.dtype
        s.array
        s.to_numpy()
    3. "Series is dict-like":
        s['index1']
        'index1' in s  # boolean


### DataFrame:

    1. Creation:
        
        # Creating a df by specifying values, index, columns
        df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
        
        # Creating a df by passing a dict:
        df2 = pd.DataFrame({'A': 1.,
                            'B': pd.Timestamp('20130102'),
                            'C': pd.Series(1, index=list(range(4)), dtype='float32')})


    2. Column:

         1  selection:
                 df['A'];    df[['A','B']]
         
         2  addition:
                 df['D'] = df['one'] > 2;    df['D'] = 'hi'
         
         3  deletion:
                 del df['D']     df.pop('D')     df.drop('ColA', axis = 1)

         4  insert a new column:
                 df.insert(loc = 1, column = 'bar', value = df['one'])

         5. Column Types:
                df.dtypes
                df['ColA'].astype(int)
                df['ColA'].astype(str)


    3. Rows:

        1.  selection by index:  
                df.loc[idx]

        2.  Filter rows by condition:    
                 df[df['A']==0];   
                 df[(df['A']==0) & (df['B']==0)]; 
                 df[(df['A']==0) | (df['B']==0)];
                 df[df['reports'].isin(report_list)];
                 df[df['year'].notnull()]; df[df['year'].isnull()];

        3.  Query String:
            # Showing only the rows where year is greater than 2012 OR name is "Frank":
            df.query('year > 2012 | name == "Frank" ')

        4. Adding a new row at a specific index (between index 2 and 3):
            new_line = pd.DataFrame({...}, index = [2.5])
            df = df.append(line, ignore_index = False)
            df = df.sort_index().reset_index(drop=True)

        5. Adding another dataframe at the bottom (Append):
            df = df.append(df2)


    4. Selection and Slicing using .loc and .iloc:
        
        1. By position - .iloc
            df.iloc[3] # row
            df.iloc[3:5, 0:2]
            df.iloc[[1,2,4],[0,2]]
        
        2. By label - .loc, .at 
            df.loc[[0],['Country']]
            df.at[[0],['Country']]

        3. Slice by row:
            df[index1:index4]


    5. Index Object of a DataFrame (df.index)

        1. Index Object Function:
            df.index
            df.index.values  # return an array representing the data in the index
            df.index.is_monotonic  
            df.index.is_unique
            ...

        2. Index related function: 
            # Reset the index
            df.reset_index(drop = False, inplace = False)
            
            # Conform the index of df1 to that of df2 
            df1.reindex_list(df2)

            # Set the df index using existing columns:
            df.set_index('ColA'); df.set_index(['ColA','ColB'])

            # reindex the df with a different ordering of index:
            new_index = [1,3,5,7,9]
            df.reindex(new_index)


    6. Merge:

        1. Concatenating a sequence of dfs:
            result = pd.concat( [df1,df2], axis = 0, join='outer', ignore_index=False )
            result = df1.append(df2)
            result = df1.append( [df2, df3] )

        2. Join and Merge:
            
            pd.merge(left, right, how = 'inner', on = 'ColumnA', left_on='ColA', right_on='ColB', suffixes=('_x','-y'))

            left.join(right, on=key)


    7. Grouping:

        1. Simple Groupby:
            df.grouby('A').sum()
            df.groupby(['A','B']).count()
            df.groupby(['A','B']).agg( [np.mean, np.std ] )  # this will show two columns with mean and std

        2. Groupby intervals:
            # Groupby by df into intervals of length = A_intervals:
            df.groupby(df.A // A_intervals)

            # Return Percentiles:   
            def percentile(n):
                def percentile_(x):
                    return np.percentile(x, n)
                percentile_.__name__ = 'percentile_%s' % n
                return percentile_

            df.groupby(['A','B']).agg( [np.mean, np.std, percentile(25), percentile(75) ] )

            # groupby the decile of a column:
            df['QI_decile'] = pd.qcut(df['QI'], 10, laels = range(10))
            df.grouby(['QI_decile'])


    8. Pivot Table:

        1. Create a pivot table:
            pd.pivot_table( df, values = 'ColD', index = ['ColA', 'ColB'], Columns=['ColC'] )







### Other Operations:
1. Viewing Data:

    df.head()
    df.tail(3)
    df.describe()
    df.index
    df.info()
    df.columns
    df.T  # Transposing


2. Convert df to numpy array:   

    df.to_numpy()


3. Sorting:    

    df.sort_index(axis = 1, ascending=False)
    df.sort_values(by =['col1,col2'], ascending=False, na_position = 'last', ignore_index = False)


4. Missing data:

    df.dropna(how='any')  # drop na
    df.fillna(value = 0)  # fill na with 0
    pd.isna(df)           # get a df of boolean

5. Loop through a dataframe:

    for row in df.itertuples():

