<h1># Movie-Recommender</h1>
<h2>A Movie Recommendation Engine</h2>

<ul>
    <li>
        Languages & Frameworks Used (Front-End):
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>Javascript</li>
            <li>Jinja Templates</li>
            <li>Bootstrap</li>
        </ul>
    </li>
    <li>
        Languages & Framework Used (Back-End):
        <ul>
            <li>Python</li>
            <li>Flask</li>
            <li>Jupyter Notebook</li>
        </ul>
    </li>
    <li>
        Dataset Used
        <ul>
            <li>
                <a href="https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata">Link</a>
            </li>
        </ul>
    </li>
</ul>

<h2>About</h2>
<p>
    Movie Recommendation Engine made for PS: 3 intrigued my interest in learning about Machine Learning and Data
    Management. So, I came up with my version of a search and recommendation engine implemented on many multiplatform
    streaming services such as Netflix,Amazon Prime and Spotify. Based on the <a href="https://www.geeksforgeeks.org/k-nearest-neighbours/">K nearest neighbours algorithm</a> and <a href="https://www.geeksforgeeks.org/timsort/">Timsort</a> , it finds
    similarities
    using the cosine values of the movie vectors created with the help of the tags. <a href="https://www.geeksforgeeks.org/cosine-similarity/">Cosine similarity</a> 
    is better over a larger dataset than Euclidean Distance or Manhattan Distance. With the use of <a href="https://www.geeksforgeeks.org/introduction-to-stemming/">stemming</a> , duplicated
    words were removed. The final dataset is provided in this drive link.
    <a href="https://drive.google.com/drive/folders/17PRpnE3fm0T-IPKFFhkcdKPQiwELrWmw?usp=sharing">LINK</a>
</p>

<h3>Additional Features</h3>
<ul>
    <li>
        Top Grosing Movies from around the world.
    </li>
    <li>
        Catered content based on search 
    </li>
    <li>
        Genre Filters
    </li>
</ul>


![image](https://user-images.githubusercontent.com/81302667/170853126-95e67b13-0f93-46a0-92de-3983c1ef0382.png)


<h2>Instructions</h2>

<h3>Pre-Requisites</h3>
<ul>
        <li>
            Install the requirements
        </li>
        <li>
            (Important) Get the similarity.pkl and interestSimilarity.pkl files from <a href="https://drive.google.com/drive/folders/17PRpnE3fm0T-IPKFFhkcdKPQiwELrWmw?usp=sharing">here</a>
        </li>
        <li>
            Follow the file structure to place the files.
        </li>  
</ul>

<h3>
    File Structure
</h3>

    |-app
        |-app
            |-__pychache__
            |-Engine
                    |-engine.py
                    |-filters.py
                    |-interest.py
                    |-popularity_engine.py
            |-static
                    |-css
                        |-main.css
                    |-scripts
                        |-script.js
            |-templates
                    |-main_template.html
                    |-index.html
            |-__init__.py
            |-pseudoDB.py
            |-views.py
        |-env
        |-Interests.pkl
        |-interestSimilarity.pkl
        |-movie_dict.pkl
        |-similarity.pkl
        |-app.py
 <h3>
  Installation
 </h3>
 
 
 pip install flask<br>
 $ source env/Scripts/activate <br>
 pip install -r requirements.txt


<br>
<h3>
Run with Bash
</h3>
$ export FLASK_APP=run.py
<br>
$ export FLASK_ENV=development
<br>
$ flask run
<br>
<br>
Note: The Engine.ipynb file contains the data modeling(not to be included in the main app).

<br>
<h3>References</h3>
<ul>
    <li>
        <a href="https://amt-lab.org/blog/2021/8/algorithms-in-streaming-services">Amt-Lab</a>
    </li>
    <li>
        <a href="https://drive.google.com/file/d/1J_I1SJhrfjwj8wHaNElozpnt1UKYsBM-/view?usp=sharing">Using Content Based Filtering</a>
    </li>
</ul>
