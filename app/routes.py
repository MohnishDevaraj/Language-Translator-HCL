from flask import Flask, request, render_template
from app import app

import time
from selenium import webdriver
import selenium


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        input1 = request.form["text-to-translate"].lower()
        input1.split()
        selected_language = request.form["select-language"]
        browser = webdriver.Chrome(
            r"C:\Users\devar\OneDrive\Desktop\Language Transilator\webdriver\chromedriver_win32\chromedriver.exe")

        browser.get("https://translate.google.co.in/?sl=auto&tl=" +
                    selected_language+"&text="+input1+"&op=translate")

        time.sleep(1)

        #output1 = browser.find_element_by_class_name("J0lOec").text
        # VIiyi
        # output1 = browser.find_element_by_xpath(
        #    "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span").text
        output1 = browser.find_element_by_xpath(
            "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]").text
        print(output1)

        return render_template('text.html', translation_result=output1)

    return render_template("text.html")


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


@app.route("/Feedback")
def profile():
    return render_template("Feedback.html")


@app.route("/text")
def text():
    return render_template("Text.html")
