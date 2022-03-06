from lib2to3.pgen2 import driver
from flask import Flask, request, render_template
# import googletrans
# from googletrans import Translator

import time
from selenium import webdriver
import selenium

app = Flask(__name__)
# translator = Translator()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            input1 = request.form["text-to-translate"].lower()
            print(input1)
            # selected_language = request.form["select-language"]webdriver
            # to_lang = translator.detect(text_to_translate)
            # from_lang = translator.detect(selected_language)
            # translated_text = translator.translate(
            #     text_to_translate, src=from_lang, dest=to_lang)
            # text = translated_text.text
            # pronunciation_data = translated_text.pronunciation
            # if (str(pronunciation_data) == "None"):
            # pronunciation_data = "{Sorry, data not available}"
            # confidence = round((translator.translate(
            # text_to_translate, dest=selected_language).extra_data["confidence"])*100, 2)
            lang_code = 'hi'

            # input1 = " Coronaviruses are a group of related viruses that cause diseases in mammals and birds. In humans, coronaviruses cause respiratory tract infections that can be mild, such as some cases of the common cold (among other possible causes, predominantly rhinoviruses), and others that can be lethal, such as SARS, MERS, and COVID-19. Symptoms in other species vary: in chickens, they cause an upper respiratory tract disease, while in cows and pigs they cause diarrhea. There are yet to be vaccines or antiviral drugs to prevent or treat human coronavirus infections."

            # launch browser with selenium:=>
            browser = webdriver.Chrome()

            # copy google Translator link here:=>
            browser.get("https://translate.google.co.in/?sl=auto&tl=" +
                        lang_code+"&text="+input1+"&op=translate")

            # just wait for some time for translating input text:=>
            time.sleep(6)

            # Given below x path contains the translated output that we are storing in output variable:=>
            output1 = driver.find_element_by_xpath(
                '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]').text
            print(output1)

            # Display the output:=>
            # , translation_result=output1)
            return render_template('text.html', translation_result=output1)
        except:
            # pronunciation_data = "-"
            text = "{ERROR: We are not able to handle your request right now}"
            # confidence = "-"
            return render_template('text.html', translation_result=text)
    return render_template("text.html")


@ app.route("/voice")
def voice():
    return render_template("Voice.html")


@ app.route("/country", methods=['POST', 'GET'])
def country():
    if request.method == 'POST':
        try:
            country = request.form["select-language"].lower
            print(country)
            return render_template('Country-Language.html', Country=country)
        except:
            error = "Error"
            return render_template('Country-Language.html', Country=error)
    return render_template('Country-Language.html')
    # return render_template("Country-Language.html")


@ app.route("/profile")
def profile():
    return render_template("Profile.html")


@ app.route("/text")
def text():
    return render_template("Text.html")


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
