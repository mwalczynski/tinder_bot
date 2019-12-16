from api.session import Session
import requests
import json

from utils.config import FIRST_MESSAGE
from utils.secrets import QNAMAKER_KEY, QNAMAKER_ENDPOINT

headers = {
    "Authorization": "EndpointKey " + QNAMAKER_KEY,
    "Content-Type": "application/json",
}


def getChatBotAnswer(question):
    questionReq = {'question': question}
    response = requests.post(QNAMAKER_ENDPOINT,
                             headers=headers,
                             data=json.dumps(questionReq)).json()
    answer = response['answers'][0]['answer']
    return answer


def initChatBot():
    session = Session()
    while True:
        matches = session.yield_matches()
        for match in matches:
            messageList = [x for x in match.get_messages()]
            if messageList:
                lastMessage = messageList[-1]
                if lastMessage.sender == "Me":
                    continue

                question = lastMessage.body
                answer = getChatBotAnswer(question)
                match.message(answer)
            else:
                match.message(FIRST_MESSAGE)


# initChatBot()
if __name__ == '__main__':
    initChatBot()