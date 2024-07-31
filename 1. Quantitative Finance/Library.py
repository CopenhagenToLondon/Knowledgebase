###############################################################################
#                        Slopes, returns and accelerations
#                        For calculating import 
#                        intra and inter day differences
###############################################################################

def slope(array):
    """
    """
    y = np.array(array)
    x = np.arange(len(y))
    slopes, intercept, r_value, p_value, std_err = linregress(x,y)
    return(slopes)

def returns(x, logs = False):
    """
    """
    if type(x) == list: # if you've entered a list
        _return = np.zeros(len(x))
        for i in range(len(x)):
            _return[i] = ((x[i]/x[i-1])-1)
    elif type(x) == pd.DataFrame: # if you've entered a dataframe
        _return = x.pct_change().dropna()   
    else: # if you've entered neither a list or a dataframe
        _return = x.pct_change().dropna()
    
    # if you want log returns
    if logs == True:
        _return = np.log(abs(_return))
    
    df = pd.DataFrame(data=_return, dtype=np.float64)
    df.columns = ["returns"]
    return(df)

def acceleration(x, logs = False):
    """
    """
    x = returns(x, logs)
    if type(x) == list:  # if you've entered a list
        acc = np.zeros(len(x))
        for i in range(len(x)):
            acc[i] = ((x[i]/x[i-1])-1)
    elif type(x) == pd.DataFrame: # if you've entered a dataframe
        acc = x.pct_change().dropna() 
    else: # if you've entered neither a list or a dataframe
        acc = x.pct_change().dropna()
        
     # if you want log acceleration  
    if logs == True:
        acc = np.log(abs(acc))
    
    df = pd.DataFrame(data=acc, dtype=np.float64)
    df.columns = ["acceleration"]
    return(df)



###############################################################################
#                        Moving averages and stds
#                        volume weighted averages and stds
#                        bollinger bands?
###############################################################################

# Time-weighted Moving Average
def twa(data, window = 20, typ = "sma", x = True):
    """
    time-weighted moving average
    """
    if typ == "sma": # simple moving average
        if len(data) < window+1:
            raise ValueError("not enough data")
            
        if x == True:
            
            df = []
            for i in range(len(data)):
                if i < window:
                    df.append(data[i])
                else:
                    df.append(np.mean(data[i-window:i]))

            df = pd.DataFrame(df, index = data.index)
            df = df.iloc[0:len(df), 0]
            return(df)
    
        elif x == False:

            df = []
            for i in range(len(data)):

                ma = np.zeros(window)

                for j in range(1,window):

                    if i < window:
                        ma[j] = data[j]


                    if i >= window:

                        ma[j] = np.mean(data[i-j:i])

                df.append(ma)

            df = pd.DataFrame(df, index = data.index)
            df = df.iloc[0:len(df), 1:len(df.columns)]
            return(df)
    
    elif typ == "ema": # exponential moving average

        df = pd.DataFrame(index=data.index, dtype=np.float64)
        df.loc[:,0] = data.ewm(span=window, min_periods=0, adjust=True, ignore_na=False).mean().values.flatten() # ????
    
        return(df)
      
#Time-Price Moving STD
def twstd(data, window = 20, x = True):
    """
    time-weighted moving standard deviation of prices
    also called volatility
    """
    if len(data) < window+1:
        raise ValueError("not enough data")

    if x == True:
        
        df = []
        for i in range(len(data)):
            if i < window:
                df.append(data[i])
            else:
                df.append(np.std(data[i-window:i]))

        df = pd.DataFrame(df, index = data.index)
        df = df.iloc[0:len(df), 0]
        return(df)
        
    elif x == False:  
        
        df = []
        for i in range(len(data)):

            mstd = np.zeros(window)

            for j in range(1,window):

                if i >= j:

                    mstd[j] = np.std(data[i-j:i])

            df.append(mstd)

        df = pd.DataFrame(df, index = data.index)
        df = df.iloc[0:len(df), 1:len(df.columns)]
    
        return(df)

# Time-Returns Moving Average
def twa_r(data, window = 21):
    """
    time-weighted moving average of returns
    """
    
    result = list(np.zeros(window))
    for i in range(window,len(data)):
        result.append(np.mean(data[i-window:i]))
    return(result)

#Time-returns Moving STD
def twstd_r(data, window = 21):
    """
    """    
    result = list(np.zeros(window))
    for i in range(window,len(data)):
        result.append(np.std(data[i-window:i]))
    return(result)

    
    
# Volume-weighted Moving Average
def vwa(data, weights, window = 20):
    """
    volume-weighted moving average
    """
    
    v_w_vel = 0
    lst = np.zeros(window)
    lst = list(lst)
    for i in range(window, len(data)):
        v_sum = sum(data.iloc[i-window:i,4])
        v_w_vel = 0
        for j in range(window):
            v_w_vel = v_w_vel + data.iloc[i-j,3] * (data.iloc[i-j,4] / v_sum)

        lst.append(v_w_vel)
    return(lst)

#Volume-Price Moving STD


#Volume-Returns Moving Average
def vwa_r(data, window = 21):
    """
    volume-weighted moving average of returns
    """
    assert data.columns[7] == "velocity"
    assert data.columns[4] == "Volume"

    v_w_vel = 0
    lst = np.zeros(window)
    lst = list(lst)
    for i in range(window, len(data)):
        v_sum = sum(data.iloc[i-window:i,4])
        v_w_vel = 0
        for j in range(window):
            v_w_vel = v_w_vel + data.iloc[i-j,7] * (data.iloc[i-j,4] / v_sum)

        lst.append(v_w_vel)
    return(lst)



#Volume-Returns Moving STD?
