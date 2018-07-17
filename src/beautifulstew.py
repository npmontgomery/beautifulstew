from bs4 import BeautifulSoup

def xml_2_soup(input_file):
    try:
        with open(input_file) as file:
            data = file.read()
            data_unescaped = html.unescape(data)
            soup = BeautifulSoup(data_unescaped, "lxml")
            return soup
    except:
        logging.error('xml_soup_maker failed to open %s', input_file)
        pass

# makes soup out of input uri


def soup_maker(input_uri):
    # Opens html file, reads markup, and outputs soup
    with open(input_uri, 'r') as file:
        data = file.read()
    soup = BeautifulSoup(data, "lxml")
    return soup

def get_all_css(soup, target_tag, output_option):
    # Takes soup, and returns list of target tag items as either text or html markup
    output_list = []
    for tag in soup.find_all(class_=target_tag):
        node_name = tag.get('id')
        if output_option == True:
            output_list.append(tag)
            print(tag)
        else:
            output_list.append(tag.text)
            print(tag.text)
    print(output_list)
    return output_list
 

def get_img_src(soup, include_internal):
    # Finds img src links and adds to list, option to exclude internal links
    output_list = []
    for tag in soup.find_all('img'):
        source = tag['src']
        if include_internal == False:
            if 'http' in source:
                output_list.append(source)
            else:
                pass
        else:
            output_list.append(source)
    print(output_list)
    return output_list
