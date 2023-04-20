import re
from urllib.parse import urljoin

## -- Task 2 -- ##


def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str = None,
) -> set:
    """Find all the url links in a html text using regex
    Arguments:
        html (str): html string to parse
    Returns:
        urls (set) : set with all the urls found in html text
    """
    # create and compile regular expression(s)

    """    
    anchor_pat = re.compile(r'<a[^>]+>', flags=re.IGNORECASE)
    url_pat = re.compile(r'href="([^"]+)"', flags=re.IGNORECASE)
    host_pat = re.compile(r'href="([^/]+)"', flags=re.IGNORECASE)  
    """

    # Finds every a-tag
    anchor_pat = re.compile(r'<a[\s]+[^>]+>', flags=re.IGNORECASE) 
    
    # Finds href and gets info between the quotes 
    url_pat = re.compile(r'href="([^"]*)"') 

    # Checking if href consists of hashtag
    frag_pat = re.compile(r'href="[^#].+"')

    #Hvis href inneholder 
    #containFrag_pat = re.compile(r'href=".+[^#].+"')

    # Finds href that starts with one /
    path_pat = re.compile(r'href="(\/{1}\w.+)"')

    # Finds href that starts with two /
    host_pat = re.compile(r'href="(\/{2}\w.+)"')

    urls = set()
    # 1. find all the anchor tags, then
    # 2. find the urls href attributes

    # Iterate through all anchor tags that matches with the pattern anchor_pat
    for anchor_tag in anchor_pat.findall(html):
        
        # Removes all fragment identifiers
        # In other words - all info from the hashtag and out will be removed
        anchor_tag = re.sub(r'(#.+)[^>]+', '"',anchor_tag)
        # Search for href in anchor tag   
        match = url_pat.search(anchor_tag)
        #print(anchor_tag)
        
        if match: #If we find a match we check the following
        
            # 1. If match starts with one /
            # If there is a match we add the base url to the match so we get a full url
            if path_pat.search(anchor_tag):
                url = base_url + match.group(1)
                urls.add(url.strip())
                continue 
            
            # 2. If there is a match where the href starts with two //
            # we add https: to the url we find
            if host_pat.search(anchor_tag):
                urls.add("https:" + match.group(1)) 
                continue
            
            #Check if there is any # in the match, if its not we add it to the url set
            if frag_pat.search(anchor_tag):
                urls.add(match.group(1))
                continue
            #urls.add(match.group(1))
        """
        if path_pat.search(anchor_tag):
            #print("******")
            #print("anchor", anchor_tag)
            #print("group(1)", match.group(1))
            url = base_url + match.group(1)
            #print("finished url", url)
            urls.add(url.strip())
            #print("[url]", url)
            #print("******")
            continue 
        
        if host_pat.search(anchor_tag):
            urls.add("https:" + match.group(1)) 
            continue
        
        if match and frag_pat.search(anchor_tag): #ser bort fra href som starter med "#"            
            #print(f'{match}\n')
            urls.add(match.group(1))
            #urls.update(match)
            continue
            
        """

        """

        Kanskje heller skrive:
        if match:
        
            if path_pat.search(anchor_tag):
                #print("******")
                #print("anchor", anchor_tag)
                #print("group(1)", match.group(1))
                url = base_url + match.group(1)
                #print("finished url", url)
                urls.add(url.strip())
                #print("[url]", url)
                #print("******")
                continue 
            
            if host_pat.search(anchor_tag):
                urls.add("https:" + match.group(1)) 
                continue
        
        urls.add(match.group(1))

        """
    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        
        output_file = open(output, "w")
        output_file.write(base_url)
        output_file.write(urls)  
        output_file.close()
        
    return urls

## -- Task 3 -- ##
def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    #Find all urls in the html text
    urls = find_urls(html)
    # Match for all urls containing "...wikipedia.org/wiki"
    pattern = re.compile(r'wikipedia.org/wiki')

    articles = set()

    #Iterating through all the urls
    for url in urls:
        #print(url)
        # Find matches that are all wiki articles
        # If we find 
        match = pattern.search(url)
        if match:
            articles.add(url)

    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        output_file = open(output, "w")
        #Writes one url per line in the file
        for url in articles: 
            output_file.write(url)
        output_file.close()
    
    return articles 
    

## Regex example
def find_img_src(html: str):
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attibute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        #print(img_tag)   
        # then, find the src attribute of the img, if any
        match = src_pat.search(img_tag)
        if match:
            src_set.add(match.group(1))
    return src_set