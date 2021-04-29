from pytest import fixture, mark


@fixture(params=(i for i in range(15)))
def count_url(request):
    return request.param


@fixture(params=(i for i in range(7)))
def num_page(request):
    return request.param

@fixture(params=[7,8,9,10,-1,-123,55,99,1014,-3435,'fgfg',True])
def num_page_neg(request):
    return request.param


@fixture(params=[-1,-1234,3545,99,10000,-99,123214124])
def count_url_neg(request):
    return request.param