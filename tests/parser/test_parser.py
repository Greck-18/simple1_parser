from pytest import mark,raises
from prs.parser.news import ParserInfo, ParserLinks
from .conftest import num_page,num_page_neg,count_url



@mark.links
def test_links(num_page):
    parser_links = ParserLinks(num_page)
    parser_links.get_data()
    assert bool(num_page) == parser_links.active_page()


@mark.links
@mark.neg
def test_neg_links(num_page_neg):
    parser_links=ParserLinks(num_page_neg)
    with raises(AttributeError):
        parser_links.get_data()
        parser_links.process_data()
        #assert bool(num_page)==parser_links.active_page()


@mark.info
def test_info(count_url,num_page):
    parser_links = ParserLinks(num_page)
    parser_links.get_data()
    parser_links.process_data()
    info=ParserInfo(parser_links.links[count_url])
    info.get_data()
    info.process_data()

    




