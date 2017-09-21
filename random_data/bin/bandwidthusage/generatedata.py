"""
Generate sample bandwidth data
"""
import random


#helper func
def get_user():
    """
    Args:
    Returns:
    """
    userslist = ['localhost', '192.168.1.1', '192.168.1.20']

    rand_userno = random.randint(0,2)
    user = userslist[rand_userno]

    return user


def get_bandwidth():
    """
    Args:
    Returns:
    """
    user = get_user()
    rand_download = round(random.uniform(200.50, 4000.70),2)
    rand_upload = round(random.uniform(200.50, 1000.70),2)

    event = "user={} download={} upload={}".format(user, rand_download, rand_upload)
    return event


