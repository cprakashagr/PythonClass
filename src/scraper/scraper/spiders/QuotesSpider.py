import scrapy


class QuotesSpider(scrapy.Spider):

    name = "Quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        print(response.url)
        # print(response.body)
        # print('\n\n\n\n')


        '''

        Command Line Executions:

% scrapy shell 'http://quotes.toscrape.com/page/1/'                                                                                                                                                                                                                 ✹ ✭

>>> reponse.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

>>> response.css('title').extract_first()
'<title>Quotes to Scrape</title>'

>>> response.css('title').extract()[0]


>>> len(response.css('a').extract())
55

>>> response.css('a::text').extract()
['Quotes to Scrape', 'Login', '(about)', 'change', 'deep-thoughts', 'thinking', 'world', '(about)', 'abilities', 'choices', '(about)', 'inspirational', 'life', 'live', 'miracle', 'miracles', '(about)', 'aliteracy', 'books', 'classic', 'humor', '(about)', 'be-yourself', 'inspirational', '(about)', 'adulthood', 'success', 'value', '(about)', 'life', 'love', '(about)', 'edison', 'failure', 'inspirational', 'paraphrased', '(about)', 'misattributed-eleanor-roosevelt', '(about)', 'humor', 'obvious', 'simile', 'Next ', 'love', 'inspirational', 'life', 'humor', 'books', 'reading', 'friendship', 'friends', 'truth', 'attributed-no-source', 'GoodReads.com', 'Scrapinghub']


>>> quotes = response.css('div.quote').extract()

>>> quotes = response.css('div.quote')
>>> quote = quotes[0]


>>> quote.css('span.text')
[<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]" data='<span class="text" itemprop="text">“The '>]


>>> quote.css('span.text')
[<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“The world as we have created it is a pr'>]


>>> quote.css('small.author::text').extract()
['Albert Einstein']


>>> response.css('li a').extract()
['<a href="/page/2/">Next <span aria-hidden="true">→</span></a>']






        '''
        pass
