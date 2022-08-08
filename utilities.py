
from pickle import load
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from re import sub
from os import path, getcwd

# initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# defining dictionary of emojis
emojis = {
    ':)': 'smile', ':-)': 'sadsmile', ':>': 'smile', ':->': 'smile',';d': 'wink', ':-E': 'vampire', ':(': 'sad',
    ':-(': 'sad', ':<': 'sad', ':-<': 'sad', ':p': 'raspberry', ':O': 'suprised', ':-@': 'shocked', ':@': 'shocked',
    ':-$': 'confused', ':\\': 'annoyed', ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
    ':@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-O': 'yell', 'O.o': 'confused', '<(-_-)>': 'robot', 
    'd(-_-)b': 'dj',  ';)':'wink', ';-)': 'wink', 'O:-)': 'angel', 'O*-)': 'angel', '(:-D': 'gossip', '=^.^=': 'cat'
}
# defining set of stopwords
stopword = set(stopwords.words('english'))
path = path.join(getcwd(), 'models', 'pipeline.pkl')
print(path)
with open(path, 'rb') as f:
    pipeline = load(f)

def preprocess(text: str) -> str:

    url_pattern = r'(http://)[^ ]* | (https://)[^ ]* | (www\.)[^ ]*'
    user_pattern = '@[\s]+'
    alpha_pattern = '[^a-zA-Z0-9]'
    sequence_pattern = r'(.)\1\1+'
    sequence_replace_pattern = r'\1\1'

    text = text.lower()

    for emoji in emojis:
        text = text.replace(emoji, 'EMOJI' + emojis[emoji])
    text = sub(url_pattern, 'URL', text)
    text = sub(user_pattern, 'USER', text)
    text = sub(alpha_pattern, ' ', text)
    text = sub(sequence_pattern, sequence_replace_pattern, text)
    return " ".join([lemmatizer.lemmatize(word) for word in text.split() if len(word) > 1 and word not in stopword])

def predict(model, text: str) -> dict:
    prediction = model.predict([preprocess(text)])[0]

    prediction_label = {
        0: 'Negative',
        1: 'Positive'
    }
    return {
        'text': text,
        'prediction': int(prediction),
        'sentiment': prediction_label[prediction]
    }

def predict_pipeline(text: str) -> dict:
    return predict(pipeline, text)

if __name__ == '__main__':
    print(preprocess("@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D"))
    print("🚀")
    print(predict_pipeline("I love twitter"))
