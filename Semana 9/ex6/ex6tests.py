from autotest import TestSet

import testrunners


def unorderedlists(exp,ans):
    try:
        return exp == sorted(sorted(p) for p in ans)
    except TypeError:
        return False


def in_range(exp,ans):
    lst11=[]
    for i in range(len(exp)):
        try:
            if abs(exp[i]-ans[i])<.001:
                lst11.append(1)
            else:
                return False
        except TypeError:
            return False
    return True

def print_in_range(exp,ans):
    try:
        ansList=ans.split()
        expList=exp.split()
        if abs(float(ansList[15])-float(expList[15]))<.001 and  abs(float(ansList[23])-float(expList[23]))<.001 and abs(float(ansList[31])-float(expList[31]))<.001:
            return True
        return False
    except TypeError:
        return False



def unordered(exp,ans):
    try:
        return type(exp)==type(ans) and sorted(exp) == sorted(ans)
    except TypeError:
        return False


defaults = {}



factorial_def={'modulename': 'ex6', 'fname': 'factorial', }
factorial_examples={ 'f1': {'args': [0], 'ans': [1], 'options': {'output': ''} },
                     'f2': {'args': [1], 'ans': [1], 'options': {'output': ''}},
                     'f3': {'args': [7], 'ans': [5040], 'options': {'output': ''}},
                     'f4': {'args': [10], 'ans': [3628800], 'options': {'output': ''}},

}

palindrome_def = {'modulename': 'ex6','fname': 'is_palindrome', }
palindrome_examples = {'palindrome1': {'args': [[]], 'ans': [True], 'options': {'output': ''} },
                      'palindrome2': {'args': [[1,4,'g','g',4,1]], 'ans': [True], 'options': {'output': ''} },
                      'palindrome3': {'args': [['a','c','v']], 'ans': [False], 'options': {'output': ''} },
       }




sum_of_digits_def={'modulename': 'ex6', 'fname': 'sum_of_digits', }
sum_of_digits_examples={ 's1': {'args': [0], 'ans': [0], 'options': {'output': ''} },
                         's2': {'args': [123], 'ans': [6], 'options': {'output': ''}},
                         's3': {'args': [720], 'ans': [9], 'options': {'output': ''}},
                         's4': {'args': [5142], 'ans': [12], 'options': {'output': ''}},

}


convert_binary_def={'modulename': 'ex6', 'fname': 'convert_binary', }
convert_binary_examples={
                         'cb1': { 'runner': testrunners.print_runner,'args': [13], 'ans': ['1101\n'], },
                         'cb2': { 'runner': testrunners.print_runner,'args': [100], 'ans': ['1100100\n'],},
                         'cb3': { 'runner': testrunners.print_runner,'args': [52], 'ans': ['110100\n'],},
                         'cb4': { 'runner': testrunners.print_runner,'args': [0], 'ans': ['0\n'],},

}






nested_list_sum_def={'modulename': 'ex6', 'fname': 'nested_list_sum', }
nested_list_sum_examples={ 'nls1': {'args': [[[0,1],2,[3,4],5]], 'ans': [15], 'options': {'output': ''} },
                         'nls2': {'args': [[[[[1]]]]], 'ans': [1], 'options': {'output': ''}},
                         'nls3': {'args': [[[[1,2,3],4],5]], 'ans': [15], 'options': {'output': ''}},
                         'nls4': {'args': [[1,[[[[2]]]]]], 'ans': [3], 'options': {'output': ''}},

}


coin_pick_winner_def={'modulename': 'ex6', 'fname': 'coin_pick_winner', }
coin_pick_winner_examples={
                        'cpw1': {'args': [3], 'ans': [(False,2)], 'options': {'output': ''} },
                        'cpw2': {'args': [4], 'ans': [(True,2)], 'options': {'output': ''} },
                        'cpw3': {'args': [5], 'ans': [(True,1)], 'options': {'output': ''} },
                        'cpw4': {'args': [12], 'ans': [(False,3)], 'options': {'output': ''} },
                        'cpw5': {'args': [8], 'ans': [(True,1)], 'options': {'output': ''} },
                        'cpw6': {'args': [10], 'ans': [(True,2)], 'options': {'output': ''} },
                    }



tsets = {
         'factorial': TestSet(factorial_def, factorial_examples),
         'palindrome': TestSet(palindrome_def, palindrome_examples),
         'sum_of_digits': TestSet(sum_of_digits_def, sum_of_digits_examples),
         'convert_binary': TestSet(convert_binary_def, convert_binary_examples),
         'nested_list': TestSet(nested_list_sum_def, nested_list_sum_examples),
         'coin_pick_winner': TestSet(coin_pick_winner_def, coin_pick_winner_examples),
         }