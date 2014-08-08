import searches
import json
from django.http import HttpResponse


def wrap_json(request, payload):
    """
    return HttpResponse with data correctly formatted for json or jsonp
    depending on the request
    """
    if 'callback' in request.GET:
        return HttpResponse('{}({})'.format(
            request.GET['callback'],
            json.dumps(payload)), content_type='text/javascript')
    else:
        return HttpResponse(json.dumps(payload),
                            content_type='application/json')


def topics(request):
    """
    return a list of paired topic names and ids
    """
    return wrap_json(request, searches.topics())


def search(request):
    """
    perform a search and return the matches
    recognised parameters are: topics, results_limit, page, string
    """
    return wrap_json(request, searches.search(request.GET))


def show(request):
    """
    fetch all shownotes belonging to a specific show number
    """
    return wrap_json(request, searches.show(request.GET))


def note(request):
    """
    retrieve details of a specific note by id
    """
    payload = []
    if 'id' in request.GET and request.GET['id'].isdigit():
        payload = searches.note(int(request.GET['id']))
    return wrap_json(request, payload)