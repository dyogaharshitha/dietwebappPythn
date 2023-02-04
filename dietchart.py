import pandas as pd
import itertools
import xldata
import dishselect
import dishcomb

tiffdf= dishcomb.tiffdf;
currydf= dishcomb.currydf;
snackdf= dishcomb.snackdf;
cerlcomb= dishcomb.gettiffcomb();
currycomb= dishcomb.getcurrycomb();
snackcomb= dishcomb.getsnackcomb();

print("start"); print(cerlcomb);
def getfiltermealdf():

    mealdf = pd.DataFrame(columns=["indx", "dishlst", "dishqtylst", "calories", "carb", "prot", "fat"]);
    mealdf.set_index("indx", inplace=True);

    mealcomb = list(itertools.product(cerlcomb, currycomb));
    print(len(mealcomb));
    i = 0;
    for tup in mealcomb:
        t1 = tup[0][0];
        t2 = tup[0][1];
        c1 = tup[1][0];
        c2 = tup[1][1];

        ml = dict(
            {"indx": i, "dishlst": "1_2", "dishqtylst": "10_100", "calories": 150, "carb": 70, "prot": 20, "fat": 15});

        # ml=pd.Series(["1,2", "10,100", 150, 70, 20,5]);
        # print(pd.concat([mealdf,ml] ));
        ml['dishlst'] = str(t1) + "_" + str(t2) + "_" + str(c1) + "_" + str(c2);
        ml['dishqtylst'] = str(tiffdf.loc[t1]['dish_qty']) + "_" + str(tiffdf.loc[t2]['dish_qty']) + "_" + str(
            currydf.loc[c1]['dish_qty']) + "_" + str(currydf.loc[c2]['dish_qty']);
        ml['calories'] = (tiffdf.loc[t1]['Calories'] + tiffdf.loc[t2]['Calories'] + currydf.loc[c1]['Calories'] +
                          currydf.loc[c2]['Calories']);
        ml['carb'] = (tiffdf.loc[t1]['Carbohydrate_g'] + tiffdf.loc[t2]['Carbohydrate_g'] + currydf.loc[c1][
            'Carbohydrate_g'] + currydf.loc[c2]['Carbohydrate_g']);
        ml['prot'] = (tiffdf.loc[t1]['Protein_g'] + tiffdf.loc[t2]['Protein_g'] + currydf.loc[c1]['Protein_g'] +
                      currydf.loc[c2]['Protein_g']);
        ml['fat'] = (tiffdf.loc[t1]['Fat_g'] + tiffdf.loc[t2]['Fat_g'] + currydf.loc[c1]['Fat_g'] + currydf.loc[c2][
            'Fat_g']);
        # ml['carb']= ml['carb']+20; ml['prot']= ml['prot']+3; ml['fat']= ml['fat']+2;
        mealdf = pd.concat([mealdf, pd.DataFrame(ml, index=[i])], axis=0, ignore_index=True);
        i = i + 1;

    mealdietdf = mealdf.loc[(mealdf['calories'].between(500,1500))];  # | (mealdf['calories']< 500) ];
    print(len(mealdietdf));
    indxlst = mealdietdf.index.tolist();
    delindx= list();

    for i in indxlst:
        # print(deldf.loc[i]);
        calgr = mealdietdf.loc[i]['carb'] + mealdietdf.loc[i]['prot'] + mealdietdf.loc[i]['fat'];
        if ((mealdietdf.loc[i]['carb'] / calgr) > 0.8) or ((mealdietdf.loc[i]['fat'] / calgr) > 0.25):
            delindx.append(i);
    reqmealdietdf = mealdietdf.drop(delindx);
    print(len(reqmealdietdf));
    return mealdietdf;


    """
    mealcomb = list(itertools.product(cerlcomb, currycomb, snackcomb));
    print(len(mealcomb));
    i = 0;
    for tup in mealcomb:
        t1 = tup[0][0]; t2 = tup[0][1];
        c1 = tup[1][0]; c2 = tup[1][1];
        sn = tup[2];

        ml = dict(
            {"indx": i, "dishlst": "1_2", "dishqtylst": "10_100", "calories": 150, "carb": 70, "prot": 20, "fat": 15});

        # ml=pd.Series(["1,2", "10,100", 150, 70, 20,5]);
        # print(pd.concat([mealdf,ml] ));
        ml['dishlst'] = str(t1) + "_" + str(t2) + "_" + str(c1) + "_" + str(c2) + "_" + str(sn);
        ml['dishqtylst'] = str(tiffdf.loc[t1]['dish_qty']) + "_" + str(tiffdf.loc[t2]['dish_qty']) + "_" + str(
            currydf.loc[c1]['dish_qty']) + "_" + str(currydf.loc[c2]['dish_qty']) + "_" + str(
            snackdf.loc[sn]['dish_qty']);
        ml['calories'] = (tiffdf.loc[t1]['Calories'] + tiffdf.loc[t2]['Calories'] + currydf.loc[c1]['Calories'] +
                          currydf.loc[c2]['Calories'] + snackdf.loc[sn]['Calories']);
        ml['carb'] = (tiffdf.loc[t1]['Carbohydrate_g'] + tiffdf.loc[t2]['Carbohydrate_g'] + currydf.loc[c1][
            'Carbohydrate_g'] + currydf.loc[c2]['Carbohydrate_g'] + snackdf.loc[sn]['Carbohydrate_g']);
        ml['prot'] = (tiffdf.loc[t1]['Protein_g'] + tiffdf.loc[t2]['Protein_g'] + currydf.loc[c1]['Protein_g'] +
                      currydf.loc[c2]['Protein_g'] + snackdf.loc[sn]['Protein_g']);
        ml['fat'] = (tiffdf.loc[t1]['Fat_g'] + tiffdf.loc[t2]['Fat_g'] + currydf.loc[c1]['Fat_g'] + currydf.loc[c2][
            'Fat_g'] + snackdf.loc[sn]['Fat_g']);
        # ml['carb']= ml['carb']+20; ml['prot']= ml['prot']+3; ml['fat']= ml['fat']+2;
        mealdf = pd.concat([mealdf, pd.DataFrame(ml, index=[i])], axis=0, ignore_index=True);
        i = i + 1;
    print(len(mealdf));
    mealdietdf = mealdf.loc[(mealdf['calories'].between(900, 1300))];  # | (mealdf['calories']< 500) ];
    #print(mealdietdf);
    indxlst = mealdietdf.index.tolist();
    for i in indxlst:
        # print(deldf.loc[i]);
        calgr = mealdietdf.loc[i]['carb'] + mealdietdf.loc[i]['prot'] + mealdietdf.loc[i]['fat'];
        if ((mealdietdf.loc[i]['carb'] / calgr) > 0.8) or ((mealdietdf.loc[i]['prot'] / calgr) > 0.25):
            mealdietdf.drop(mealdietdf.loc[i]);

    return mealdietdf;
"""



