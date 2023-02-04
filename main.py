import json
import dietchart
import updatedf

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import misc

app= Flask(__name__);

@app.route("/", methods=['GET', 'POST'])
def showhomepg():
    print("show home page func");
    return render_template('homepg.html');

@app.route("/logmeal", methods=['GET', 'POST'])
def showlogmealpage():
    print("show logmeal func");
    return render_template('logmeal.html');

@app.route("/logmealresponse", methods=['GET', 'POST'])
def logmealfun():
    print("log meal response fun");
    msg= ' ';
    cereal1= request.form['cereal1'];
    cereal1qty= request.form['cereal1qty'];
    msg= cereal1;

    return render_template('formresponse.html',msg= msg)

@app.route("/calnutri", methods=['GET', 'POST'])
def calnutri():
    print("cal nutri func");
    if request.method== 'POST':
        print("cal nutri post");
        jdat = json.loads(request.data);
        if jdat['srch']=='yes':
            dshlst= jdat['dat'];
            srchlst= updatedf.srchkeywrd(dshlst);
            print(updatedf.srchkeywrd(dshlst));
            snd= json.dumps(srchlst);
            return snd;
        if jdat['srch']== 'no':
            print("log data"); print(jdat['dat']);
            dshlst= jdat['dat'];
            dsh= list();
            for el in dshlst:
                dsh.append(int(el));

            nutrijsn= updatedf.calcnutri(dsh);
            snd = json.dumps(nutrijsn); print(snd);
            return snd;
    return render_template('calnutri.html');

@app.route("/dietforday", methods=['GET', 'POST'])
def dietforday():
    print("get diet for day");
    if request.method== 'POST':
        diet= misc.getdiet();
        cereal1= diet['cereal1'];
        cereal1qty= diet['cereal1qty'];
        return render_template('dietforday.html', cereal1=cereal1, cereal1qty=cereal1qty, diet=diet);
    return render_template('dietforday.html');

@app.route("/ajx", methods=['GET', 'POST'])
def ajx():
    print("ajx fun");
    if request.method== 'POST':
        #dat= request.json;
        #print(dat);
        dat= json.loads(request.data);
        print(dat['a']);
        print("ajx post")
        snd= json.loads('{"x": "y"}')
        return snd;
    return render_template('ajx.html');

app.run(host="0.0.0.0")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
