

def make_dict(attributes: dict) -> dict:
    status_dict = {}
    filter_dict = {}

    if 'page' in attributes:
        status_dict['page'] = int(attributes['page'])
    if 'status' in attributes:
        status_dict['status'] = False
        if attributes['status'].lower() in 'new':
            status_dict['status'] = True
    if 'title' in attributes:
        filter_dict['title'] = str(attributes['title'])
    if 'description' in attributes:
        filter_dict['description'] = str(attributes['description'])
    if 'year' in attributes:
        filter_dict['year'] = int(attributes['year'])
    if 'rating' in attributes:
        filter_dict['rating'] = float(attributes['rating'])
    if 'genre_id' in attributes:
        filter_dict['genre_id'] = int(attributes['genre_id'])
    if 'director_id' in attributes:
        filter_dict['director_id'] = int(attributes['director_id'])

    return (status_dict, filter_dict)


def get_length_page(page: int = 1, length_page: int = 12) -> dict:
    limit = round(page * length_page)
    offset = limit - length_page
    return {'limit': limit, 'offset': offset}
