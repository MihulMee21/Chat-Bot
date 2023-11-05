import re
import Long_resposes as long

def message_probability(user_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_words=True

    for word in user_message:
        if word  in recognised_words:
            message_certainty +=1

    percentage = float(message_certainty)/float(len(recognised_words))


    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    
def check_all_message(message):
    highest_pron_list={}

    def response(Bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_pron_list
        highest_pron_list[Bot_response]=message_probability(message,list_of_words,single_response,required_words)

    # Response--------------------------------------------------------------------------------------------------------------
    response('Hello!',['Hello','hi','sup','hallo','hey'],single_response=True)
    response('I\'m doing fine,and you?',['how','are','you','doing'],required_words=['how'])
    response('Thank You!',['i','love','code','palace'],required_words=['code','palace'])
    response(long.R_eating,['what','are','you','eating'],required_words=['you','eat'])
    response(long.R_name,['what','is','your','name'],required_words=['your','is'])
   
    
    best_match=max(highest_pron_list,key=highest_pron_list.get)
    # print(highest_pron_list)

    return long.unknown() if highest_pron_list[best_match] < 1 else best_match



def get_response(user_input):
    split_Message=re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_message(split_Message)
    return response

# Testing the response system:-
while True:
    print('Bot: ' + get_response(input('You: ')))