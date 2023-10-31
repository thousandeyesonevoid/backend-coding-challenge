import re

from api_service import fetch_gists_for_username, fetch_gist_details

def fetch_and_search(username: str, pattern: str):
    gists = fetch_all_gist_contents(username=username)
    if not gists:
        return { "success": False, "info": 'This username has no public gists', "matches": [] }
    compiled_pattern = re.compile(re.escape(pattern))
    matched_gists = [gist for gist in gists if gist_has_pattern(gist=gist, pattern=compiled_pattern)]
    if not matched_gists:
        return { "success": False, "info": 'This user does not have any code with this pattern present', "matches": [] }
    
    return { "success": True, "matches": matched_gists }

def fetch_all_gist_contents(username: str):
    gists, pagination_link = fetch_gists_for_username(username=username, page=1)
    total_pages = parse_total_number_of_pages(link=pagination_link)
    for page_number in (1, total_pages):
        paged_gists, _ = fetch_gists_for_username(username=username, page=page_number+1)
        gists += paged_gists
    return [ fetch_gist_details(gist_id=gist.get('id')) for gist in gists ]
        

def parse_total_number_of_pages(link: str):
    """ Parses the paginagtion """
    if link is None:
        return 1
    
    match = re.search("page=(\d+)>; rel=\"last\"", link)
    return int(match.group(1))

def gist_has_pattern(gist: hash, pattern: str):
    for _file_name, file_info in gist.get('files').items():
        if pattern.search(file_info.get('content')):
            return True
        
    return False