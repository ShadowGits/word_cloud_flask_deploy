from flask import request
from flask_restful import Resource
from models import db, Image , ImageSchema


from getWordcloud import text_to_wordcloud


images_schema = ImageSchema(many=True)
image_schema = ImageSchema()

class ImageResource(Resource):
    def get(self):
        images = Image.query.all()
        images = images_schema.dump(images).data
        return {'status': 'success', 'data': images[-1]}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = image_schema.load(json_data)
        if errors:
            return errors, 422
        image = Image.query.filter_by(encoded_image=data['encoded_image']).first()
        # if image:
        #     return {'message': 'Image already exists'}, 400
        
        
        #text to wordlcloud
        encoded_image_received=text_to_wordcloud("Word Cloud is a data visualization technique used for representing text data in which the size of each word indicates its frequency or importance. Significant textual data points can be highlighted using a word cloud. Word clouds are widely used for analyzing data from social network websites.For generating word cloud in Python, modules needed are – matplotlib, pandas and wordcloud. To install these packages, run the following commands :")
        # image = Image(
        #     encoded_image=encoded_image_received
        #     )

        # db.session.add(image)
        # db.session.commit()

        result = image_schema.dump(image).data

        return { "status": 'success', 'data': encoded_image_received }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = image_schema.load(json_data)
        if errors:
            return errors, 422
        image = Image.query.filter_by(id=data['id']).first()
        if not image:
            return {'message': 'Image does not exist'}, 400
        image.name = data['encoded_image']
        db.session.commit()

        result = image_schema.dump(image).data

        return { "status": 'success', 'data': result }, 204
    
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = image_schema.load(json_data)
        if errors:
            return errors, 422
        image = Image.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = image_schema.dump(image).data

        return { "status": 'success', 'data': result}, 204
