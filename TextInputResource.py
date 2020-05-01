from flask import request
from flask_restful import Resource
from models import db, TextInput,TextInputSchema

text_inputs_schema = TextInputSchema(many=True)
text_input_schema = TextInputSchema()

class TextInputResource(Resource):
    def get(self):
        images = TextInput.query.all()
        images = images_schema.dump(images).data
        return {'status': 'success', 'data': images}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = image_schema.load(json_data)
        if errors:
            return errors, 422
        image = Text_Input.query.filter_by(encoded_image=data['encoded_image']).first()
        if image:
            return {'message': 'TextInput already exists'}, 400
        image = TextInput(
            encoded_image=json_data['encoded_image']
            )

        db.session.add(image)
        db.session.commit()

        result = image_schema.dump(image).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = image_schema.load(json_data)
        if errors:
            return errors, 422
        image = TextInput.query.filter_by(id=data['id']).first()
        if not image:
            return {'message': 'TextInput does not exist'}, 400
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
        image = TextInput.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = image_schema.dump(image).data

        return { "status": 'success', 'data': result}, 204
