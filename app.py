from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Replace with your OpenAI key
openai.api_key = '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'

premise = '''I will give you a concept.
You use the concept and provide a prompt for it.

Use the following examples as a guide:
Concept: A macro shot of a stempunk insect
Prompt: a close up of a bug with big eyes, by Andrei Kolkoutine, zbrush central contest winner, afrofuturism, highly detailed textured 8k, reptile face, cyber steampunk 8 k 3 d, c 4 d ”, high detail illustration, detailed 2d illustration, space insect android, with very highly detailed face, super detailed picture 
Concept: An orange pie on a wooden table
Prompt: a pie sitting on top of a wooden table, by Carey Morris, pexels contest winner, orange details, linen, high details!, gif, leafs, a pair of ribbed, 🦩🪐🐞👩🏻🦳, vivid attention to detail, navy, piping, warm sunshine, soft and intricate, lights on, crisp smooth lines, religious 
Concept: a close up shot of a plant with blue and golden leaves
Prompt: a close up of a plant with golden leaves, by Hans Schwarz, pexels, process art, background image, monochromatic background, bromeliads, soft. high quality, abstract design. blue, flax, aluminium, walking down, solid colours material, background artwork 

Do not write explanations. I will write you a concept and you’ll only reply the prompt of the concept.
prompt needs to be in English regardless of the language in which the concept is described.
you'll start with nothing.
When the picture is suit for Vertical plate，you will use --ar 2:3 at the end of the prompt.
When the picture is suit for Horizontal plate，you will use --ar 3:2 at the end of the prompt.


Now give me a prompt，the concept is'''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    concept = request.json.get('concept')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change engine type to 'gpt-3.5-turbo'
            messages=[
                {"role": "system", "content": premise},
                {"role": "user", "content": concept}
            ]
        )
        return jsonify(response['choices'][0]['message']['content'].strip())
    except Exception as e:
        return jsonify(str(e)), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
