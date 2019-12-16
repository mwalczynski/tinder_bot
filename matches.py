from api.session import Session
from utils.image_formatter import show_images
from utils.requirements_checker import meets_requirements

from utils.secrets import SUBSCRIPTION_KEY_NAME, COGNITIVESERVICES_ENDPOINT

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


def get_image_description(client, image_url):
    described_image = client.describe_image(image_url)
    described_image.image_url = image_url
    return described_image


def initMatchGenerator():
    credentials = CognitiveServicesCredentials(SUBSCRIPTION_KEY_NAME)
    cv_client = ComputerVisionClient(COGNITIVESERVICES_ENDPOINT, credentials)

    session = Session()
    for user in session.yield_users():
        described_images = [get_image_description(cv_client, i) for i in user.photos]
        interesting_images = [i for i in described_images if meets_requirements(i)]

        isSmilingEnough = len(interesting_images) >= len(user.photos) / 2
        if isSmilingEnough:
            user.like()
        else:
            user.dislike()

        show_images(described_images, user)


if __name__ == '__main__':
    initMatchGenerator()