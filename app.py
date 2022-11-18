import os

from flask import Flask, render_template, request

from highlightHelper.configDict import IPA_DICT, COLORS
from highlightHelper.highlighter import highlight_text
from omapHelper.omapper import getmap
from omapHelper.updateRules import updateRulesFile, getRules
from stressHelper.cmu_stress_syll import cmu_stress
from syllableHelper.syllabify import get_syllables

try:
  import eng_to_ipa
except ImportError:
  os.system('python -m pip install eng_to_ipa')

import eng_to_ipa as phen
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8e8a8244e245e9627363ec1d181d6c3e2a02b30773494ac'

pyanyDir = ""#"/home/adhar1sai/mysite/"

doc = {'user' : 'analytics/User_Logs.csv',
        'feedback' : 'analytics/Feedback_Logs.csv',
        'report' : 'analytics/Report_Logs.csv'}

def logAnalytics(analytics, information):
    if information:
        filename = pyanyDir + doc[analytics]
        data = []
        data.append(str(datetime.datetime.now()))
        data.append(information.strip())
        data = ",".join(data) + "\n"
        f = open(filename, "a+")
        f.writelines(data)
        f.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/highlighted', methods=['GET', 'POST'])
def highlighter():
    if(request.method == "POST"):
        # Analytics
        user_type = request.form.get('user')
        logAnalytics('user',user_type)


        # List of checkboxes selected
        ipa_all_checkboxes = request.form.getlist('ipa_ckb')


        selected_ipa = []
        for i in ipa_all_checkboxes:
            selected_ipa.append(IPA_DICT[int(i)])

        # User Text input, divided into individual words
        text_input = request.form.get('user_input')
        input_in_words = text_input.split(" ")


        ipa_to_word_indices_dict = highlight_text(input_in_words,selected_ipa)

        # Template to highlight each word
        mark_text = "<mark class='ph1' style='background: COLOR!important'>WORDTEXT</mark>"
        legend_text = ""
        for i,k in enumerate(ipa_to_word_indices_dict.keys()):
            curr_mark = mark_text.replace("COLOR",COLORS[i])
            for ind in ipa_to_word_indices_dict[k]:
                input_in_words[ind] = curr_mark.replace("WORDTEXT", input_in_words[ind])
            legend_text += curr_mark.replace("WORDTEXT", "\t/ "+k+" /\t") + "&emsp;"

        final_text = " ".join(input_in_words)
        final_text +=  "<br/><br/><p class='legend'>"+ legend_text + "<p>"

        return render_template('highlighted.html', text = final_text, original_text = text_input )#request.args['user_input'])

@app.route('/s')
@app.route('/syllabifier')
@app.route('/syllabified', methods=['GET', 'POST'])
def syllabified():
    html_syllables = ""
    if(request.method == "POST"):

        word = request.form.get('user_input')
        word = word.split(" ")[0]
        divided_syllables = get_syllables(word)
        html_syllables = divided_syllables.replace("|"," <span>&#8226;</span> ")

    return render_template('syllabified.html', syllables = html_syllables)


@app.route('/stress')
@app.route('/ss')
@app.route('/stressed', methods=['GET', 'POST'])
def stressed():
    html_syllables  = ""
    ipa_conv = ""
    if(request.method == "POST"):

        word = request.form.get('user_input')
        word = word.split(" ")[0]
        divided_syllables = get_syllables(word).split("|")
        word = word.upper()
        if word in cmu_stress.keys():
            stresses = cmu_stress.get(word)
        else:
            return render_template('stressed.html', syllables = "***")
        st = list(set(stresses))
        html_syllables = []
        for i in st:
            conv = []
            for w in divided_syllables:
                conv.append(w)
            if i < len(divided_syllables):
                conv[i] = "<b>" + conv[i] + "</b>"
            else:
                return render_template('stressed.html', syllables = html_syllables)
            conv = " <span>&#8226;</span> ".join(conv)
            html_syllables.append(conv)
        html_syllables = "<br>".join(html_syllables)
        ipa_conv = phen.convert(word).strip()

    return render_template('stressed.html', syllables = html_syllables, ipa = ipa_conv)

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        info = []
        info.append(request.form.get("source"))
        word = request.form.get("name").replace(",", ";")
        info.append(word)
        desc = request.form.get("message").replace(",", ";").replace("\n", " ")
        info.append(desc)
        info = ",".join(info)
        logAnalytics('report',info)
        return ('',204)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        info = []
        info.append(request.form.get('source'))
        info.append(request.form.get('name').replace(",", " "))
        info.append(request.form.get('email'))
        info.append(request.form.get('message').replace(",", ";").replace("\n", " "))
        logAnalytics('feedback',",".join(info))
        return ('',204)

@app.route('/rules')
@app.route('/omaprules', methods=['GET', 'POST'])
def omapRules():
    if request.method == 'POST':
        updatedRules = request.form.get('rules_input')
        updateRulesFile(updatedRules)
    curr_rules = getRules()
    return render_template('omap_rules.html', rules_text = curr_rules)

@app.route('/o')
@app.route('/omap', methods=['GET', 'POST'])
def omap():
    mapp = ""
    if request.method == 'POST':
        word = request.form.get('word_input')
        mapping = getmap(word)
        mapp = "<br>".join(mapping)
    return render_template('omapping.html', map = mapp)
    



if __name__=='__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0",port=5000)