import requests


def get_v1_account():
    """
    Get current user
    :return:
    """

    url = "http://5.63.153.31:5051/v1/account"
    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5CdS6VgrXhgGsVK1ULfL4rMDxWCa7nvG6D34NDIImajtxAP/fi9E1ckh4jQANlZhouVlc94b348kLS0zo'
                           'OXk7pc6BiToSVhk4vuR/TWe3aeXoECJar+Rt6NsTgSfSQEhkg=',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="GET",
        url=url,
        headers=headers
    )

    return response
