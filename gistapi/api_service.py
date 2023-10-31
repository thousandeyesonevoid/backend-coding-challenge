import requests

def fetch_gists_for_username(username: str, page: int):
    """Provides the list of gist metadata for a given user.
    Args:
        username (string): the user to query gists for

    Returns:
        A list of public gists based on the page number
    """
    gists_url = f'https://api.github.com/users/{username}/gists?page={page}'
    response = requests.get(gists_url)
    return response.json(), response.headers.get('link')

def fetch_gist_details(gist_id: str):
    """Provides details for the gist associated with the id passed in
    Args:
        gist_id (string): the identifier for the gist the details are to be fetched for

    Returns:
        The dict parsed from the json response from the Github API.  See
    """
    gist_details_url = f'https://api.github.com/gists/{gist_id}'
    response = requests.get(gist_details_url)
    return response.json()
