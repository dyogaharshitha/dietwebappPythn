import pandas as pd
import dishselect

dishdf= dishselect.dishdf;

def srchkeywrd(kywrd):
  dshnme= dishdf["dish_name"];
  srch= list();
  srchnum= list();
  srchdic= dict();
  if type(kywrd) == 'int':
    dish= dishdf.loc[kywrd];
    srchdic[kywrd]= dish;
  else:
    for indx,dishnm in dshnme.items():
      if kywrd in dishnm:
        srch.append(dishnm);
        srchnum.append(indx);
  srchdict= dict(zip(srchnum, srch));


  return srchdict;





def calnutri(dishlst):
  #mealdf= pd.DataFrame();
  #for el in dishlst:
   # df= dishdf.loc[el];
  mealdf= dishdf.loc[dishlst];
  print(mealdf);
  calories= mealdf["Calories"].sum(); carb= mealdf["Carbohydrate_g"].sum(); prot= mealdf["Protein_g"].sum(); fat= mealdf['Fat_g'].sum();
  nutrilst= [calories,carb,prot,fat];
  return nutrilst;


def calcnutri(dishlst):
    mealdf= pd.DataFrame();
    for indx in dishlst:
      el= dishdf.loc[indx];
      mealdf = pd.concat([mealdf, pd.DataFrame(el)], axis=1, ignore_index=False);
    print(mealdf);
    calories = mealdf.loc["Calories"].sum();
    carb = mealdf.loc["Carbohydrate_g"].sum();
    prot = mealdf.loc["Protein_g"].sum();
    fat = mealdf.loc['Fat_g'].sum();
    nutridict = {"cal":calories,"carb": carb, "prot": prot, "fat": fat};
    return nutridict;
