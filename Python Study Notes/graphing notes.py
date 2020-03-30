
### subplot with line graphs:

    # Setup figure:
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (10,5))
    plt.setp(axes, xticks=[1, 3, 5, 7, 9 ], xticklabels=['1st', '3rd' , '5th', '7th', '9th'])

    # An alternative to set x axis value:
    plt.xticks([10,12,14,16],['10:00', '12:00', '14:00','16:00'])


    # Plot lines from df:
    df_time.plot(ax=axes[0],x='qi_decile', y='mean')
    df_prob.plot(ax=axes[1],x='qi_decile', y='mean')

    # Draw bands from 25 percentile to 75 percentile using fill_between
    axes[0].fill_between(df_time['qi_decile'], df_time['percentile_25'], df_time['percentile_75'], alpha = 0.3)

    # Set x,y label:
    axes[0].set_xlabel('Queue Imbalance Decile')
    axes[1].set_xlabel('Queue Imbalance Decile')
    axes[0].set_ylabel('Fill Time (Second)')
    axes[1].set_ylabel('Fill Probability')
    axes[0].get_legend().remove()
    axes[1].get_legend().remove()
    
    plt.xlabel('Time', fontsize = 12)
    plt.ylabel('Price', fontsize = 12)

    # Remove legend:
    axes[0].get_legend().remove()
    axes[1].get_legend().remove()

### Plot horzontal lines:
    plt.hlines(y = syn_fill['price'], xmin = syn_fill['time'], xmax = syn_fill['fill time'], color='green', label = 'Fill Time')




### Histogram (Density) Plot:
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
    sns.distplot(df_rn['q_imbal'], bins = 100, kde=False, norm_hist=True, ax=axes[0])
    sns.distplot(df_trade['q_imbal'], bins = 100, kde=False, norm_hist=True, ax=axes[1])



### 3D graphs:
fig = plt.figure()
ax = fig.gca(projection='3d')

x = Q_table[Q_table['M']!=1]['M'].unique()
y = Q_table[Q_table['M']!=1]['QI_interval'].unique()
x2, y2 = np.meshgrid(x,y)
z = scipy.interpolate.griddata((Q_table['M'], Q_table['QI_interval']), Q_table['Continue_Value'], (x2, y2), method='cubic')
surf = ax.plot_surface(x2, y2, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)



### Save figure with tight margin:
   plt.savefig('../qi_pattern_'+graph_type+'.pdf', bbox_inches = 'tight')


