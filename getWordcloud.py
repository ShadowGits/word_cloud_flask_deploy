
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image

import base64
import io


def text_to_wordcloud(text):
# show only 10 words in the wordcloud . 
    wordcloud = WordCloud(background_color = "white",width=480, height=480, max_words=30).generate(text) 
    
    # plot the WordCloud image  
    plt.figure() 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis("off") 
    plt.margins(x=0, y=0) 
    #plt.show() 




    # plt.plot([1, 2])
    # plt.title("test")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    im = Image.open(buf)
    image64=base64.b64encode(buf.read())


    buf.close()
    return str(image64)

# data = {}
# with open('some.gif', mode='rb') as file:
#     img = file.read()