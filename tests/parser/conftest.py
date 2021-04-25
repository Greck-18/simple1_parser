from pytest import fixture, mark


@fixture(params=(i for i in range(51)))
def count_url(request):
    return request.param


@fixture(params=(i for i in range(1,7)))
def num_page(request):
    return request.param

@fixture(params=[7,8,9,10,-1,0,-123,55,99])
def num_page_neg(request):
    return request.param


@fixture(params=[-1,-1234,3545,99,10000,-99,123214124])
def count_url_neg(request):
    return request.param