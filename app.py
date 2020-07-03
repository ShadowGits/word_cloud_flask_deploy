from flask import Flask, request, jsonify
from getWordcloud import text_to_wordcloud
#Init app

def  create_app():
    app=Flask(__name__)


    


    #GET IMAGE STRING
    @app.route("/Image",methods=["GET"])
    def get_image_string():

        string_tuple=text_to_wordcloud("")
        return jsonify({"image_string":string_tuple[0],
                    "image_string_invert":string_tuple[1],
                    "image_string_masked":string_tuple[2],
                    "image_string_invert_masked":string_tuple[3]})



    #Customised IMAGE STRING
    @app.route("/Image",methods=["POST"])
    def get_text_image_string():

        text=request.json['input_text']
        print(text)
        string_tuple=text_to_wordcloud(text)
        return jsonify({"image_string":string_tuple[0],
                    "image_string_invert":string_tuple[1],
                    "image_string_masked":string_tuple[2],
                    "image_string_invert_masked":string_tuple[3]})
    return app


#Run Server
if __name__=="__main__":
    create_app().run(debug=True)
    
