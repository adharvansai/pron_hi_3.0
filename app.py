from flask import Flask, render_template, request, url_for, flash, redirect
from matplotlib.pyplot import legend
from highlightHelper.configDict import IPA_DICT,COLORS
from highlightHelper.highlighter import highlight_text



app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8e8a8244e245e9627363ec1d181d6c3e2a02b30773494ac'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/highlighted', methods=['GET', 'POST'])
def highlighter():
    if(request.method == "POST"):

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

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
