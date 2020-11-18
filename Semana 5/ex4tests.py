
from autotest import TestSet
import testrunners

#func to check if unordered lists are the same
def unorderedlists(exp,ans):
    try:
        for i in range(len(exp)):
            x = exp[i]
            if exp[i] not in ans:
                return False

        if len(ans)!=len(exp):
            return False
        else:
            return True
    except TypeError:
        return False

#func to check if unordered lists are the same for q6
def unorderedlists2(exp,ans):
    ans = ans.split("\n")
    exp = exp.split("\n")
    try:
        for i in range(len(exp)):
            if exp[i] not in ans:
                return False

        if len(ans)!=len(exp):
            return False
        else:
            return True
    except TypeError:
        return False


###q7 help func1
def print_in_range(exp,ans):
    try:
        ansList=ans.split("\n")
        expList=exp.split("\n")
        h1 = ansList[2:4]
        h2= expList[2:4]

        f1=ansList[0:2]
        f2 = expList[0:2]

        l1 = ansList[4:]
        l2 = expList[4:]
        try:
            for i in range(len(h1)):
                if h1[i] not in h2:
                    return False

            if len(h2) != len(h1):
                return False
            if f1!=f2:
                return False
            if l1!=l2:
                return False
        except TypeError:
            return False



    except TypeError:
        return False
    return True


###q7 help func2
def print_in_range2(exp,ans):
    try:
        ansList=ans.split("\n")
        expList=exp.split("\n")

        f1=ansList[0:2]
        f2 = expList[0:2]

        l11 = ansList[4:6]
        l21 = expList[4:6]

        l12 = ansList[8:]
        l22 = expList[8:]

        try:

            if f1!=f2:
                return False
            if l11!=l21:
                return False
            if l12!=l22:
                return False
        except TypeError:
            return False



    except TypeError:
        return False
    return True



defaults = {}


###1.ready, cards_intersect
cards_intersect_def = {'modulename': 'ex4','fname': 'cards_intersect',}
cards_intersect= {'cards_intersect': {'comparemethod':unorderedlists ,'args':  [['spider', 'pencil', 'stop'],
                                        ['apple','spider', 'pencil']], 'ans': [['pencil','spider']],},
                  'cards_intersect_none': {'comparemethod':unorderedlists ,'args':  [['pen','sun', 'stop'],
                                        ['apple', 'pencil', 'spider']], 'ans': [[]],},
        }

###2.ready.remove_card
remove_card_def = {'modulename': 'ex4','fname': 'remove_card',}
remove_card= {
              'remove_card_good': {'args':  [[['dolphin', 'bomb',  'spider'],
                                    ['scissors', 'spider', 'exclamation point']],['dolphin', 'bomb',  'spider']], 'ans': [True],},
        }


###3.ready.add_card
add_card_def = {'modulename': 'ex4','fname': 'add_card',}
add_card = {
            'add_card_good': {'args': [[['dolphin', 'bomb', 'spider'],['scissors', 'spider', 'exclamation point']],['scarecrow', 'spider', 'stop']],
                                   'ans': [True], },
            }

###4.ready,is_valid
is_valid_def = {'modulename': 'ex4','fname': 'is_valid',}
is_valid= {'is_valid_good': {'args':  [[['dolphin', 'bomb',  'spider'],
                                    ['scissors', 'spider', 'exclamation point']]], 'ans': [True],},
            'is_valid_bad': {'args':  [[['dolphin', 'bomb'],
                                    ['scissors', 'spider', 'exclamation point']]], 'ans': [False],},
        }

###5.ready.draw_random_cards_def
draw_random_cards_def = {'modulename': 'ex4','fname': 'draw_random_cards',}
draw_random_cards= {'draw_random_cards': {'comparemethod':unorderedlists ,'args':  [[['dolphin', 'bomb',  'spider'],
['scissors', 'spider', 'exclamation point']]],'ans':[[
['dolphin', 'bomb',  'spider'],['scissors', 'spider', 'exclamation point']]],},
        }

##6.ready.print_symbols_counts
print_symbols_counts_def = {'modulename': 'ex4','fname': 'print_symbols_counts',}
print_symbols_counts = {'print_symbols_counts': {'comparemethod':unorderedlists2 ,'runner':testrunners.print_runner,'args':  [[['dolphin', 'bomb',  'spider'],
            ['scissors', 'spider', 'exclamation point']]], 'ans': ['spider 2\ndolphin 1\nexclamation point 1\nbomb 1\nscissors 1\n'],},
    }


##7.ready.play_dobble
play_dobble_def = {'modulename': 'ex4','fname': 'play_dobble',}
play_dobble = {'play_dobble': {'runner':testrunners.print_runner,
                               'comparemethod': print_in_range,
                               'options': {'input': 'P\nspider', },
                               'args':  [[['dolphin', 'bomb',  'spider'],
                                      ['scissors', 'spider', 'exclamation']]],
                               'ans': [ "Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                        "Identify joint symbol:\n"
                                        "scissors,spider,exclamation\n"
                                        "dolphin,bomb,spider\n"
                                        "Very nice! Found the correct card in 0.0 sec.\n"
                                        "Finished Game. Correct: 1 Wrong: 0 Average time: 0.0 sec.\n","Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                        "Identify joint symbol:\n"
                                        "scissors, spider, exclamation\n"
                                        "dolphin, bomb, spider\n"
                                        "Very nice! Found the correct card in 0.0 sec.\n"
                                        "Finished Game. Correct: 1 Wrong: 0 Average time: 0.0 sec.\n"],},
                'play_dobble2': {'runner':testrunners.print_runner,
                                               'comparemethod': print_in_range,
                                               'options': {'input': 'P\nbomb', },
                                               'args':  [[['dolphin', 'bomb',  'spider'],
                                                      ['scissors', 'spider', 'exclamation']]],
                                               'ans': [ "Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                                        "Identify joint symbol:\n"
                                                        "dolphin,bomb,spider\n"
                                                        "scissors,spider,exclamation\n"
                                                        "Wrong!\n"
                                                        "Finished Game. Correct: 0 Wrong: 1 Average time: 0.0 sec.\n", "Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                                        "Identify joint symbol:\n"
                                                        "dolphin, bomb, spider\n"
                                                        "scissors, spider, exclamation\n"
                                                        "Wrong!\n"
                                                        "Finished Game. Correct: 0 Wrong: 1 Average time: 0.0 sec.\n"],},

                'add': {'runner':testrunners.print_runner,
                                               'options': {'input': 'A\ndolphin,bomb\n', },
                                               'args':  [[['dolphin', 'bomb',  'spider'],
                                                      ['scissors', 'spider', 'exclamation']]],
                                               'ans': [ "Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                                        "Error! Card is of wrong length\n"],},
                'remove': {'runner':testrunners.print_runner,
                                                               'options': {'input': 'R\ndolphin,bomb\n', },
                                                               'args':  [[['dolphin', 'bomb',  'spider'],
                                                                      ['scissors', 'spider', 'exclamation']]],
                                                               'ans': [ "Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                                                        "Error! card is not in the deck!\n","Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                                                        "Error!  card is not in the deck!\n"],
                                                               },
                'remove2': {'runner':testrunners.print_runner,
                                                               'options': {'input': 'R\ndolphin,bomb,spider\n', },
                                                               'args':  [[['dolphin', 'bomb',  'spider'],
                                                                      ['scissors', 'spider', 'exclamation']]],
                                                               'ans': [ "Select operation: (P)lay, (A)dd card, (R)emove card, or (C)ount\n"
                                                                        ],},


               }




tsets = {
         'cards_intersect': TestSet(cards_intersect_def,cards_intersect),
         'remove_card': TestSet(remove_card_def,remove_card),
         'add_card': TestSet(add_card_def, add_card),
         'is_valid': TestSet(is_valid_def, is_valid),
         'draw_random_cards': TestSet(draw_random_cards_def, draw_random_cards),
         'print_symbols_counts': TestSet(print_symbols_counts_def, print_symbols_counts),
         'play_dobble': TestSet(play_dobble_def, play_dobble),

}
