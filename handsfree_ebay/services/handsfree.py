from handsfree_ebay.services import bingspeech
from handsfree_ebay.services import ebay

user_item_summaries = {}
user_current_item = {}


def read_basic_result(item_num, item_summaries):
    text = ebay.get_basic_info(item_summaries[item_num])
    audio_response = bingspeech.get_tts_audio(text)
    return audio_response


def read_details(item_num, item_summaries):
    text = ebay.get_details(item_summaries[item_num])
    audio_response = bingspeech.get_tts_audio(text)
    return audio_response


def clean_up(user):
    del user_item_summaries[user]
    del user_current_item[user]
    return


def unknown_command():
    # TODO have this response stored instead of calling for it each time
    audio_response = bingspeech.get_tts_audio('sorry, I don\'t know that command.')
    return audio_response


def provide_search_terms(audio_file, user):
    search_terms = bingspeech.get_stt_text(audio_file)
    json_results = ebay.search_for(search_terms)
    item_summaries = json_results.get('itemSummaries')
    user_item_summaries[user] = item_summaries
    user_current_item[user] = 0

    audio_response = read_basic_result(0, item_summaries)
    return audio_response


def provide_user_reply(audio_file, user):
    if user not in user_item_summaries.keys():
        return None
    
    reply_text = bingspeech.get_stt_text(audio_file)
    reply_text = reply_text.lower().strip()
    if reply_text.startswith('more detail'):
        audio_response = read_details(user_current_item.get(user), user_item_summaries.get(user))
    elif reply_text.startswith('next result'):
        if user_current_item.get(user) < 2:
            user_current_item[user] += 1
            audio_response = read_basic_result(user_current_item.get(user), user_item_summaries.get(user))
        else:
            audio_response = None
    elif reply_text.startswith('done'):
        audio_response = None
        clean_up(user)
    else:
        audio_response = unknown_command()
        
    return audio_response
