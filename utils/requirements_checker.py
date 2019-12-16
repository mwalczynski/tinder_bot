INTERESTING_TAGS = ["smiling"]


def meets_requirements(image):
    return all(tag in image.tags for tag in INTERESTING_TAGS)


def does_not_meet_requirements(image):
    return not all(tag in image.tags for tag in INTERESTING_TAGS)