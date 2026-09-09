def seasonal_average(series: list, period: int) -> list:
    """
    Returns the average for each position in the seasonal cycle.
    """
    # Write code here
    l = [0]*period
    avgDenom = len(series)/period
    for i in range(0,len(series)):
        l[i%period]+=series[i] *1.0/avgDenom 
    return(l)