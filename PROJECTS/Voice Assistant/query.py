import requests
import string
from lxml import html
from googlesearch.googlesearch import GoogleSearch
from bs4 import BeautifulSoup

# to search
# print(chatbot_query('how old is samuel l jackson'))

result = ''

def chatbot_query(query, index=0):
    fallback = 'Sorry, I cannot think of a reply for that.'

    try:
        response = GoogleSearch().search(query)
        for result in response.results:
            return result.getText()
        """
        page = requests.get(search_result_list[index])

        tree = html.fromstring(page.content)

        soup = BeautifulSoup(page.content, features="lxml")

        article_text = ''
        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            { ord(c): None for c in string.whitespace }
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback

        return result
        """
    except:
        if len(result) == 0: result = fallback
        return result

print(chatbot_query("Who is the 44th president of the united states"))