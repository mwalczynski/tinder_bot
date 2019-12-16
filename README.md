# Tinder Bot
Welcome to simple Tinder Bot. It was created to show possibilities of Microsoft Azure Cognitive Services (read more here [https://azure.microsoft.com/pl-pl/services/cognitive-services/](https://azure.microsoft.com/pl-pl/services/cognitive-services/)). Tinder api bindings were taken from [MMcintire96/python_TinderAPI](https://github.com/MMcintire96/python_TinderAPI)

# Getting Started

To start using the bot you have to fill missing values in **utils/secrets.py**. To get each of them follow the instructions below.

## Tinder token
- login to [Tinder] (https://tinder.com/) in a browser
- open developer tools
- go to application tab
- from local storage select https://tinder.com
- copy value for TinderWeb/APIToken

## Your subscription key and Azure Cognitive Services endpoint
You will receive after creating Cognitive Services service.
For more details follow https://docs.microsoft.com/en-us/sandbox/demos/nothotdog.

## Your QnA Maker key QnA Maker endpoint
You will receive after creating QnA Maker service.
For more details follow https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-qna?view=azure-bot-service-4.0&tabs=cs.

# Usage
Just run `python chat.py` or `python matches.py` to run each of the modules.