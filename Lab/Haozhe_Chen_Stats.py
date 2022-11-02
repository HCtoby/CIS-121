import statistics

def median(data):
    result_median = statistics.median(data)
    return result_median

def mean(data):
    result_mean = statistics.mean(data)
    return result_mean

def mode(data):
    result_mode = statistics.multimode(data)
    return result_mode