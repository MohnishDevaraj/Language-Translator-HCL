from flask import Flask, request, render_template
from app import app
# import googletrans
# from googletrans import Translator

import time
from selenium import webdriver
import selenium


# translator = Translator()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        input1 = request.form["text-to-translate"].lower()
        input1.split()
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
        browser = webdriver.Chrome(
            r"C:\Users\devar\Downloads\chromedriver_win32\chromedriver.exe")

        # copy google Translator link here:=>
        browser.get("https://translate.google.co.in/?sl=auto&tl=" +
                    lang_code+"&text="+input1+"&op=translate")

        # just wait for some time for translating input text:=>
        time.sleep(6)

        # Given below x path contains the translated output that we are storing in output variable:=>
        output1 = browser.find_element_by_class_name("VIiyi").text
        print(output1)

        # Display the output:=>
        # , translation_result=output1)
        return render_template('text.html', translation_result=output1)

        # pronunciation_data = "-"
        #text = "{ERROR: We are not able to handle your request right now}"
        # confidence = "-"
        # return render_template('text.html', translation_result=text)
    return render_template("text.html")


# def country():


# @app.route("/country")
# def country():
#    if request.method == 'POST':
#        try:
#     #         count = request.form["select-translate"].lower()
#     #         print(count)
#     #         return render_template('Country-Language.html', Country_Lang=count)
#     #     except:
#     #         error = "Error"
#     #         return render_template('Country-Language.html', Country_Lang=error)
#     # return render_template('Country-Language.html')

#     return render_template("Country-Language.html")


@app.route("/document")
def document():
    return render_template("Document.html")


@app.route("/country", methods=['POST', 'GET'])
def country():
    if request.method == 'POST':
        try:
            count = request.form.get["country-to-translate"].lower()
            print(count)
            return render_template('Country-Language.html', text_to_translate=count)
        except:
            error = "Error not able to get country"
            return render_template('Country-Language.html', text_to_translate=error)
    return render_template('Country-Language.html')


@app.route("/profile")
def profile():
    return render_template("Profile.html")


@app.route("/text")
def text():
    return render_template("Text.html")