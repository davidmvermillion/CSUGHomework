import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pickle
import scipy.stats as stats
import statsmodels.stats.api as sms


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