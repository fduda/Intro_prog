from autotest import TestSet

import testrunners
import copy

def unorderedlists(exp,ans):
    try:
        return exp == sorted(sorted(p) for p in ans)
    except TypeError:
        return False


def in_range(exp,ans):
    lst11=[]
    for i in range(len(exp)):
        try:
            if i>1 and exp[i]!=ans[i]:
                return False
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
        copyAns=copy.deepcopy(ansList)
        copyExp=copy.deepcopy(expList)

        copyAns[15]='aaa'
        copyExp[15]='aaa'
        copyAns[23] = 'aaa'
        copyExp[23] = 'aaa'
        copyAns[31] = 'aaa'
        copyExp[31] = 'aaa'

        if copyAns != copyExp:
            return False

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

fancy_mean_def = {'modulename': 'ex3', }
fancy_mean_examples = {'fm1': {'fname': 'fancy_mean',
                     'runner': testrunners.print_runner,
                     'options': {'input': '4\n9\n\n', },
                     'args': [],
                    'comparemethod':print_in_range,
                     'ans': ["Please enter the numbers, one in each line:\n"
                             "The arithmetic mean of the numbers is 6.5\n"
                             "The geometric mean of the numbers is 6.0\n"
                             "The harmonic mean of the numbers is 5.538461538461538\n",],
                     },
                      'fm2': {'fname': 'fancy_mean',
                      'runner': testrunners.print_runner,
                      'options': {'input': '1\n2\n3\n\n', },
                      'args': [],
                      'comparemethod': print_in_range,
                       'ans': ["Please enter the numbers, one in each line:\n"
                             "The arithmetic mean of the numbers is 2.0\n"
                             "The geometric mean of the numbers is 1.8171205928321397\n"
                             "The harmonic mean of the numbers is 1.6363636363636365\n",],
                     },
                      'fm3': {'fname': 'fancy_mean',
                      'runner': testrunners.print_runner,
                      'options': {'input': '0.5\n1\n4\n3\n\n', },
                      'args': [],
                      'comparemethod': print_in_range,
                       'ans': ["Please enter the numbers, one in each line:\n"
                             "The arithmetic mean of the numbers is 2.125\n"
                             "The geometric mean of the numbers is 1.5650845800732873\n"
                             "The harmonic mean of the numbers is 1.1162790697674418\n",],
                     },
             }



palindrome_def = {'modulename': 'ex3',
           'fname': 'is_palindrome', }
palindromes = {'palindrome1': {'args': [[]], 'ans': [True], 'options': {'output': ''} },
               'palindrome2': {'args': [[1,4,'g','g',4,1]], 'ans': [True], 'options': {'output': ''} },
               'palindrome3': {'args': [['a','c','v']], 'ans': [False], 'options': {'output': ''} },
       }

lucky_tosses_def = {'modulename': 'ex3',
           'fname': 'lucky_tosses', }
lucky_examples = {'lucky1': {'args': [[1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1]],
                             'ans': [[57.69230769230769, 42.30769230769231,2,7]],
                              'comparemethod':in_range,
                              'options': {'output': ''},
                             },
                  'lucky2': {'args': [[1,1,0,0,1,1,1,1,0,0,0,1,1,1]],
                             'ans': [[64.28571428571429, 35.714285714285715, 0, 4]],
                              'comparemethod':in_range,
                              'options': {'output': ''}
                             },
                  }


cumulative_distribution_def = {'modulename': 'ex3',
           'fname': 'cumulative_distribution', }
cumulative_examples = {'cumulative1': {'args': [[1],[0]],
                             'ans': [ [0]],
                              'options': {'output': ''},
                             },
                        'cumulative2': {'args': [[1],[1.5]],
                             'ans': [ [1]],
                              'options': {'output': ''},
                             },
                        'cumulative3': {'args': [[1],[0,1.5]],
                             'ans': [ [0,1]],
                              'options': {'output': ''},
                             },

                        'cumulative4': {'args': [[1,2.2],[0,1.5]],
                             'ans': [ [0,0.5]],
                              'options': {'output': ''},
                             },
                       'cumulative5': {'args': [[1, 2.2], [0, 1.5, 2.1, 2.2]],
                                       'ans': [[0, 0.5, 0.5, 1.0]],
                                       'options': {'output': ''},
                                       },

                       'cumulative6': {'args': [[1, 2,3,4], [0, 0.5, 1, 2, 3, 4]],
                                       'ans': [[0, 0, 0.25, 0.5, 0.75, 1.0]],
                                       'options': {'output': ''},
                                       },
                  }



product_pairs_def = {'modulename': 'ex3',
           'fname': 'equal_product_pairs', }
product_examples = {'product1': {'args': [6],
                             'ans': [[[2,3]]],
                             'comparemethod':unorderedlists,
                             'options': {'output': ''},
                             },

                    'product2': {'args': [5],
                             'ans': [[]],
                             'comparemethod':unorderedlists,
                             'options': {'output': ''},
                             },

                    'product3': {'args': [9],
                             'ans': [[[3,3]]],
                             'comparemethod':unorderedlists,
                             'options': {'output': ''},
                             },

                    'product4': {'args': [36],
                             'ans': [[[2,18],[3,12],[4,9],[6,6]]],
                             'comparemethod':unorderedlists,
                             'options': {'output': ''},
                             },

                  }






pascal_def = {'modulename': 'ex3',
           'fname': 'pascal_triangle', }
pascal_examples = {'pas1': {'args': [1],
                             'ans': [[[1]]],
                              'options': {'output': ''},
                             },
                    'pas2': {'args': [2],
                             'ans': [[[1],[1,1]]],
                              'options': {'output': ''},
                             },
                    'pas3': {'args': [3],
                             'ans': [[[1],[1,1],[1,2,1]]],
                              'options': {'output': ''},
                             },
                    'pas4': {'args': [4],
                             'ans': [  [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]  ],
                              'options': {'output': ''},
                             },


                  }


tsets = {
         'fancy_mean': TestSet(fancy_mean_def, fancy_mean_examples),
         'is_palindrome': TestSet(palindrome_def, palindromes),
         'lucky tosses': TestSet(lucky_tosses_def, lucky_examples),
         'cumulative_distribution': TestSet(cumulative_distribution_def, cumulative_examples),
         'equal_product_pairs':TestSet(product_pairs_def, product_examples),
         'pascal':TestSet(pascal_def, pascal_examples),
         }