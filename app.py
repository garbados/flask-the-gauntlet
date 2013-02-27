from flask import Flask, render_template, Markup
import markdown, os

app = Flask(__name__)

# use README as content
with open('README.md', 'r') as f:
	content = Markup(markdown.markdown(f.read()))

@app.route('/')
def index():
	return render_template('index.html', 
		content=content,
		title="The Gauntlet")

if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		port=os.environ.get('PORT', 5000))