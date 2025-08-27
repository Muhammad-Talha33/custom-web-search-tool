from agents import  function_tool
from my_confg.tavily_confg import tavily_client


@function_tool
def web_search_tool(query:str):
    """This tool searches the web"""
    print("web_search_tool triggered ---->", "\n")
    lst = []
    response = tavily_client.search(query)
    r = response['results']
    for i in r:
     url = i['url']
     title = i['title']
     content = i['content']
     lst.append({"url": url, "title": title, "content": content})
    return lst


