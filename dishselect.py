import pandas as pd
import xldata
#import setFoodlimit as fdlmt

dishdf = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\dishnutri.xlsx");
dishmethusg = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\dishmethod.xlsx");
fooditemfrq = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\foodnutri.xlsx");
dishtype = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\currytype.xlsx");
nutridf = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\nutrireq.xlsx");
foodclassdf = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\foodclass.xlsx");

frqmeth = dishmethusg[dishmethusg['usage_frq'] > dishmethusg['max_times_per_week']].index.tolist();
frqingri = fooditemfrq[fooditemfrq['usage_week_frq'] > fooditemfrq['max_week_frq']].index.tolist();
frqcurrytype = dishtype[dishtype['usg_frq_month'] > dishtype['max_frq_month']].index.tolist();

tiffdf= dishdf.loc[(dishdf['class'] == 'cereal') & (dishdf['type'] == 'tiffin') & (dishdf['usage_frq_week'] < 3)];

def gettifdf():
    tiffdf = dishdf.loc[(dishdf['class'] == 'cereal') & (dishdf['type'] == 'tiffin') & (dishdf['usage_frq_week'] < 3)];

    if frqmeth:
        drplst = tiffdf[tiffdf['method'] in frqmeth].index.tolist();
        drplst = set(drplst) & set(tiffdf.index.tolist());
        tiffdf = tiffdf.drop(drplst, inplace=True);
    if (tiffdf.shape[0] !=0):
        for indx, el in tiffdf['ingridient_id'].iteritems():
            el = str(el);
            el = el.split("_");
            el = [eval(i) for i in el];
            if set(el) & set(frqingri):
                tiffdf.drop(indx, inplace=True);

    if tiffdf.shape[0]> 10:
        tiffdf = tiffdf.sort_values(by=['Calories', 'Fat_g'], ascending=[True, True]);
        tiffdf= tiffdf.head(7);


    return tiffdf;

def getcurrydf():
    currydf = dishdf.loc[(dishdf['class'].isin(['curry', 'chutney'])) & (dishdf['usage_frq_week'] < 3)];

    if frqmeth:
        drplst = currydf[currydf['method'] in frqmeth].index.tolist();
        drplst = set(drplst) & set(currydf.index.tolist());
        currydf = currydf.drop(drplst, inplace=True);
    if frqcurrytype:
        drplst = currydf[currydf['type'] in frqcurrytype].index.tolist();
        drplst = set(drplst) & set(currydf.index.tolist());
        currydf = currydf.drop(drplst, inplace=True);
    if (currydf.shape[0] !=0):
        for indx, el in currydf['ingridient_id'].iteritems():
            el = str(el);
            el = el.split("_");
            el = [eval(i) for i in el];
            if set(el) & set(frqingri):
                currydf.drop(indx, inplace=True);

    if currydf.shape[0]> 20:
        currydf = currydf.sort_values(by=['Protein_g', 'Fiber_g'], ascending=[False, False]);
        currydf= currydf.head(15);

    return currydf;

def getsnackdf():
    snackdf = dishdf.loc[((dishdf['class'] == 'fruit') | (dishdf['class'] == 'nuts')) & (dishdf['usage_frq_week'] < 3)];

    return snackdf;





