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


@app.route("/country", methods=['POST', 'GET'])
def country():
    if request.method == 'POST':
        count = request.form["country-to-translate"]
        if(count == "India" or count == "india"):
            lang = "Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Urdu, Kannada, Odia, Malayalam, Punjabi, Assamese, Maithili"
        elif(count == "Afghanistan" or count == "afghanistan"):
            lang = "Afghan Persian or Dari (official), Pashto (official), Uzbek, English, Turkmen, Urdu, Pashayi, Nuristani, Arabic, Balochi"
        elif(count == "Albania" or count == "albania"):
            lang = "Albanian(official), Greek"
        elif(count == "Algeria" or count == "algeria"):
            lang = "Arabic (official), French, Berber or Tamazight (official), Shawiya Berber, Mzab Berber, Tuareg Berber"
        elif(count == "Andorra" or count == "andorra"):
            lang = "Catalan (official), French, Castilian, Portuguese"
        elif(count == "Angola" or count == "angola"):
            lang = "Portuguese(official), Umbundu, Kikongo, Kimbundu, Chokwe, Nhaneca, Nganguela, Fiote, Kwanhama, Muhumbi, Luvale"
        elif(count == "Argentina" or count == "argentina"):
            lang = "Spanish (official), Italian, English, German, French, indigenous"
        elif(count == "Belgium" or count == "belgium"):
            lang = "Dutch (official), French (official), German (official)"
        elif(count == "Brazil" or count == "brazil"):
            lang = "Portuguese"
        elif(count == "Cambodia" or count == "cambodia"):
            lang = "Khmer (official)"
        elif(count == "Canada" or count == "canada"):
            lang = "English (official), French (official), Punjabi, Italian, Spanish, German, Cantonese, Tagalog, Arabic"
        elif(count == "Chile" or count == "chile"):
            lang = "Spanish(official), English, indigenous, Aymara, Quechua"
        elif(count == "China" or count == "china"):
            lang = "Standard Chinese or Mandarin (official), Putonghua, Yue, Wu, Minbei, Minnan, Xiang, Gan, Hakka dialects"
        elif(count == "Colombia" or count == "colombia"):
            lang = "Spanish (official)"
        elif(count == "Cuba" or count == "cuba"):
            lang = "Spanish (official)"
        elif(count == "Dominica" or count == "dominica"):
            lang = "English (official), French patois"
        elif(count == "East Timor" or count == "east timor"):
            lang = "Spanish (official)"
        elif(count == "Finland" or count == "finland"):
            lang = "Finnish (official), Swedish (official), Russian"
        elif(count == "Germany" or count == "germany"):
            lang = "German (official)"
        elif(count == "Indonesia" or count == "indonesia"):
            lang = "Bahasa Indonesian, English, Dutch"
        elif(count == "Iran" or count == "iran"):
            lang = "Persian Farsi (official), Azeri and other Turkic dialects, Kurdish, Gilaki and Mazandarani, Luri, Balochi, Arabic"
        elif(count == "Israel" or count == "israel"):
            lang = "Hebrew (official), Arabic, English"
        elif(count == "Italy" or count == "Italy"):
            lang = "Italian (official), German, French, Slovene"
        elif(count == "Japan" or count == "japan"):
            lang = "Japanese"
        elif(count == "New Zealand" or count == "new zealand"):
            lang = "English (de facto official), Maori, Samoan, Northern Chinese, Hindi, French, Yue, New Zealand Sign Language"
        elif(count == "Pakistan" or count == "Ppakistan"):
            lang = "Punjabi, Sindhi, Saraiki (a Punjabi variant), Pashto (alternate name, Pashtu), Urdu (official), Balochi, Hindko, Brahui, English, Burushaski"
        elif(count == "Russia" or count == "russia"):
            lang = "Russian (official), Tatar, Chechen"
        elif(count == "Singapore" or count == "singapore"):
            lang = "English (official), Mandarin (official), other Chinese dialects (includes Hokkien, Cantonese, Teochew, Hakka), Malay (official), Tamil"
        else:
            lang = "Error"
        return render_template('Country-Language.html', text_to_translate=lang)
    return render_template('Country-Language.html')


@app.route("/Feedback")
def profile():
    return render_template("Feedback.html")


@app.route("/text")
def text():
    return render_template("Text.html")
