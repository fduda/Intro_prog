from autotest import TestSet

import testrunners

defaults = {'modulename':'math_print',}

cases = {'cos':{'fname':'cos_45',
               'runner':testrunners.print_runner,
               'ans':["0.5253219888177297\n"],
           },
         'log':{'fname':'natural_log_20',
               'runner':testrunners.print_runner,
               'ans':["2.995732273553991\n"],
           },
         'triangle':{'fname':'triangle_area_3x12',
               'runner':testrunners.print_runner,
               'ans':["18.0\n",
                      "18\n",],
           },
        }

tsets = {'ex1':TestSet({},cases),
}
