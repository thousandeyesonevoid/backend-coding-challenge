from gistapi.github_service import parse_total_number_of_pages, gist_has_pattern, fetch_all_gist_contents, fetch_and_search

def test_parse_total_number_of_pages_nil():
    assert parse_total_number_of_pages(link=None) == 1

def test_parse_total_number_of_pages():
    link = '<https://api.github.com/user/abcd/gists?page=2>; rel="next", <https://api.github.com/user/abcd/gists?page=10>; rel="last"'
    assert parse_total_number_of_pages(link=link) == 10

def test_gist_has_pattern_no_pattern():
    gist = {
        "files": {
            "file1.py": { "content": "import abcd \n print('hello world')" }
        }
    }
    pattern = 'import lmno'
    assert gist_has_pattern(gist, pattern) == False

def test_gist_has_pattern():
    gist = {
        "files": {
            "file1.py": { "content": "import lmno \n print('hello world')" }
        }
    }
    pattern = 'import lmno'
    assert gist_has_pattern(gist, pattern) == True

def test_fetch_all_gist_contents(mocker):
    gistList = [
        {
            "id": "123456"            
        }
    ]
    gistDetails = {   
        "id": "123456",
        "files": {
            "file1.py": { "content": "import lmno \n print('hello world')" }
        }
    }
    gists_api_mock = mocker.patch("gistapi.github_service.fetch_gists_for_username", return_value=(gistList, None))
    details_api_mock = mocker.patch("gistapi.github_service.fetch_gist_details", return_value=gistDetails)
    results = fetch_all_gist_contents(username='testuser')

    assert results == [gistDetails]
    gists_api_mock.assert_called_once_with(username='testuser', page=1)
    details_api_mock.assert_called_once_with(gist_id="123456")

def test_fetch_and_search_no_gists(mocker):
    mocker.patch('gistapi.github_service.fetch_all_gist_contents', return_value=[])
    result = fetch_and_search(username='testuser', pattern="pattern")

    assert result.get('success') == False
    assert result.get('info') ==  'This username has no public gists'
    assert result.get('matches') == []

def test_fetch_and_search_no_matches(mocker):
    gists = [
        {   
            "id": "123456",
            "files": {
                "file1.py": { "content": "import lmno \n print('hello world')" }
            }
        }
    ]
    mocker.patch('gistapi.github_service.fetch_all_gist_contents', return_value=gists)
    mocker.patch('gistapi.github_service.gist_has_pattern', return_value=False)
    result = fetch_and_search(username='testuser', pattern="pattern")

    assert result.get('success') == False
    assert result.get('info') ==  'This user does not have any code with this pattern present'
    assert result.get('matches') == []

def test_fetch_and_search_has_matches(mocker):
    gists = [
        {   
            "id": "123456",
            "files": {
                "file1.py": { "content": "import lmno \n print('hello world')" }
            }
        }
    ]
    mocker.patch('gistapi.github_service.fetch_all_gist_contents', return_value=gists)
    mocker.patch('gistapi.github_service.gist_has_pattern', return_value=True)
    result = fetch_and_search(username='testuser', pattern="pattern")

    assert result.get('success') == True
    assert result.get('matches') == gists
