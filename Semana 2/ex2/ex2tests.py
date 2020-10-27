from autotest import TestSet

import testrunners



def num_in_range(exp,ans):
    epsilon=0.0001
    try:
        if abs(exp-ans)<epsilon:
            return True
        return False
    except TypeError:
        return False

def in_range(exp,ans):
    epsilon = 0.0001
    lst11=[]
    for i in range(len(exp)):
        try:
            if abs(exp[i]-ans[i])>epsilon:
                return False
        except TypeError:
            return False
    return True



def print_in_range(exp,ans):
    epsilon = 0.0001
    try:
        ansList=ans.split(' ')
        expList=exp.split(' ')
        if expList[:-1]!=ansList[:-1]:
            return False
        ansNum=float(ansList[len(ansList)-1].replace('\n',''))
        expNum=float(expList[len(expList)-1].replace('\n',''))
        if abs(ansNum-expNum)>epsilon:
            return False
    except TypeError:
        return False
    return True










defaults = {}

mean = {'mean': {'modulename': 'compute_mean',
                 'fname': 'compute_mean',
                 'args': [2, 3, 'H'], 'ans': [2.4],
                 'comparemethod': num_in_range,
                 },
        }
nat_lang = {'nat_lang': {'modulename': 'natural_language_compute_mean',
                         'fname': 'natural_language_compute_mean',
                         'args': ['Compute arithmetic mean of 5,7'], 'ans': [(5, 7, 6), (5, 7, 6.0), ],
                         'comparemethod': in_range,
                         },
      }


user_mean_def = {'modulename': 'user_input_compute_mean', }
user_mean = {'us1': {'fname': 'user_input_compute_mean',
                     'runner': testrunners.print_runner,
                     'comparemethod': print_in_range,
                     'options': {'input': '5 7\nA\n', },
                     'args': [],
                     'ans': ["Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             "The arithmetic mean of 5 and 7 is 6\n",
                             #"Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             #"The arithmetic mean of 5 and 7 is 6.0\n",
                             #"Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             #"The arithmetic mean of 5 and 7 is 6.000000\n",
                             ],
                     },
             'us2': {'fname': 'user_input_compute_mean',
                     'runner': testrunners.print_runner,
                     'comparemethod': print_in_range,
                     'options': {'input': '5 7\nG\n'},
                     'args': [],
                     'ans': ["Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             "The geometric mean of 5 and 7 is 5.91608\n",
                             #"Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             #"The geometric mean of 5 and 7 is 5.916080\n",
                             #"Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             #"The geometric mean of 5 and 7 is 5.916079783099616\n",
                             ],
                     },
             'us3': {'fname': 'user_input_compute_mean',
                     'runner': testrunners.print_runner,
                     'comparemethod': print_in_range,
                     'options': {'input': '3 8\nH\n'},
                     'args': [],
                     'ans': ["Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             "The harmonic mean of 3 and 8 is 4.363636\n",
                             #"Please enter two numbers, x and y: Please enter (A)rithmetic, (G)eometric or (H)armonic: "
                             #"The harmonic mean of 3 and 8 is 4.363636363636364\n",
                      ],
                     },
             }
win_def = {'modulename': 'is_first_player_winner',
           'fname': 'is_first_player_winner', }


win = {'win_6_8_3_7': {'args': [6, 8, 3, 7], 'ans': [True], },
       'win_6_11_3_13': {'args': [6, 11, 3, 13], 'ans': [True], },
       }


fancy_def = {'modulename': 'fancy_arithmetic_mean',
             'fname': 'fancy_arithmetic_mean', }
fan = {'right_uses': {'runner': testrunners.print_runner,
                      'comparemethod': print_in_range,
                      'options': {'input': '2\n10\n30\n', },
                      'ans': ['Please enter a number of numbers (1-5): Please enter the numbers, one in each line \nThe arithmetic mean of the numbers is 20\n',
                              #'Please enter a number of numbers (1-5): Please enter the numbers, one in each line \nThe arithmetic mean of the numbers is 20\n',
                              #'Please enter a number of numbers (1-5): Please enter the numbers, one in each line\nThe arithmetic mean of the numbers is 20.0\n',
                              #'Please enter a number of numbers (1-5): Please enter the numbers, one in each line\nThe arithmetic mean of the numbers is 20\n',
                       ]
                      },
       'wrong_uses': {'runner': testrunners.print_runner,
                      'options': {'input': '7\n', },
                      'ans': ['Please enter a number of numbers (1-5): The number you entered is not between 1 and 5, goodbye!\n', ],
                      }

       }


tsets = {'compute_mean': TestSet({}, mean),
         'natural_language_compute_mean': TestSet({}, nat_lang),
         'user_input_compute_mean': TestSet(user_mean_def, user_mean),
         'is_first_player_winner': TestSet(win_def, win),
         'fancy_arithmetic_mean': TestSet(fancy_def, fan),
         }
