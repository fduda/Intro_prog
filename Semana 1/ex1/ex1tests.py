from autotest import TestSet

import testrunners


def print_in_range(exp,ans):
    epsilon = 0.001
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



defaults = {'modulename':'math_print',}

cases = {'cos':{'fname':'cos_45',
               'runner':testrunners.print_runner,'comparemethod': print_in_range,
               'ans':["0.5253219888177297\n"],
           },
         'log':{'fname':'natural_log_20',
               'runner':testrunners.print_runner,'comparemethod': print_in_range,
               'ans':["2.995732273553991\n"],
           },
         'triangle':{'fname':'triangle_area_3x12',
               'runner':testrunners.print_runner,'comparemethod': print_in_range,
               'ans':["18.0\n",
                      "18\n",],
           },
        }

tsets = {'ex1':TestSet({},cases),
}
