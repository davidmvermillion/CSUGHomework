import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pickle
import scipy.stats as stats
import statsmodels.stats.api as sms
import numpy as np


# https://pynative.com/python-write-list-to-file/#h-pickle-module-to-write-serialize-list-into-a-file
# https://www.w3schools.com/python/gloss_python_string_concatenation.asp
def read_list(name):
    # for reading also binary mode is important
    with open('data/' + str(name) + '.pickle', 'rb') as fp:
        n_list = pd.DataFrame(pickle.load(fp))
        return n_list
    
def qqplot(variable, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig = sm.qqplot(variable, dist = stats.norm, fit=True, line='q', ax=ax)
    ax.set_title(str(title), fontsize = 23, pad = 15).set_color('#171819')
    for pos in ['right', 'top']:
        plt.gca().spines[pos].set_visible(False)
    ax.get_lines()[0].set_markerfacecolor('#2d3047')
    ax.get_lines()[0].set_markeredgewidth(0)
    ax.get_lines()[1].set_color('#e34234')
    ax.get_lines()[1].set_linewidth(2)
    ax.get_lines()[1].set_solid_capstyle('round')
    ax.spines['bottom'].set_color('#A0A0A0')
    ax.spines['left'].set_color('#A0A0A0')
    ax.tick_params(axis='y', which='both', right=False,
                left=False, colors = '#686868')
    ax.tick_params(axis='x', which='both', top=False, 
                bottom=False, colors = '#686868')
    ax.set_xlabel('Theoretical Quantiles', fontsize = 12, loc =
                'left').set_color('#707070')
    ax.set_ylabel('Sample\nQuantiles', fontsize = 12, rotation =
                'horizontal', loc = 'bottom', labelpad =
                55).set_color('#707070')
    
# AFIT DASC 512 - 24 - Analysis of Variance
def anova(model):
    at = sms.anova_lm(model, typ=2)
    at['mean_sq'] = at['sum_sq'] / at['df']
    at = at.reindex(['df','sum_sq','mean_sq','F','PR(>F)'],axis=1)
    return at

# AFIT DASC 512 - 23 - Tests of Variability
def chi2_1samp_var_stats(s2, sigma2, n, alternative='two-sided'):
    '''
    This function runs the one-sample chi-squared test for variance
    based on known values. Use chi2_1samp_var_data if you have raw
    data rather than summary statistics.
    
    Inputs:
    s2     : the observed variance
    sigma2 : the null hypothesized variance
    n      : the sample size
    alternative : the alternative hypothesis ('two-sided', 'greater', 'less')
    
    Returns:
    test   : the chi-squared test statistic
    pval   : the p-value for the test
    '''
    dist = stats.chi2(df=n-1)
    test = (n-1) * s2 / sigma2
    pval = 0
    if alternative == 'less':
        pval = dist.cdf(test)
    elif alternative == 'greater':
        pval = dist.sf(test)
    else:
        pval = 2 * min(dist.cdf(test),dist.sf(test))
    return test, pval

def chi2_1samp_var_data(data, sigma2, alternative='two-sided'):
    '''
    This function runs the one-sample chi-squared test for variance
    based on given data. Use chi2_1samp_var_stats if you know values
    but do not have the raw data.
    
    Inputs:
    data   : the observed data
    sigma2 : the null hypothesized variance
    alternative : the alternative hypothesis ('two-sided', 'greater', 'less')
    
    Returns:
    test   : the chi-squared test statistic
    pval   : the p-value for the test
    '''
    s2 = np.var(data, ddof=1)
    n = len(data)
    dist = stats.chi2(df=n-1)
    test = (n-1) * s2 / sigma2
    pval = 0
    if alternative == 'less':
        pval = dist.cdf(test)
    elif alternative == 'greater':
        pval = dist.sf(test)
    else:
        pval = 2 * min(dist.cdf(test),dist.sf(test))
    return test, pval

def F_2samp_var_stats(var1, var2, n1, n2, alternative='two-sided'):
    '''
    This function runs the two-sample F test for variance based on
    known values. Use F_2samp_var_data if you have raw data.
    
    Inputs:
    var1     : the observed variance for sample 1
    var2     : the observed variance for sample 2
    n1       : the sample size for sample 1
    n2       : the sample size for sample 2
    alternative : the alternative hypothesis ('two-sided', 'greater', 'less')
    
    Returns:
    test   : the F test statistic
    pval   : the p-value for the test
    '''
    dist = stats.f(dfn=n1-1, dfd=n2-1)
    test = var1/var2
    pval = 0
    if alternative == 'less':
        pval = dist.cdf(test)
    elif alternative == 'greater':
        pval = dist.sf(test)
    else:
        pval = 2 * min(dist.cdf(test),dist.sf(test))
    return test, pval

def F_2samp_var_data(data1, data2, alternative='two-sided'):
    '''
    This function runs the two-sample F test for variance based on
    raw data. Use F_2samp_var_stats if you have summary statistics.
    
    Inputs:
    data1   : sample 1
    data2   : sample 2
    alternative : the alternative hypothesis ('two-sided', 'greater', 'less')
    
    Returns:
    test   : the F test statistic
    pval   : the p-value for the test
    '''
    var1 = np.var(data1, ddof=1)
    var2 = np.var(data2, ddof=1)
    n1 = len(data1)
    n2 = len(data2)
    dist = stats.f(dfn=n1-1, dfd=n2-1)
    test = var1/var2
    pval = 0
    if alternative == 'less':
        pval = dist.cdf(test)
    elif alternative == 'greater':
        pval = dist.sf(test)
    else:
        pval = 2 * min(dist.cdf(test),dist.sf(test))
    return test, pval