from pytest import mark,raises
from prs.parser.news import ParserInfo, ParserLinks
from .conftest import num_page,num_page_neg,count_url,count_url_neg



@mark.links
def test_links(num_page):
    parser_links = ParserLinks(num_page)
    parser_links.get_data()
    assert num_page in [i for i in range(parser_links.last_page())]

@mark.links
@mark.neg
def test_neg_links(num_page_neg):
    parser_links=ParserLinks(num_page_neg)
    with raises(AttributeError):
        parser_links.get_data()
        parser_links.process_data()
        assert num_page in [i for i in range(parser_links.last_page())]
        #assert bool(num_page)==parser_links.active_page()


@mark.info
def test_info(count_url,num_page):
    parser_links = ParserLinks(num_page)
    parser_links.get_data()
    parser_links.process_data()
    info=ParserInfo(parser_links.links[count_url])
    info.get_data()
    info.process_data()


@mark.info
@mark.neg
def test_neg_info(count_url_neg,num_page):
    parser_links = ParserLinks(num_page)
    parser_links.get_data()
    parser_links.process_data()
    with raises(TypeError):
        info=ParserInfo(parser_links.links[count_url])
        info.get_data()
        info.process_data()



    




