
#-----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the invoice file. To simplify marking, your program should
# generate its invoice using this file name.

##### Invoice HTML

invoice_html = """
<!DOCTYPE html>
<html>
<head>
<title>Bear's Cart Care</title>
<style>

.bar {
    background-color: slateblue;
    padding: 10px;
}

h1 {
    font-family: Impact;
    font-size: 350%
}

h2 {
    font-size: 200%;
    text-align: center;
}

.end {
    font-size: 80%;
    text-align: left;
    margin-left: 100px;
}

.price_box {
    height: auto;
    width: 600px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: 3px no-border;
    align-content: center;
    text-align: right;
}

.item_box {
    height: auto;
    width: 500px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: 8px ridge pink;
    align-content: center;
}

img {
    max-width: 500px
}

.total_box {
    padding: 20px;
    background-color: AliceBlue;
    width: 400px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: 5px outset lightblue;
    align-content: center;
}

.end_bar {
    height: 0px;
    width: 300px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: 2px dashed black;
    align-content: center;
}

.body_box {
    height: auto;
    width: 1000px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: no-border;
    align-content: center;
    text-align:center;
    font-size: 140%;
}

</style>
</head>

<body class="body_box">

<!-- Title and image -->
<h1>Bear's Cart Care Shopping</h1>
<img src="https://image.freepik.com/free-vector/happy-bear-with-trolley-mascot-design_35422-26.jpg" width="600">
<p>Thank you for shopping with Bear's Cart Care!</p>

<!--#INFO-->

<p><em>! Hope to see you again !</em></p>
<p class="end_bar"></p>

</body>
</html>

"""
# HTML code for invoice information
html_info = """
<!-- The total price of the items bought -->
<p class="total_box">Total amount: <b>$#TOTAL_PRICE <sub>AUD</sub></b></p>


<!-- List of items bought (name, image, price) -->
<!--#ITEMS-->

<p class="bar"></p>

<!-- URLs of where the items was retrieved from -->
<h3 class="end">Bargain items from:</h3>
<ul class="end">
  <li>https://www.etsy.com/au/shop/WishedForJewellery/rss </li>
  <li>https://feed.zazzle.com/rss?qs=navy+lumbar+pillows </li>
</ul>

<h3 class="end">New/Best Sellers items from:</h3>
<ul class="end">
  <li>https://www.ebay.com.au/sch/i.html?&_nkw=coat&_sop=10&LH_BIN=1&_rss=1 </li>
  <li>https://www.amazon.com/gp/rss/bestsellers/music </li>
</ul>
"""
# HTML code for added items
html_items = """
<p class="bar"></p>
<h2>#NAME</h2>
<p class="item_box"><img src="#IMAGE"></p>
<p class="price_box">Price: <b>#PRICE <sub>#CURRENCY</sub></b></p>

<!--#ITEMS-->
"""
# HTML code for no added items
html_no_buy = '<p>There are no items to print!</p>'

##### SQLite

# Connect to the shopping cart database
connection = connect('shopping_cart.db')
cursor = connection.cursor()

# Delete all rows in the database
delete_query = """
DELETE
FROM ShoppingCart
"""
cursor.execute(delete_query)
connection.commit()
cursor.close()
connection.close()

#query for adding values
add_query = """
INSERT INTO ShoppingCart
VALUES ('{}', '{}')
"""
queries = []

##### Program Codes

total_price_list = []
total_price = 0

def print_invoice():
    global invoice_html
    global html_info
    global html_no_buy
    global total_price
    global total_price_list
    global queries

    # Calculate the total price
    for total_aud in total_price_list:
        total_price = total_price + float(total_aud)
    total_price_list = []

    # If there are no items added
    if total_price == 0:
        invoice_html = invoice_html.replace('<!--#INFO-->', html_no_buy)
    # If there are items added
    else:
        html_info = html_info.replace('#TOTAL_PRICE', str("{0:.02f}".format(total_price)))
        invoice_html = invoice_html.replace('<!--#INFO-->', html_info)

    # Create text file with invoice html written in
    invoice_file = open('invoice.html', 'w', encoding = 'UTF-8')
    invoice_file.write(invoice_html)
    invoice_file.close()

    # Connect to the shopping cart database
    connection = connect('shopping_cart.db')
    cursor = connection.cursor()
        
    # Run the queries and add to the database
    for query in queries:
        cursor.execute(query)
    queries = []
    
    connection.commit()

    # Cloase the cursor and connection
    cursor.close()
    connection.close()


def get_list():
    x = v.get()

    # Covering the previous items list
    blind = Label(window, height=35, width=80)
    blind.grid(row=2, column=2, sticky=W)

    # Construct frame2
    frame2 = Frame(window, height=500, width=500, bd=1)
    frame2.grid(row=2, column=2, sticky=W)

    iframe2 = Frame(frame2, bd=4, relief=GROOVE)
    iframe2.grid(row=2, column=0, pady=20, padx=5, sticky=W)

    # Initial start and lists
    start = 0
    name_list = []
    price_list = []
    items_info = []

    # Wished For Jewellery
    if x == 1:
        # Open and read xhtml file
        html_file = open('WishedForJewellery.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()
        html_url = "https://www.etsy.com/au/shop/WishedForJewellery/rss"

        # Find info of 10 items and store in a list
        for info in range(10):
            # Find the name of the item
            item_tag = html_text.find('<item>', start)
            name_start = html_text.find("<title>", item_tag) + len("<title>")
            name_end = html_text.find("</title>", item_tag)
            item_name = html_text[name_start:name_end]
            name_list.append(item_name)

            # Find the price of the item
            price_start = html_text.find('class=&quot;price&quot;&gt;', item_tag) + len('class=&quot;price&quot;&gt;')
            price_end = html_text.find(' GBP&lt;/p&gt;', price_start)
            item_price = html_text[price_start:price_end]
            price_list.append(item_price + ' GBP')

            # Find the image of the item
            image_start = html_text.find('img src=&quot;', item_tag) + len('img src=&quot;')
            image_end = html_text.find('&quot;', image_start)
            item_image = html_text[image_start:image_end]

            start = name_end # Next item

            # Add item information to the list
            items_info.append(item_name)
            items_info.append(item_image)
            items_info.append(item_price)

    # Navy Lumbar Pillows
    elif x == 2:
        # Open and read xhtml file
        html_file = open('NavyLumbarPillows.xhtml', 'r', encoding='UTF-8')
        html_text = html_file.read()
        html_url = "https://feed.zazzle.com/rss?qs=navy+lumbar+pillows"

        # Find info of 10 items and store in a list
        for info in range(10):
            # Find the name of the item
            item_tag = html_text.find('<item>', start)
            name_start = html_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
            name_end = html_text.find("]]></title>", item_tag)
            item_name = html_text[name_start:name_end]
            name_list.append(item_name)

            # Find the price of the item
            price_start = html_text.find('<price>$', item_tag) + len('<price>$')
            price_end = html_text.find('</price>', price_start)
            item_price = html_text[price_start:price_end]
            price_list.append('$' + item_price)

            # Find the image of the item
            image_start = html_text.find('src="', item_tag) + len('src="')
            image_end = html_text.find('"', image_start)
            item_image = html_text[image_start:image_end]

            start = name_end # Next item

            # Add item information to the list
            items_info.append(item_name)
            items_info.append(item_image)
            items_info.append(item_price)

    # New Coats
    elif x == 3:
        # Open and read web document
        html_url = "https://www.ebay.com.au/sch/i.html?&_nkw=coat&_sop=10&LH_BIN=1&_rss=1"
        web_page = urlopen(html_url)
        web_text = web_page.read().decode('UTF-8')

        # Find info of 10 items and store in a list
        for info in range(10):
            # Find the name of the item
            item_tag = web_text.find('<item>', start)
            name_start = web_text.find("<title><![CDATA[", item_tag) + len("<title><![CDATA[")
            name_end = web_text.find("]]></title>", item_tag)
            item_name = web_text[name_start:name_end]
            name_list.append(item_name)

            # Find the price of the item
            price_start = web_text.find('<strong><b>AU $</b>', item_tag) + len('<strong><b>AU $</b>')
            price_end = web_text.find('</strong>', price_start)
            item_price = web_text[price_start:price_end]
            price_list.append('$' + item_price)

            # Find the image of the item
            image_start = web_text.find('src="', item_tag) + len('src="')
            image_end = web_text.find('">', image_start)
            item_image = web_text[image_start:image_end]

            start = name_end # Next item

            # Add item information to the list
            items_info.append(item_name)
            items_info.append(item_image)
            items_info.append(item_price)

    # Best Sellers in Musics
    elif x == 4:
        # Open and read web document
        html_url = "https://www.amazon.com.au/gp/rss/bestsellers/music"
        web_page = urlopen(html_url)
        web_text = web_page.read().decode('UTF-8')

        # Find info of 10 items and store in a list
        for info in range(10):
            # Find the artist of the item
            item_tag = web_text.find('<item>', start)
            artist_start = web_text.find('"riRssContributor">', item_tag) + len('"riRssContributor">')
            artist_end = web_text.find(' <span class="byLinePipe">', artist_start)
            item_artist = web_text[artist_start:artist_end]

            # Find the name of the item
            name_start = web_text.find("<title>", item_tag) + len("<title>")
            name_end = web_text.find("</title>", name_start)
            item_name = web_text[name_start:name_end] + ' - ' + item_artist
            name_list.append(item_name)

            # Find the price of the item
            price_start = web_text.find('<span class="price">$', item_tag) + len('<span class="price">$')
            price_end = web_text.find('</span><br />', price_start)
            item_price = web_text[price_start:price_end]
            price_list.append('$' + item_price)

            # Find the image of the item
            image_start = web_text.find('<img src="', item_tag) + len('<img src="')
            image_end = web_text.find('"', image_start)
            item_image = web_text[image_start:image_end]

            start = name_end # Next item

            # Add item information to the list
            items_info.append(item_name)
            items_info.append(item_image)
            items_info.append(item_price)

    # items_info = [name1, image1, price1, name2, image2, price2, name3, ...]

    def add_item(btn_no):
        global html_info
        global invoice_html
        global query

        # Change the invoice html so it can add items without exiting the GUI
        invoice_html = invoice_html.replace(html_no_buy, '<!--#INFO-->')
        invoice_html = invoice_html.replace(html_info, '<!--#INFO-->')
        html_info = html_info.replace('amount: <b>$'+str("{0:.02f}".format(total_price)),
                                      'amount: <b>$#TOTAL_PRICE')
        # Include the html items to html info
        html_info = html_info.replace('<!--#ITEMS-->', html_items)

        # Replace item name, image and price in html info
        html_info = html_info.replace('#NAME', items_info[0+(btn_no-1)*3])
        html_info = html_info.replace('#IMAGE', items_info[1+(btn_no-1)*3])
        if x == 1:
            html_info = html_info.replace('#PRICE', items_info[2+(btn_no-1)*3])
        else: # x == 2 or 3 or 4
            html_info = html_info.replace('#PRICE', '$' + items_info[2+(btn_no-1)*3])

        # Replace currency and add item price (in AUD) to the list
        if x == 1:
            html_info = html_info.replace('#CURRENCY', 'GBP')
            total_price_list.append(float(items_info[2+(btn_no-1)*3]) * 1.77)
        elif x == 2:
            html_info = html_info.replace('#CURRENCY', 'USD')
            total_price_list.append(float(items_info[2+(btn_no-1)*3]) * 1.32)
        else: # x == 3 or 4
            html_info = html_info.replace('#CURRENCY', 'AUD')
            total_price_list.append(float(items_info[2+(btn_no-1)*3]))

        # Add item name and price to SQLite query
        queries.append(add_query.format(items_info[0+(btn_no-1)*3], items_info[2+(btn_no-1)*3]))


    # Buttons for adding items to cart
    btn1 = Button(iframe2, text="Add #01", font=gui_font, command=lambda: add_item(1))
    btn1.grid(row=0, column=0, sticky=W)
    btn2 = Button(iframe2, text="Add #02", font=gui_font, command=lambda: add_item(2))
    btn2.grid(row=1, column=0, sticky=W)
    btn3 = Button(iframe2, text="Add #03", font=gui_font, command=lambda: add_item(3))
    btn3.grid(row=2, column=0, sticky=W)
    btn4 = Button(iframe2, text="Add #04", font=gui_font, command=lambda: add_item(4))
    btn4.grid(row=3, column=0, sticky=W)
    btn5 = Button(iframe2, text="Add #05", font=gui_font, command=lambda: add_item(5))
    btn5.grid(row=4, column=0, sticky=W)
    btn6 = Button(iframe2, text="Add #06", font=gui_font, command=lambda: add_item(6))
    btn6.grid(row=5, column=0, sticky=W)
    btn7 = Button(iframe2, text="Add #07", font=gui_font, command=lambda: add_item(7))
    btn7.grid(row=6, column=0, sticky=W)
    btn8 = Button(iframe2, text="Add #08", font=gui_font, command=lambda: add_item(8))
    btn8.grid(row=7, column=0, sticky=W)
    btn9 = Button(iframe2, text="Add #09", font=gui_font, command=lambda: add_item(9))
    btn9.grid(row=8, column=0, sticky=W)
    btn10 = Button(iframe2, text="Add #10", font=gui_font, command=lambda: add_item(10))
    btn10.grid(row=9, column=0, sticky=W)

    # Item names and prices
    lbl1 = Label(iframe2, text=name_list[0] + "   " + price_list[0],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl1.grid(row=0, column=1, padx=5, sticky=W)
    lbl2 = Label(iframe2, text=name_list[1] + "   " + price_list[1],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl2.grid(row=1, column=1, padx=5, sticky=W)
    lbl3 = Label(iframe2, text=name_list[2] + "   " + price_list[2],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl3.grid(row=2, column=1, padx=5, sticky=W)
    lbl4 = Label(iframe2, text=name_list[3] + "   " + price_list[3],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl4.grid(row=3, column=1, padx=5, sticky=W)
    lbl5 = Label(iframe2, text=name_list[4] + "   " + price_list[4],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl5.grid(row=4, column=1, padx=5, sticky=W)
    lbl6 = Label(iframe2, text=name_list[5] + "   " + price_list[5],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl6.grid(row=5, column=1, padx=5, sticky=W)
    lbl7 = Label(iframe2, text=name_list[6] + "   " + price_list[6],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl7.grid(row=6, column=1, padx=5, sticky=W)
    lbl8 = Label(iframe2, text=name_list[7] + "   " + price_list[7],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl8.grid(row=7, column=1, padx=5, sticky=W)
    lbl9 = Label(iframe2, text=name_list[8] + "   " + price_list[8],
                 wraplength=450, font=gui_font, justify=LEFT)
    lbl9.grid(row=8, column=1, padx=5, sticky=W)
    lbl10 = Label(iframe2, text=name_list[9] + "   " + price_list[9],
                  wraplength=450, font=gui_font, justify=LEFT)
    lbl10.grid(row=9, column=1, padx=5, sticky=W)

    lbl_url = Label(iframe2, text=html_url, wraplength=450,
                    font=('Arial', 10), justify=LEFT, fg="blue")
    lbl_url.grid(row=10, column=1, padx=20, sticky=W)

    # Hide the Image
    photo.grid_forget()



##### GUI

# Create window
window = Tk()

window.title("Bear's Cart Care")
##window.configure(background="white")

gui_font = ('Arial', 12)


# Title label
lbl_welcome = Label(window, text="WELCOME TO  ", font=('Impact', 20))
lbl_welcome.grid(row=0, column=0, padx=20)

lbl_title = Label(window, text="  Bear's Cart Care Shopping", font=('Impact', 40))
lbl_title.grid(row=0, column=1, columnspan=2, padx=(0, 30))

# Add separator below the title
separator3 = Frame(window, width=750, height=3, bd=3, relief=GROOVE)
separator3.grid(row=1, column=0, columnspan=3)

# Image on start of the window
file = PhotoImage(file="Trolleybear.png")
photo = Label(image=file)
photo.image = file
photo.grid(row=2, column=2, sticky=W)


###
# Construct frame1
frame1 = Frame(window, bd=1)
frame1.grid(row=2, column=0, columnspan=2, sticky=W)

iframe1 = Frame(frame1, bd=4, relief=GROOVE)

# Shops list in frame 1
v = IntVar()
rdo_jewellery = Radiobutton(iframe1,
                            text="Wished for Jewellery",
                            variable=v,
                            value=1,
                            font=gui_font,
                            command=get_list)
rdo_pillow = Radiobutton(iframe1,
                         text="Navy Lumbar Pillows",
                         variable=v,
                         value=2,
                         font=gui_font,
                         command=get_list)
rdo_coat = Radiobutton(iframe1,
                       text="New Coats",
                       variable=v,
                       value=3,
                       font=gui_font,
                       command=get_list)
rdo_music = Radiobutton(iframe1,
                        text="Best Sellers in Musics",
                        variable=v,
                        value=4,
                        font=gui_font,
                        command=get_list)

rdo_jewellery.grid(row=1, column=0, padx=15, sticky=W)
rdo_pillow.grid(row=2, column=0, padx=15, sticky=W)
rdo_coat.grid(row=5, column=0, padx=15, sticky=W)
rdo_music.grid(row=6, column=0, padx=15, sticky=W)

# Bargain and New/Best Seller label in frame 1
lbl_bargain = Label(iframe1, text="Bargain Items", font=('Arial', 14, 'bold'))
lbl_bargain.grid(row=0, column=0, sticky=W)

lbl_new = Label(iframe1, text="New/Best Sellers Items", font=('Arial', 14, 'bold'))
lbl_new.grid(row=4, column=0, sticky=W)

# Add separators in frame 1
separator1 = Frame(iframe1, width=230, height=3, bd=3, relief=GROOVE)
separator1.grid(row=3, column=0)

separator2 = Frame(iframe1, width=230, height=2, bd=3, relief=GROOVE)
separator2.grid(row=7, column=0)

# Print Invoice button in frame 1
btn_print = Button(iframe1,
                   text="Print Invoice",
                   font=('Arial', 14, 'bold'),
                   command=print_invoice)
btn_print.grid(row=8, column=0, pady=10)

# Place frame1
iframe1.grid(row=2, column=0, pady=10, padx=5)


mainloop()
