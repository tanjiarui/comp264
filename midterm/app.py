import json
from chalice import Chalice
from translation_service import *

#####
# chalice app configuration
#####
app = Chalice(app_name='the reviews translator')
app.debug = True

#####
# services initialization
#####
translation_service = TranslationService()


#####
# RESTful endpoints
#####
@app.route('/reviews', methods=['POST'], cors=True)
def translate():
	"""processes texts to the translation service"""
	request_data = json.loads(app.current_request.raw_body)
	text = request_data['original_text'].replace('\t', '').split('\n')
	translated_lines = list()
	for line in text:
		if line == '':
			continue
		try:
			translated_line = translation_service.translate_text(line)
			translated_lines.append({
				'text': line,
				'translation': translated_line
			})
		except ValueError:
			translated_lines.append({
				'text': line,
				'translation': ValueError('Language not supported')
			})
	return translated_lines