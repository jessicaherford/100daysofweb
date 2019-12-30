from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from billpro.data import repository


@view_config(route_name='home', renderer='../templates/home/default.jinja2')
def home(_: Request):
    user_id = 1  # probably would get from a cookie

    user = repository.get_user_by_id(user_id, include_bills=True)
    return {
        'user': user,
    }


@view_config(route_name='details', renderer='../templates/home/details.jinja2', request_method='GET')
def details_get(request: Request):
    bill_id = int(request.matchdict.get('bill_id'))
    bill = repository.get_user_by_id(bill_id)
    if not bill:
        return Response(status=404)

    user_id = 1
    user = repository.get_user_by_id(user_id)

    return {
        'user': user,
        'bill': bill
    }


@view_config(route_name='details', renderer='../templates/home/details.jinja2')
def details_post(request: Request):
    user_id = 1  # probably would get from a cookie

    user = repository.get_user_by_id(user_id, include_bills=True, request_method='POST')
    return {
        'user': user,
    }