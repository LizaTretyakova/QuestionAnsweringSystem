#!/usr/bin/env python3

from src.attributes import parse
from src.dispatcher import Dispatcher


# TODO: make it a module and use the library
def process_question(question):
    return Dispatcher.find_answer(parse(question))


def run():
    try:
        run.questions
    except AttributeError:
        run.questions = [
            "How many downloads were made from Asia in 2015?",
            "How many customers bought PyCharm in European Union 2 years ago?",
            "How many times PyCharm was downloaded from North America?",
            "How many PyCharm downloads were made from Tirol?",
            "How many PyCharm downloads were made from Siberia?",
            "How many PyCharm downloads were made from Bavaria?",

            "how many downloads were there in Russia?",
            "how many downloads were there in 2015?",
            "how many downloads were in 2016?",
            "how many downloads were in Russia in 2015?",
            "how many downloads were there in Nigeria in 2014?",
            "how many downloads were made in Russia and Germany?",
            "How many customers were in China in 2015?",
            "how many customers are there in Japan?",
            "How many customers are there in Japan?",
            "How many PyCharm downloads were made in 2014?",
            "How many times PyCharm was downloaded in 2015?",
            "When was DataGrip released?",
            "When is PyCon 2016?",
            "How many downloads have been since 2015?",
            "how many downloads were 1 year ago?",
            "How many customers were since 2015?",

            "dkfsdlkgjhslkrghkrgjhlkj dkfjhgdlsfkjhg dfgjhkshg fgdsklhg?",
            "How many downloads of PyCharm were made from Russia in 2014?",
            "How many different products are downloaded from Russia?", # potentially okay question
            "How many downloads of PyCharm were made from Russia from 2013 to 2015?",
            "How many downloads of PyCharm were made from Russia between 2013 and 2015?",
            "What was the number of licences of PyCharm sold in Russia in 2014?",
            "What was the number of licences of PyCharm bought in Russia in 2014?",
            "What was the number of licences of PyCharm downloaded in Russia in 2014?",
            "What is the number of PyCharm downloads?",
            "Which number of clients bought PyCharm in 2014?",
            "Which number of clients downloaded PyCharm in 2014?",
            "What was the country of the latest PyCharm download?",
            "What was the time of the first PyCharm download?",
            "What number of countries is PyCharm downloaded from?",
            "When was the last PyCharm download?",
            "How many customers have been since 2000?",
            "How many downloads were from 2000 to 2016 except 2015?",
            "How many downloads were till 2016 without 2015?",
            "When have xamarin been downloaded?",
            "How many downloads of PyCharm were made from Munich in 2014?",
            "How many different products are downloaded from Saint Petersburg?", # potentially okay question
            "how many downloads were there in Munich and Saint Petersburg?",
            "How many customers were there in 2000 and 2011?",
            "How many customers are there in United States of America?",
            "How many customers are there in Russia?",
            "How many customers were there in 2012?",
            "How many customers were there during 2012?",
            "How many downloads were there within 2014 and 2015?",
            "How many downloads were?",
            "How many downloads were there?"
        ]

    for question in run.questions:
        print(question)
        print(process_question(question))
        print("***")
