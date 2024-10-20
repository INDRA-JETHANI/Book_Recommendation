from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
new = pickle.load(open('new.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Title'].values),
                           author=list(popular_df['Author'].values),
                           image=list(popular_df['Image_Url'].values),
                           votes=list(popular_df['Total_Rating_Count'].values),
                           rating=list(popular_df['Average_Rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = new[new['Title'] == user_input].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    items = []
    for i in distances[1:6]:
        item = []
        item.append(data.iloc[i[0]].Title)
        item.append(data.iloc[i[0]].Author)
        item.append(data.iloc[i[0]].Image_Url)
        items.append(item)


    print(items)

    return render_template('recommend.html',items=items)






if __name__ == '__main__':
    app.run(debug=True)