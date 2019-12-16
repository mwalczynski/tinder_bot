from urllib.request import urlopen
from PIL import Image

import matplotlib.pyplot as plt
import io

from utils.requirements_checker import meets_requirements, does_not_meet_requirements


def get_title(user, isSmilingEnough):
    if isSmilingEnough:
        title = "LIKED {0} ({1}), she seems to be a very positive person!".format(user.name, user.age)
    else:
        title = "DISLIKED {0} ({1}), she does not smile enough!".format(user.name, user.age)
    return title


def get_images(described_images):
    interesting_image_descriptions = [
        i for i in described_images if meets_requirements(i)
    ]
    interesting_images_urls = [
        i.image_url for i in interesting_image_descriptions
    ]
    interesting_fds = [urlopen(i) for i in interesting_images_urls]
    interesting_image_files = [io.BytesIO(fd.read()) for fd in interesting_fds]
    interesting_images = [Image.open(i) for i in interesting_image_files]

    not_interesting_image_descriptions = [i for i in described_images if does_not_meet_requirements(i)]
    not_interesting_images_urls = [i.image_url for i in not_interesting_image_descriptions]
    not_interesting_fds = [urlopen(i) for i in not_interesting_images_urls]
    not_interesting_image_files = [io.BytesIO(fd.read()) for fd in not_interesting_fds]
    not_interesting_images = [Image.open(i) for i in not_interesting_image_files]

    return interesting_images, not_interesting_images


def show_images(described_images, user):
    interesting_images, not_interesting_images = get_images(described_images)
    isSmilingEnough = len(interesting_images) >= len(user.photos) / 2

    first_col_len = len(interesting_images)
    second_col_len = len(not_interesting_images)

    number_of_images = sum([first_col_len, second_col_len])

    fig = plt.figure(figsize=(12, 6))
    axes_interesting = [
        fig.add_subplot(1, number_of_images, c + 1)
        for c in range(first_col_len)
    ]
    axes_not_interesting = [
        fig.add_subplot(1, number_of_images, c + first_col_len + 1)
        for c in range(second_col_len)
    ]

    for ax, image in zip(axes_interesting, interesting_images):
        ax.imshow(image)

    for ax, image in zip(axes_not_interesting, not_interesting_images):
        ax.imshow(image)

    for ax in axes_interesting:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.tick_params(color="green", labelcolor="green")
        for spine in ax.spines.values():
            spine.set_edgecolor("green")
            spine.set_linewidth(2)

    for ax in axes_not_interesting:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.tick_params(color="red", labelcolor="red")
        for spine in ax.spines.values():
            spine.set_edgecolor("red")
            spine.set_linewidth(2)

    title = get_title(user, isSmilingEnough)
    fig.suptitle(title, fontsize=16)
    plt.show()
