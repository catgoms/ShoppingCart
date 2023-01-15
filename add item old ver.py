
def add_item1():
    x = v.get()
    global html_info
    global html_no_buy
    global invoice_html
    global total_price

    # Change the invoice html so it can add items without exiting the GUI
    invoice_html = invoice_html.replace(html_no_buy, '<!--#INFO-->')
    invoice_html = invoice_html.replace(html_info, '<!--#INFO-->')
    html_info = html_info.replace('amount: <b>$'+str("{0:.02f}".format(total_price)),
                                  'amount: <b>$#TOTAL_PRICE')

    # Include the html items to Invoice html
    html_info = html_info.replace('<!--#ITEMS-->', html_items)

    # Wished For Jewellery
    if x == 1:
        # Open and read xhtml file
        html_file = open('WishedForJewellery.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()

        # Find the location of the item tag
        item_tag = html_text.find('<item>')
        
        # Find the name of the item
        name_start = html_text.find("<title>", item_tag) + len("<title>")
        name_end = html_text.find("</title>", name_start)
        item_name = html_text[name_start:name_end]

        # Find the price of the item
        price_start = html_text.find('class=&quot;price&quot;&gt;', item_tag) + len('class=&quot;price&quot;&gt;')
        price_end = html_text.find(' GBP&lt;/p&gt;', price_start)
        item_price = html_text[price_start:price_end]

        # Find the image of the item
        image_start = html_text.find('img src=&quot;', item_tag) + len('img src=&quot;')
        image_end = html_text.find('&quot;', image_start)
        item_image = html_text[image_start:image_end]

        # Replace currency and price
        html_info = html_info.replace('#CURRENCY', 'GBP')
        html_info = html_info.replace('#PRICE', item_price)

        # Add currency converted amount to the list
        total_price_list.append(float(item_price) * 1.77)

    # Navy Lumbar Pillows
    if x == 2:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read xhtml file
        html_file = open('NavyLumbarPillows.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()

        # Find the location of the item tag
        item_tag = html_text.find('<item>')
        
        # Find the name of the item
        name_start = html_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
        name_end = html_text.find("]]></title>", name_start)
        item_name = html_text[name_start:name_end]

        # Find the price of the item
        price_start = html_text.find('<price>$', item_tag) + len('<price>$')
        price_end = html_text.find('</price>', price_start)
        item_price = html_text[price_start:price_end]

        # Find the image of the item
        image_start = html_text.find('src="', item_tag) + len('src="')
        image_end = html_text.find('"', image_start)
        item_image = html_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'USD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add currency converted amount to the list
        total_price_list.append(float(item_price) * 1.32)

    # New Coats
    elif x == 3:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read web document
        web_page = urlopen("https://www.ebay.com.au/sch/i.html?&_nkw=coat&_sop=10&LH_BIN=1&_rss=1")
        web_text = web_page.read().decode('UTF-8')
        
        # Find the name of the item
        item_tag = web_text.find('<item>')
        name_start = web_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
        name_end = web_text.find("]]></title>", name_start)
        item_name = web_text[name_start:name_end]

        # Find the price of the item
        price_start = web_text.find('<strong><b>AU $</b>', item_tag) + len('<strong><b>AU $</b>')
        price_end = web_text.find('</strong>', price_start)
        item_price = web_text[price_start:price_end]

        # Find the image of the item
        image_start = web_text.find('src="', item_tag) + len('src="')
        image_end = web_text.find('">', image_start)
        item_image = web_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'AUD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add amount to the list
        total_price_list.append(float(item_price))

    # Best Sellers in Musics
    elif x == 4:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read web document
        web_page = urlopen("https://www.amazon.com.au/gp/rss/bestsellers/music")
        web_text = web_page.read().decode('UTF-8')
        
        # Find the artist of the item
        item_tag = web_text.find('<item>')
        artist_start = web_text.find('"riRssContributor">', item_tag) + len('"riRssContributor">')
        artist_end = web_text.find(' <span class="byLinePipe">', artist_start)
        item_artist = web_text[artist_start:artist_end]
        
        # Find the name of the item
        name_start = web_text.find("<title>", item_tag) + len("<title>")
        name_end = web_text.find("</title>", name_start)
        item_name = web_text[name_start:name_end] + ' - ' + item_artist

        # Find the price of the item
        price_start = web_text.find('<span class="price">$', item_tag) + len('<span class="price">$')
        price_end = web_text.find('</span><br />', price_start)
        item_price = web_text[price_start:price_end]

        # Find the image of the item
        image_start = web_text.find('<img src="', item_tag) + len('<img src="')
        image_end = web_text.find('"', image_start)
        item_image = web_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'AUD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add amount to the list
        total_price_list.append(float(item_price))

    # Replace items name and image
    html_info = html_info.replace('#NAME', item_name)
    html_info = html_info.replace('#IMAGE', item_image)


def add_item2():
    x = v.get()
    global html_info
    global html_no_buy
    global invoice_html
    global total_price

    # Change the invoice html so it can add items without exiting the GUI
    invoice_html = invoice_html.replace(html_no_buy, '<!--#INFO-->')
    invoice_html = invoice_html.replace(html_info, '<!--#INFO-->')
    html_info = html_info.replace('amount: <b>$'+str(round(total_price, 2)),
                                  'amount: <b>$#TOTAL_PRICE')

    # Include the html items to Invoice html
    html_info = html_info.replace('<!--#ITEMS-->', html_items)

    # Wished For Jewellery
    if x == 1:
        # Open and read xhtml file
        html_file = open('WishedForJewellery.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()

        # Find the location of the item tag
        start = html_text.find('</item>')
        item_tag = html_text.find('<item>', start)
        
        # Find the name of the item
        name_start = html_text.find("<title>", item_tag) + len("<title>")
        name_end = html_text.find("</title>", name_start)
        item_name = html_text[name_start:name_end]

        # Find the price of the item
        price_start = html_text.find('class=&quot;price&quot;&gt;', item_tag) + len('class=&quot;price&quot;&gt;')
        price_end = html_text.find(' GBP&lt;/p&gt;', price_start)
        item_price = html_text[price_start:price_end]

        # Find the image of the item
        image_start = html_text.find('img src=&quot;', item_tag) + len('img src=&quot;')
        image_end = html_text.find('&quot;', image_start)
        item_image = html_text[image_start:image_end]

        # Replace currency and price
        html_info = html_info.replace('#CURRENCY', 'GBP')
        html_info = html_info.replace('#PRICE', item_price)

        # Add currency converted amount to the list
        total_price_list.append(float(item_price) * 1.77)

    # Navy Lumbar Pillows
    elif x == 2:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read xhtml file
        html_file = open('NavyLumbarPillows.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()

        # Find the location of the item tag
        start = html_text.find('</item>')
        item_tag = html_text.find('<item>', start)
        
        # Find the name of the item
        name_start = html_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
        name_end = html_text.find("]]></title>", name_start)
        item_name = html_text[name_start:name_end]

        # Find the price of the item
        price_start = html_text.find('<price>$', item_tag) + len('<price>$')
        price_end = html_text.find('</price>', price_start)
        item_price = html_text[price_start:price_end]

        # Find the image of the item
        image_start = html_text.find('src="', item_tag) + len('src="')
        image_end = html_text.find('"', image_start)
        item_image = html_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'USD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add currency converted amount to the list
        total_price_list.append(float(item_price) * 1.32)

    # New Coats
    elif x == 3:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read web document
        web_page = urlopen("https://www.ebay.com.au/sch/i.html?&_nkw=coat&_sop=10&LH_BIN=1&_rss=1")
        web_text = web_page.read().decode('UTF-8')

        # Find the location of the item tag
        start = web_text.find('</item>')
        item_tag = web_text.find('<item>', start)
        
        # Find the name of the item
        name_start = web_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
        name_end = web_text.find("]]></title>", name_start)
        item_name = web_text[name_start:name_end]

        # Find the price of the item
        price_start = web_text.find('<strong><b>AU $</b>', item_tag) + len('<strong><b>AU $</b>')
        price_end = web_text.find('</strong>', price_start)
        item_price = web_text[price_start:price_end]

        # Find the image of the item
        image_start = web_text.find('src="', item_tag) + len('src="')
        image_end = web_text.find('">', image_start)
        item_image = web_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'AUD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add amount to the list
        total_price_list.append(float(item_price))

    # Best Sellers in Musics
    elif x == 4:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read web document
        web_page = urlopen("https://www.amazon.com.au/gp/rss/bestsellers/music")
        web_text = web_page.read().decode('UTF-8')

        # Find the location of the item tag
        start = web_text.find('</item>')
        item_tag = web_text.find('<item>', start)
        
        # Find the artist of the item
        artist_start = web_text.find('"riRssContributor">', item_tag) + len('"riRssContributor">')
        artist_end = web_text.find(' <span class="byLinePipe">', artist_start)
        item_artist = web_text[artist_start:artist_end]
        
        # Find the name of the item
        name_start = web_text.find("<title>", item_tag) + len("<title>")
        name_end = web_text.find("</title>", name_start)
        item_name = web_text[name_start:name_end] + ' - ' + item_artist

        # Find the price of the item
        price_start = web_text.find('<span class="price">$', item_tag) + len('<span class="price">$')
        price_end = web_text.find('</span><br />', price_start)
        item_price = web_text[price_start:price_end]

        # Find the image of the item
        image_start = web_text.find('<img src="', item_tag) + len('<img src="')
        image_end = web_text.find('"', image_start)
        item_image = web_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'AUD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add amount to the list
        total_price_list.append(float(item_price))

    # Replace items name and image
    html_info = html_info.replace('#NAME', item_name)
    html_info = html_info.replace('#IMAGE', item_image)

def add_item3():
    x = v.get()
    global html_info
    global html_no_buy
    global invoice_html
    global total_price

    # Change the invoice html so it can add items without exiting the GUI
    invoice_html = invoice_html.replace(html_no_buy, '<!--#INFO-->')
    invoice_html = invoice_html.replace(html_info, '<!--#INFO-->')
    html_info = html_info.replace('amount: <b>$'+str(round(total_price, 2)),
                                  'amount: <b>$#TOTAL_PRICE')

    # Include the html items to html info
    html_info = html_info.replace('<!--#ITEMS-->', html_items)

    # Wished For Jewellery
    if x == 1:
        # Open and read xhtml file
        html_file = open('WishedForJewellery.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()

        # Find the location of the item tag
        start = 0
        for tag in range(3):
            item_tag = html_text.find('<item>', start)
            start = item_tag + 1
        
        # Find the name of the item
        name_start = html_text.find("<title>", item_tag) + len("<title>")
        name_end = html_text.find("</title>", name_start)
        item_name = html_text[name_start:name_end]

        # Find the price of the item
        price_start = html_text.find('class=&quot;price&quot;&gt;', item_tag) + len('class=&quot;price&quot;&gt;')
        price_end = html_text.find(' GBP&lt;/p&gt;', price_start)
        item_price = html_text[price_start:price_end]

        # Find the image of the item
        image_start = html_text.find('img src=&quot;', item_tag) + len('img src=&quot;')
        image_end = html_text.find('&quot;', image_start)
        item_image = html_text[image_start:image_end]

        # Replace currency and price
        html_info = html_info.replace('#CURRENCY', 'GBP')
        html_info = html_info.replace('#PRICE', item_price)

        # Add currency converted amount to the list
        total_price_list.append(float(item_price) * 1.77)

    # Navy Lumbar Pillows
    elif x == 2:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read xhtml file
        html_file = open('NavyLumbarPillows.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()

        # Find the location of the item tag
        start = 0
        for tag in range(3):
            item_tag = html_text.find('<item>', start)
            start = item_tag + 1
        
        # Find the name of the item
        name_start = html_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
        name_end = html_text.find("]]></title>", name_start)
        item_name = html_text[name_start:name_end]

        # Find the price of the item
        price_start = html_text.find('<price>$', item_tag) + len('<price>$')
        price_end = html_text.find('</price>', price_start)
        item_price = html_text[price_start:price_end]

        # Find the image of the item
        image_start = html_text.find('src="', item_tag) + len('src="')
        image_end = html_text.find('"', image_start)
        item_image = html_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'USD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add currency converted amount to the list
        total_price_list.append(float(item_price) * 1.32)

    # New Coats
    elif x == 3:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read web document
        web_page = urlopen("https://www.ebay.com.au/sch/i.html?&_nkw=coat&_sop=10&LH_BIN=1&_rss=1")
        web_text = web_page.read().decode('UTF-8')

        # Find the location of the item tag
        start = 0
        for tag in range(3):
            item_tag = web_text.find('<item>', start)
            start = item_tag + 1
        
        # Find the name of the item
        name_start = web_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
        name_end = web_text.find("]]></title>", name_start)
        item_name = web_text[name_start:name_end]

        # Find the price of the item
        price_start = web_text.find('<strong><b>AU $</b>', item_tag) + len('<strong><b>AU $</b>')
        price_end = web_text.find('</strong>', price_start)
        item_price = web_text[price_start:price_end]

        # Find the image of the item
        image_start = web_text.find('src="', item_tag) + len('src="')
        image_end = web_text.find('">', image_start)
        item_image = web_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'AUD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add amount to the list
        total_price_list.append(float(item_price))

    # Best Sellers in Musics
    elif x == 4:
        # Include the html items to Invoice html
        html_info.replace('<!--#ITEMS-->', html_items)
    
        # Open and read web document
        web_page = urlopen("https://www.amazon.com.au/gp/rss/bestsellers/music")
        web_text = web_page.read().decode('UTF-8')

        # Find the location of the item tag
        start = 0
        for tag in range(3):
            item_tag = web_text.find('<item>', start)
            start = item_tag + 1
        
        # Find the artist of the item
        artist_start = web_text.find('"riRssContributor">', item_tag) + len('"riRssContributor">')
        artist_end = web_text.find(' <span class="byLinePipe">', artist_start)
        item_artist = web_text[artist_start:artist_end]
        
        # Find the name of the item
        name_start = web_text.find("<title>", item_tag) + len("<title>")
        name_end = web_text.find("</title>", name_start)
        item_name = web_text[name_start:name_end] + ' - ' + item_artist

        # Find the price of the item
        price_start = web_text.find('<span class="price">$', item_tag) + len('<span class="price">$')
        price_end = web_text.find('</span><br />', price_start)
        item_price = web_text[price_start:price_end]

        # Find the image of the item
        image_start = web_text.find('<img src="', item_tag) + len('<img src="')
        image_end = web_text.find('"', image_start)
        item_image = web_text[image_start:image_end]

        # Replace currency
        html_info = html_info.replace('#CURRENCY', 'AUD')
        html_info = html_info.replace('#PRICE', '$' + item_price)

        # Add amount to the list
        total_price_list.append(float(item_price))

    # Replace items name and image
    html_info = html_info.replace('#NAME', item_name)
    html_info = html_info.replace('#IMAGE', item_image)
    

        
