import re

from api_service import fetch_gists_for_username, fetch_gist_details


def fetch_and_search(username: str, pattern: str):
    """
    handles the fetch and search pattern calls
    """
    gists = fetch_all_gist_contents(username=username)
    if not gists:
        return {
            "success": False,
            "info": "This username has no public gists",
            "matches": [],
        }
    matched_gists = [
        gist for gist in gists if gist_has_pattern(gist=gist, pattern=pattern)
    ]
    if not matched_gists:
        return {
            "success": False,
            "info": "This user does not have any code with this pattern present",
            "matches": [],
        }

    return {"success": True, "matches": matched_gists}


def fetch_all_gist_contents(username: str):
    """Fetches all gists and then details of each gist for the provided username"""
    gists, pagination_link = fetch_gists_for_username(username=username, page=1)
    total_pages = parse_total_number_of_pages(link=pagination_link)
    for page_number in range(1, total_pages):
        paged_gists, _ = fetch_gists_for_username(
            username=username, page=page_number + 1
        )
        gists += paged_gists
    return [fetch_gist_details(gist_id=gist.get("id")) for gist in gists]


def parse_total_number_of_pages(link: str):
    """Parses the pagination link"""
    if link is None:
        return 1

    match = re.search('page=(\\d+)>; rel="last"', link)
    return int(match.group(1))


def gist_has_pattern(gist: hash, pattern: str):
    """
    checks if any of the files in the gist has the pattern in it's contents
    """
    compiled_pattern = re.compile(re.escape(pattern))
    for _file_name, file_info in gist.get("files").items():
        if compiled_pattern.search(file_info.get("content")):
            return True

    return False
