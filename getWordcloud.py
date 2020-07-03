
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import cv2
import base64


def text_to_wordcloud(text):
    p='''Declarative visualization grammars can accelerate development, 
    facilitate retargeting across platforms, and allow language-level optimizations.
    However, existing declarative visualization languages are primarily concerned with 
    visual encoding, and rely on imperative event handlers for interactive behaviors. 
    In response, we introduce a model of declarative interaction design for data visualizations. 
    Adopting methods from reactive programming, we model low-level events as composable data 
    streams from which we form higher-level semantic signals. Signals feed predicates and scale 
    inversions, which allow us to generalize interactive selections at the level of item geometry
     into interactive queries over the data domain. Production rules then use these queries to manipulate
      the visualization’s appearance. To facilitate reuse and sharing, these constructs can be encapsulated 
      as named interactors: standalone, purely declarative specifications of interaction techniques. We 
      assess our model’s feasibility and expressivity by instantiating it with extensions to the Vega
       visualization grammar. Through a diverse range of examples, we demonstrate coverage over an established 
       taxonomy of visualization interaction techniques.We present Reactive Vega, a system architecture that
        provides the first robust and comprehensive treatment of declarative visual and interaction design for 
        data visualization. Starting fr'''
        
    if(text is "Check Data" or len(text)==0):
        text=p


    col = Image.open("mask4.jpg")
    gray = col.convert('L')

# Let numpy do the heavy lifting for converting pixels to pure black or white
    bw = np.asarray(gray).copy()

# Pixel range is 0...255, 256/2 = 128
    bw[bw < 128] = 0    # Black
    bw[bw >= 128] = 255 # White

# Now we put it back in Pillow/PIL land


    mask1=bw
    mask2=np.invert(mask1)

    imfile = Image.fromarray(mask1)

    imfile.save("mask.jpeg")

    imfile = Image.fromarray(mask2)

    imfile.save("mask_i.jpeg")

 
    wc = WordCloud(background_color="white", max_words=1000, mask=mask1,
               max_font_size=90,random_state=5)
    wc.generate(text)
    wc_i= WordCloud(background_color="white", max_words=1000, mask=mask2,
               max_font_size=90,random_state=5)
    wc_i.generate(text)
    wc.to_file("cloud.png")
    wc_i.to_file("cloud_invert.png")
    
    

    #masked AND images
    src1 = cv2.imread('cloud.png')
    src2 = cv2.imread('mask_i.jpeg')

    dst = cv2.bitwise_and(src1, src2)
 
    cv2.imwrite('cloud_masked.jpg', dst)
    
    #masked AND images
    src1 = cv2.imread('cloud_invert.png')
    src2 = cv2.imread('mask.jpeg')

    dst = cv2.bitwise_and(src1, src2)
 
    cv2.imwrite('cloud_invert_masked.jpg', dst)
    
    with open("cloud.png",'rb') as f:
        image64=base64.b64encode(f.read())
    image_string=image64.decode('utf-8')
    
    with open("cloud_invert.png",'rb') as f:
        image64=base64.b64encode(f.read())
    image_string_invert=image64.decode('utf-8')
    

    return (image_string,image_string_invert)


print(text_to_wordcloud("")[0][:10])