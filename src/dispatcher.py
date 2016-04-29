#!/usr/bin/env python3

from answer_maker import get_answer
from model import QuestionType
import database_utils


def itertools_to_list(iter):
    return [item for item in iter]


databases_ask_functions = {
    database_utils.CustomersWrapper.ask
}


class Dispatcher(object):
    @staticmethod
    def find_answer(meta_data):
        if meta_data is None:
            return None
        print(meta_data.attributes)
        if meta_data.question_type is QuestionType.CUSTOMERS:
            wrapper = database_utils.CustomersWrapper()
            return get_answer(meta_data, wrapper.ask(meta_data))
        if meta_data.question_type is QuestionType.DOWNLOADS:
            wrapper = database_utils.DownloadsWrapper()
            downloads_answer = wrapper.get(meta_data)
            if downloads_answer['message'] is "Success":
                return get_answer(meta_data, downloads_answer["result"][0])
            else:
                return (get_answer(meta_data, 0) + "\n" +
                        downloads_answer["message"])
