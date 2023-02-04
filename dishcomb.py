import pandas as pd
import xldata
import dishselect
import itertools
import setFoodlimit as fdlmt

tiffdf= dishselect.gettifdf();
currydf= dishselect.getcurrydf();
snackdf= dishselect.getsnackdf();

def gettiffcomb():
    # print(tiffdf);
    cerlitms = tiffdf.index.tolist();
    cerlcomb = list(itertools.combinations(cerlitms, 3));
    # print(cerlcomb);
    copycerlcomb = cerlcomb.copy();
    for tup in cerlcomb:
        if (tup[0] == 1001 and tup[1] == 1002):
            # print(tup);
            each_cerlcombdf = tiffdf.loc(axis=0)[[tup[0], tup[1], tup[2]]];
            daycerlqty = each_cerlcombdf['dish_qty'].sum();
            daycerlcal = each_cerlcombdf['Calories'].sum();
            daycerlcarbs = each_cerlcombdf['Carbohydrate_g'].sum();
            if daycerlcal > 900:
                indx = each_cerlcombdf['Calories'].idxmax();
                #print(indx);  # print(each_cerlcombdf); print( each_cerlcombdf.loc[1009]['Calories']);
                each_cerlcombdf.loc[indx]['Calories'] = (each_cerlcombdf.loc[indx]['min_qty_serving'] *
                                                         each_cerlcombdf.loc[indx]['Calories']) / \
                                                        each_cerlcombdf.loc[indx]['dish_qty'];
                daycerlcal = each_cerlcombdf['Calories'].sum();
            if daycerlcal > 900:
                indx = copycerlcomb.index(tup);
                print(indx);
                print(copycerlcomb[indx]);
                del copycerlcomb[indx];
                continue;
            # reqcomb.append(tup);
        else:
            # print(tup);
            indx = copycerlcomb.index(tup);  # print(indx); #print(copycerlcomb[indx]);
            # del copycerlcomb[indx];
            copycerlcomb.pop(indx);
            continue;
    # print(tup);

    if copycerlcomb:
        cerlcomb = copycerlcomb;
    #print(copycerlcomb);
    return cerlcomb;

def getcurrycomb():
    curryitms = currydf.index.tolist();
    currycomb = list(itertools.combinations(curryitms, 2));
    # print(currycomb);
    # print(currydf.loc(axis=0)[1019,1020]);
    copycurrycomb = currycomb.copy();
    for tup in currycomb:
        t0 = tup[0];
        t1 = tup[1];
        each_currycombdf = currydf.loc(axis=0)[[t0, t1]];
        crytyp0 = each_currycombdf.loc[tup[0]]['type'];
        crytyp1 = each_currycombdf.loc[tup[1]]['type'];
        if (crytyp0 != crytyp1):
            if (crytyp0 == 'dal' and crytyp1 == 'dalcurry' or (crytyp0 == 'dalcurry' and crytyp1 == 'dal') or (
                    crytyp0 == 'dal' and crytyp1 == 'gravy') or (crytyp0 == 'gravy' and crytyp1 == 'dal')):
                indx = copycurrycomb.index(tup);
                copycurrycomb.pop(indx);
                continue;
            # print(tup);

            daycurryqty = each_currycombdf['dish_qty'].sum();
            daycurrycal = each_currycombdf['Calories'].sum();
            daycurrycarbs = each_currycombdf['Carbohydrate_g'].sum();
            if daycurrycal < 300:
                indx = each_currycombdf['Calories'].idxmax();
                # print(indx);  # print(each_cerlcombdf); print( each_cerlcombdf.loc[1009]['Calories']);
                each_currycombdf.loc[indx]['Calories'] = (each_currycombdf.loc[indx]['max_qty_serving'] *
                                                          each_currycombdf.loc[indx]['Calories']) / \
                                                         each_currycombdf.loc[indx]['dish_qty'];
                daycurrycal = each_currycombdf['Calories'].sum();
                if daycurrycal > 900:
                    indx = copycurrycomb.index(tup);  # print(indx);
                    # print(copycurrycomb[indx]);
                    del copycurrycomb[indx];
                    continue;
            # reqcomb.append(tup);
        else:
            # print(tup);
            indx = copycurrycomb.index(tup);  # print(indx); #print(copycerlcomb[indx]);
            # del copycerlcomb[indx];
            copycurrycomb.pop(indx);
            continue;
        # print(tup);

    if copycurrycomb:
        cerlcomb = copycurrycomb;
    #print(copycurrycomb);
    return currycomb;

def getsnackcomb():
    snackitms = snackdf.index.tolist();
    snackcomb= snackitms;

    return snackcomb;






