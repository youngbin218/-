import urllib.request
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/check',methods=['POST'])
def check(start_date=None, end_date=None, cnt=None, penalty=None, git_id=None):
    if request.method != 'POST' and start_date == None and end_date == None:
        return render_template('main2.html', start_date=start_date, end_date=end_date, cnt=cnt, penalty=penalty, git_id=git_id)
    
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        git_id = request.form['git_id']
        
        not_commit_cnt = 0
        url = "https://github.com/" + git_id
        res = urllib.request.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")

        results = soup.select("div.position-relative svg g")

        for result in results:
            git_commit = result.select("rect")
            if git_commit[0]["data-date"] <= end_date:
                for j in range(1,6):
                    if start_date <= git_commit[j]["data-date"] <= end_date:
                        if int(git_commit[j]["data-count"]) == 0:
                            not_commit_cnt += 1
                    else:
                        break
            else:
                break
                    
        price = 0
        if 1 < not_commit_cnt <= 6:
            price = 2500 * 2 ** (not_commit_cnt - 2)
        elif not_commit_cnt >= 7:
            mprice = 50000
            
        cnt = not_commit_cnt
        penalty = price
    else:
        start_date = None
        end_date = None
        cnt = None
        penalty = None
        git_id = None
        
    return render_template('main2.html', start_date=start_date, end_date=end_date, cnt=cnt, penalty=penalty, git_id=git_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True)
