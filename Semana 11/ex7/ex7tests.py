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



def perimeter_wrapper(x,y):
    try:
        import polygon
        pp = polygon.Polygon(x, y)
        p = copy.deepcopy(pp)
        return p.perimeter()
    except TypeError:
        return False


def convex_wrapper(x,y):
    try:
        import polygon
        pp=polygon.Polygon(x,y)
        p=copy.deepcopy(pp)
        return p.is_convex()
    except TypeError:
        return 10


def translate_wrapper(x,y,movex,movey):
    try:
        import polygon
        p=polygon.Polygon(x,y)
        pp=copy.deepcopy(p)
        pp.translate(movex,movey)
        temp=pp.get_vertices()
        return temp[0],temp[1]
    except TypeError:
        return False

def rotate_wrapper(x,y,alpha):
    try:
        import polygon
        pp=polygon.Polygon(x,y)
        p=copy.deepcopy(pp)
        p.rotate(alpha)
        temp = p.get_vertices()
        return temp[0], temp[1]
    except TypeError:
        return False


def eq_wrapper(x1,y1,x2,y2):
    try:
        import polygon
        pp1=polygon.Polygon(x1,y1)
        pp2=polygon.Polygon(x2,y2)
        p1 = copy.deepcopy(pp1)
        p2 = copy.deepcopy(pp2)
        temp = p1==p2
        #print(temp)
        return temp
    except TypeError:
        return 10

def cong_wrapper(x1,y1,x2,y2):
    try:
        import polygon
        pp1=polygon.Polygon(x1,y1)
        pp2=polygon.Polygon(x2,y2)
        p1 = copy.deepcopy(pp1)
        p2 = copy.deepcopy(pp2)
        temp = p1.is_congruent(p2)
        #print(temp)
        return temp
    except TypeError:
        return 10


def intersect_wrapper(x1,y1,i,j):
    try:
        import polygon
        pp1=polygon.Polygon(x1,y1)
        p1 = copy.deepcopy(pp1)
        return p1.intersect(i,j)
    except TypeError:
        return 10

def isvalid_wrapper(x1,y1):
    try:
        import polygon
        pp1=polygon.Polygon(x1,y1)
        p1 = copy.deepcopy(pp1)
        return p1.is_valid()
    except TypeError:
        return 10

def area_wrapper(x1,y1):
    try:
        import polygon
        pp1=polygon.Polygon(x1,y1)
        p1 = copy.deepcopy(pp1)
        return p1.area()
    except TypeError:
        return False


def cent_wrapper(x1,y1):
    try:
        import polygon
        pp1=polygon.Polygon(x1,y1)
        p1 = copy.deepcopy(pp1)
        return p1.centroid()
    except TypeError:
        return False


defaults = {}

perimeter_def = {'modulename': 'ex7tests', }
perimeter_examples = {'fm1': {'fname': 'perimeter_wrapper',
                              'args': [[1,8,9],[1,10,-3]],
                             'ans': [33.3844 ],
                              'options': {'output': ''} ,
                             'comparemethod':num_in_range, },
                    'fm2': {'fname': 'perimeter_wrapper',
                              'args': [[11.1,82.2,93.3,24.4],[14.5,105.6,-36.7,-12.8]],
                             'ans': [361.5885075521438 ],
                              'options': {'output': ''} ,
                             'comparemethod':num_in_range, },
                        }

convex_def = {'modulename': 'ex7tests', }
convex_examples = {'fm1': {'fname': 'convex_wrapper',
                              'args': [[1,8,9],[1,10,-3]],
                             'ans': [True ],
                              'options': {'output': ''} ,
                              },
                    'fm2': {'fname': 'convex_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20]],
                             'ans': [False ],
                              'options': {'output': ''} ,
                              },
                        }

translate_def = {'modulename': 'ex7tests', }
translate_examples = {'fm1': {'fname': 'translate_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],1,2],
                             'ans': [ (  [-9, 31, 61, 41],[-8, 32, 12, 22])],
                              'options': {'output': ''} ,
                             'comparemethod':tuple_list_in_range,
                                },
                    'fm2': {'fname': 'translate_wrapper',
                              'args': [[11.1,82.2,93.3,24.4],[14.5,105.6,-36.7,-12.8],20,30],
                              'ans': [  ([31.1, 102.2, 113.3, 44.4], [44.5, 135.6, -6.7, 17.2])  ],
                              'options': {'output': ''} ,
                              'comparemethod':tuple_list_in_range, },
                        }

rotate_def = {'modulename': 'ex7tests', }
rotate_examples = {'fm1': {'fname': 'rotate_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],.4],
                             'ans': [(  [-9.929943704074335, 29.789831112223, 59.928725239344075, 39.859400022256565], [-10.069568910033562, 30.208706730100694, 10.41863192493164, 20.278763026026358]  )],
                              'options': {'output': ''} ,
                             'comparemethod':tuple_list_in_range,
                                },
                    'fm2': {'fname': 'rotate_wrapper',
                              'args':  [[-10,30,60,40],[-10,30,10,20],-.4],
                              'ans': [(    [-10.069568910033565, 30.208706730100694, 60.0683504453033, 40.13865043417503], [-9.929943704074331, 29.789831112223, 9.580880689176254, 19.720262202189435] ) ],
                              'options': {'output': ''} ,
                              'comparemethod':tuple_list_in_range, },
                   'fm3': {'fname': 'rotate_wrapper',
                           'args': [[-10, 30, 60, 40], [-10, 30, 10, 20], 100],
                           'ans': [  (    [11.584559306791382, -34.75367792037416, -20.26696819013789, -26.64208216692137], [-8.111595753452782, 24.334787260358326, 57.35198340406319, 35.919346567149724]   )  ],
                           'options': {'output': ''},
                           'comparemethod': tuple_list_in_range, },
                        }




eq_def = {'modulename': 'ex7tests', }
eq_examples = {'fm1': {'fname': 'eq_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],[60,-10,40,30],[10,-10,20,30]],
                              'ans': [False],
                              'options': {'output': ''} ,
                                },
                'fm2': {'fname': 'eq_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],[60,40,-10,30],[10,20,-10,30]],
                              'ans': [True],
                              'options': {'output': ''} ,
                        },
               }


cong_def = {'modulename': 'ex7tests', }
cong_examples = {'fm1': {'fname': 'cong_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],[-10,30,60,40],[-10,30,10,4]],
                              'ans': [False],
                              'options': {'output': ''} ,
                                },
                'fm2': {'fname': 'cong_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],  [-6.895093830884443, 14.370612236884932, 49.7908089031445, 27.47540560000029], [-8.34372105617747, 44.07545239628396, 37.336782785485774, 38.75902587934161]],
                              'ans': [True],
                              'options': {'output': ''} ,
                        },
               }




intersect_def = {'modulename': 'ex7tests', }
intersect_examples = {'fm1': {'fname': 'intersect_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],1,2],
                              'ans': [True],
                              'options': {'output': ''} ,
                                },
                      'fm2': {'fname': 'intersect_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],1,3],
                              'ans': [False],
                              'options': {'output': ''} ,
                                },
                      'fm3': {'fname': 'intersect_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20],2,3],
                              'ans': [True],
                              'options': {'output': ''} ,
                                },
               }

isvalid_def = {'modulename': 'ex7tests', }
isvalid_examples = {'fm1': {'fname': 'isvalid_wrapper',
                              'args': [[-10,30,0],[-40,30,0]],
                              'ans': [True],
                              'options': {'output': ''} ,
                                },
                    'fm2': {'fname': 'isvalid_wrapper',
                              'args': [[-10,30,10],[-10,30,10]],
                              'ans': [False],
                              'options': {'output': ''} ,
                                },
                    'fm3': {'fname': 'isvalid_wrapper',
                              'args': [[-10,30,10,-20],[-10,30,10,0]],
                              'ans': [False],
                              'options': {'output': ''} ,
                                },
               }


area_def = {'modulename': 'ex7tests', }
area_examples = {'fm1': {'fname': 'area_wrapper',
                              'args': [[-10,30,60,40],[-10,30,10,20]],
                              'ans': [450],
                              'options': {'output': ''} ,
                            'comparemethod':num_in_range,
                                },
                    'fm2': {'fname': 'area_wrapper',
                              'args': [[-10.4, 30.4, 60.2, 40.01],[-10.4, 30.5, 10.2, 20.3]],
                              'ans': [459.04300],
                              'options': {'output': ''} ,
                        'comparemethod':num_in_range,
                                },

                    'fm4': {'fname': 'area_wrapper',
                              'args': [[-10.4, 30.4, 60.2],[-10.4, 30.5, 10.2]],
                              'ans': [1023.5300],
                              'options': {'output': ''} ,
                        'comparemethod':num_in_range,
                                },
                    }

cent_def = {'modulename': 'ex7tests', }
cent_examples = {'fm1': {'fname': 'cent_wrapper',
                              'args': [[-10.4, 30.4, 60.2],[-10.4, 30.5, 10.2]],
                              'ans':  [[26.733333333333334, 10.1]],
                              'options': {'output': ''} ,
                            'comparemethod':in_range,
                                },
                  'fm2': {'fname': 'cent_wrapper',
                              'args': [[-10.4, 30.4, 60.2, 40.01], [-10.4, 30.5, 10.2, 20.3]],
                              'ans': [[22.794181612615812, 14.280993501698099]],
                              'options': {'output': ''} ,
                            'comparemethod':in_range,
                                },
                    }




tsets = {
         'perimeter': TestSet(perimeter_def, perimeter_examples),
         'convex': TestSet(convex_def, convex_examples),
         'translate': TestSet(translate_def, translate_examples),
         'rotate': TestSet(rotate_def, rotate_examples),
         'eq': TestSet(eq_def, eq_examples),
         'cong': TestSet(cong_def, cong_examples),
         'intersect': TestSet(intersect_def, intersect_examples),
         'isvalid': TestSet(isvalid_def, isvalid_examples),
         'area': TestSet(area_def, area_examples),
         'cent': TestSet(cent_def, cent_examples),
}