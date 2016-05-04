from src.model import TimeAttribute
from datetime import date
import re


def get_attribute_time_spacy(doc, question):
    times = []
    for ent in doc.ents:
        if ent.label_ == "DATE":
            times.append(ent)

    except_prepositions = []
    prepositions = []
    except_date = []

    from_date_for_segment = None

    from_date = None
    to_date = None

    time_attribute = TimeAttribute()

    for time in times:
        if "ago" in time.orth_:
            cur_year = date.today().year
            count_years = find_number(time.orth_)
            from_date = cur_year - count_years
            to_date = cur_year - count_years
            prepositions = ["in"]
            time_attribute.add_segment(from_date, to_date)
            continue
        if "between" in time.orth_:
            part1 = time.orth_.split("and")[0]
            part2 = time.orth_.split("and")[1]
            from_date = find_number(part1)
            to_date = find_number(part2)
            prepositions = ["between"]
            time_attribute.add_segment(from_date, to_date)
            continue
        preposition = time.root.head
        if preposition.orth_ == "since":
            from_date = find_number(time.orth_)
            to_date = None
            prepositions = ["since"]
            time_attribute.add_segment(from_date, None)
        elif preposition.orth_ == "from":
            prepositions = ["from"]
            if "to" in time.orth_:
                prepositions.append("to")
            elif "until" in time.orth_:
                prepositions.append("until")
            elif "till" in time.orth_:
                prepositions.append("till")
            if len(prepositions) > 1:
                part1 = time.orth_.split(prepositions[1])[0]
                part2 = time.orth_.split(prepositions[1])[1]
                from_date = find_number(part1)
                to_date = find_number(part2)
                time_attribute.add_segment(from_date, to_date)
                continue
            from_date = find_number(time.orth_)
            if from_date_for_segment is not None:
                time_attribute.add_segment(from_date_for_segment, None)
            from_date_for_segment = find_number(time.orth_)
        elif preposition.orth_ == "to" or preposition.orth_ == "till" or preposition.orth_ == "until":
            prepositions.append(preposition.orth_)
            to_date = find_number(time.orth_)
            time_attribute.add_segment(from_date_for_segment, to_date)
            from_date_for_segment = None
        elif preposition.orth_ == "after" or preposition.orth_ == "by":
            from_date = find_number(time.orth_)
            to_date = None
            prepositions = ["after"]
            time_attribute.add_segment(from_date, None)
        elif preposition.orth_ == "before":
            from_date = None
            to_date = find_number(time.orth_)
            prepositions = ["before"]
            time_attribute.add_segment(None, to_date)
        elif preposition.orth_ == "in" or preposition.orth_ == "within":
            from_date = find_number(time.orth_)
            to_date = find_number(time.orth_)
            prepositions = [preposition.orth_]
            time_attribute.add_segment(from_date, to_date)
        elif preposition.orth_ == "except" or preposition.orth_ == "without":
            except_value = find_number(time.orth_)
            except_date.append(except_value)
            except_prepositions.append(preposition.orth_)
            time_attribute.add_except_segment(except_value, except_value)

    find_another_dates(doc, time_attribute)
    print(from_date, to_date, prepositions, except_date, except_prepositions)
    time_attribute.eval_real_segments()

    time_attribute.from_date = from_date
    time_attribute.to_date = to_date
    time_attribute.except_date = except_date
    time_attribute.except_prepositions = except_prepositions

    print(time_attribute.real_segments)

    return time_attribute


def find_another_dates(doc, time_attribute):
    from_date_for_segment = None
    for token in doc:
        if token.is_digit:
            cur_token = token
            while cur_token.head is not cur_token and cur_token.dep_ == "conj":
                cur_token = cur_token.head
            cur_token = cur_token.head
            if cur_token.orth_ == "in":
                time_attribute.add_segment(find_number(token.orth_), find_number(token.orth_))
            if cur_token.orth_ == "without" or cur_token.orth_ == "except":
                time_attribute.add_except_segment(find_number(token.orth_), find_number(token.orth_))
            if cur_token.orth_ == "from":
                if from_date_for_segment is not None:
                    time_attribute.add_segment(from_date_for_segment, None)
                from_date_for_segment = find_number(token.orth_)
            if cur_token.orth_ == "till":
                time_attribute.add_segment(from_date_for_segment, find_number(token.orth_))
                from_date_for_segment = None


def find_number(text):
    search_result = re.search('\d+', text)
    if search_result is not None:
        return int(search_result.group(0))
    else:
        return None


def get_attribute_time(question):
    search_result = re.search('in (\d+)', question)
    if search_result is not None:
        time = search_result.group(1)
        return TimeAttribute(start=time, end=time)
    else:
        return TimeAttribute()
