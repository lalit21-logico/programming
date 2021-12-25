import scrapy


class ProductSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['net-a-porter.com']
    # this list  used for past the required urls to scrap the data
    start_urls = [
        'https://www.net-a-porter.com/en-in/shop/clothing/tops',
        'https://www.net-a-porter.com/en-in/shop/shoes',
    ]
    # for adding 40 page link of 20-20 for each footwaer and topwear
    for i in range(2, 30):
        start_urls.append(
            'https://www.net-a-porter.com/en-in/shop/clothing/tops?pageNumber='+str(i)+'')
        start_urls.append(
            'https://www.net-a-porter.com/en-in/shop/shoes?pageNumber='+str(i)+'')

    def parse(self, response):
        # creating list of url of product page and img_src because of problem faced of url extract  while get product data.
        pro_url = [a.attrib['href']
                   for a in response.css('div.ProductGrid52 a')]

        # code for category
        if 'Tops' == response.css('div.app div.ProductListingPage52 div.ContentHeader6 div.Header6.ContentHeader6__container div.Header6__content.ContentHeader6__content div.Header6__headingsContainer h1.Header6__title.Header6__title--large::text').get():
            category = 'topwear'
        else:
            category = 'footwear'

        # iterate response to get product data
        index = -1
        for product in response.css('a div.ProductItem24'):
            index += 1
            yield {
                # html body main.content div.app div.ProductListingPage52 section.ProductListingPage52__gutterWrapper div.ProductListingPage52__layoutGridWrapper div.ProductListingPage52__layoutGrid div.ProductGrid52.ProductListWithLoadMore52__listingGrid a div#pid-24062987016703457.ProductItem24.ProductList52__productItem div.ProductItem24__p div.ProductItem24__skeletonContainer div.ProductItem24__content span.ProductItem24__details.ProductItem24__details--brief span.ProductItem24__designer
                'name': product.css('div.ProductItem24__p div.ProductItem24__skeletonContainer div.ProductItem24__content span.ProductItem24__details.ProductItem24__details--brief span.ProductItem24__name::text').get(),
                'brand': product.css('div.ProductItem24__p div.ProductItem24__skeletonContainer div.ProductItem24__content span.ProductItem24__details.ProductItem24__details--brief span.ProductItem24__designer::text').get(),
                'original_price': product.css('div.ProductItem24__p div.ProductItem24__skeletonContainer div.ProductItem24__content div.PriceWithSchema9.ProductItem24__price span.PriceWithSchema9__value span::text').get(),
                'sale_price': product.css('div.ProductItem24__p div.ProductItem24__skeletonContainer div.ProductItem24__content div.PriceWithSchema9.ProductItem24__price span.PriceWithSchema9__value span::text').get(),
                'image_url': product.xpath('//div/div/div[1]/div/div/div[1]/div/div/div/picture/img/@src').get(),
                'product_page_url': 'https://www.net-a-porter.com'+pro_url[index],
                'product_category': category,
            }
