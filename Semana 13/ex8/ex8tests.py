from autotest import TestSet

import testrunners
import copy

def unorderedlists(exp,ans):
    try:
        return exp == sorted(sorted(p) for p in ans)
    except TypeError:
        return False



def tuple_list_in_range(exp,ans):
    lst=[]
    try:
        for i in range(len(exp)):
            for j in range(len(exp[0])):
                lst.append(abs(exp[i][j]-ans[i][j]))
        if max(lst)<.0001:
            return True
        return False
    except TypeError:
        return False


def in_range(exp,ans):
    lst11=[]
    for i in range(len(exp)):
        try:
            if i>1 and exp[i]!=ans[i]:
                return False
            if abs(exp[i]-ans[i])<.0001:
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

        if abs(float(ansList[15])-float(expList[15]))<.0001 and  abs(float(ansList[23])-float(expList[23]))<.0001 and abs(float(ansList[31])-float(expList[31]))<.0001:
            return True
        return False
    except TypeError:
        return False

def num_in_range(exp,ans):
    epsilon=0.0001
    try:
        if abs(exp-ans)<epsilon:
            return True
        return False
    except TypeError:
        return False


def unordered(exp,ans):
    try:
        return type(exp)==type(ans) and sorted(exp) == sorted(ans)
    except TypeError:
        return False



def check_next_method(x,steps):
    try:
        import ex8_iterators
        iterator1=ex8_iterators.reverse_iter(x)
        sol=[]
        for i in range(steps):
            sol.append(iterator1.next())
        return sol
    except TypeError:
        return False



def fib_wrapper(x):
    try:
        import ex8_iterators
        iterator1=ex8_iterators.fibonacci()
        sol=[]
        for i in range(x):
            sol.append(next(iterator1))
        return sol
    except TypeError:
        return False



def bin_wrapper(x):
    try:
        import ex8_iterators
        iterator1=ex8_iterators.recursive_binary(x)
        sol=[]
        try:
            for i in range(x):
                sol.append(next(iterator1))
        except StopIteration:
            return sol
        return sol
    except TypeError:
        return False




def range_wrapper1(start,stop,jump,iters):
    try:
        import ex8_iterators
        iterator1=ex8_iterators.myRange(start,stop,jump)
        sol=[]
        for i in range(iters):
            try:
                sol.append(next(iterator1))
            except StopIteration:
                return sol
    except TypeError:
        return False
    return False


def range_wrapper2(start,stop,jump,iters):    #without stopIteration
    try:
        import ex8_iterators
        iterator1=ex8_iterators.myRange(start,stop,jump)
        sol=[]
        for i in range(iters):
            sol.append(next(iterator1))
    except TypeError:
        return False
    return sol


def card_wrapper():
    try:
        import ex8_iterators
        iterator1=ex8_iterators.take_card()
        sol=next(iterator1)
        if sol[0] in [1,2,3,4,5,6,7,8,9,10,11,12,13] and sol[1] in ['diamond','heart','club','spade']:
            return True
        return False
    except TypeError:
        return False


def card_wrapper_all():
    try:
        import ex8_iterators
        iterator1=ex8_iterators.take_card()
        sol=[]
        for i in range(52):
            sol.append(next(iterator1))
        for item1 in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
            for item2 in ['diamond','heart','club','spade']:
                if (item1,item2) not in sol:
                    return False
        return True
    except TypeError:
        return False


def diff_wrapper(func,delta,x):
    try:
        import ex8_2nd_order
        f=ex8_2nd_order.differential_function(func,delta)
        return f(x)
    except TypeError:
        return False

def integral_wrapper(func,x0,x1,segments):
    try:
        import ex8_2nd_order
        f=ex8_2nd_order.get_integral_func(x0,x1,segments)
        return f(func)
    except TypeError:
        return False

def inverse_wrapper(func,interval,epsilon,x):
    try:
        import ex8_2nd_order
        f=ex8_2nd_order.inverse(func,interval,epsilon)
        return f(x)
    except TypeError:
        return False






defaults = {}


fibonacci_def = {'modulename': 'ex8tests', }
fibonacci_examples = {'fm1': {'fname': 'fib_wrapper',
                              'args': [10],
                             'ans': [[1,1,2,3,5,8,13,21,34,55] ],
                              'options': {'output': ''} ,
                             },
                        }

bin_def = {'modulename': 'ex8tests', }
bin_examples = {'fm1': {'fname': 'bin_wrapper',
                              'args': [59],
                             'ans': [[1,1,1,0,1,1] ],
                              'options': {'output': ''} ,
                             },
                        }




card_def = {'modulename': 'ex8tests', }
card_examples = {'fm1': {'fname': 'card_wrapper',
                              'args': [],
                             'ans': [True ],
                              'options': {'output': ''} ,
                             },
                  'fm2': {'fname': 'card_wrapper_all',
                              'args': [],
                             'ans': [True ],
                              'options': {'output': ''} ,
                             },
                        }


diff_def = {'modulename': 'ex8tests', }
diff_examples = {'fm1': {'fname': 'diff_wrapper',
                              'args': [lambda x:x**2+2*x,.00001,1],
                             'ans': [4 ],
                            'comparemethod': num_in_range,
                              'options': {'output': ''} ,
                             },
                 'fm2': {'fname': 'diff_wrapper',
                          'args': [lambda x: x ** 2 + 2 * x, .00001, .35],
                          'ans': [2.6999999999999247],
                          'comparemethod': num_in_range,
                          'options': {'output': ''},
                          },
                        }





integral_def = {'modulename': 'ex8tests', }
integral_examples = {'fm1': {'fname': 'integral_wrapper',
                              'args': [lambda x:x**2,0,1,10000],
                             'ans': [.3333333 ],
                            'comparemethod': num_in_range,
                              'options': {'output': ''} ,
                             },
                    'fm2': {'fname': 'integral_wrapper',
                              'args': [lambda x:x**3+2*x**2+3*x+4,-1,1,10000],
                             'ans': [9.33333336000001 ],
                            'comparemethod': num_in_range,
                              'options': {'output': ''} ,
                             },
                        }


inverse_def = {'modulename': 'ex8tests', }
inverse_examples = {'fm1': {'fname': 'inverse_wrapper',
                              'args': [lambda x:x**3,[-1,1],.00001,.5],
                             'ans': [0.7936973571777344 ],
                            'comparemethod': num_in_range,
                              'options': {'output': ''} ,
                             },
                    'fm2': {'fname': 'inverse_wrapper',
                              'args': [lambda x:x**3,[-1,1],.00001,0],
                             'ans': [0 ],
                            'comparemethod': num_in_range,
                              'options': {'output': ''} ,
                             },
                        }



tsets = {
        'fibonacci': TestSet(fibonacci_def, fibonacci_examples),
        'binary': TestSet(bin_def, bin_examples),
        'card': TestSet(card_def, card_examples),
        'diff': TestSet(diff_def, diff_examples),
        'integral': TestSet(integral_def, integral_examples),
        'inverse': TestSet(inverse_def, inverse_examples),

}