import urllib.request
from bs4 import BeautifulSoup

print('When you enter the date -> 2021-04-01 like this')
start_date = input('Enter the start date you want to check the commit of members : ')
end_date = input('Enter the end date you want to check the commit of members : ')
not_commit_cnt = 0
members_id = ["lCan37", "soline013", "Bisu-tjdgus", "wjdwns", "Hayeon-Lee", "yeilin-dpfls", "gPdnjs", "KangDaegyeom", "youngbin218", "dn5772", "yuris99"]
members_name = ["지석훈", "심현솔", "조성현", "박정준", "이하연", "최예린", "신혜원", "강대겸", "기영빈", "신대니", "홍지훈"];

url = "https://github.com"
for i in range(0,11):
    member_url = url + "/" + members_id[i]
    res = urllib.request.urlopen(member_url)
    soup = BeautifulSoup(res, "html.parser")

    results = soup.select("div.position-relative svg g")

    for result in results:
        git_commit = result.select("rect")
        for j in range(1,6):
            date = git_commit[j]["data-date"]
            if date >= start_date and date <= end_date:
                if int(git_commit[j]["data-count"]) == 0:
                    not_commit_cnt += 1
                    #print(git_commit[j]["data-date"], git_commit[j]["data-count"])
            elif date > end_date:
                break;
    member_price = 0
    if 1 < not_commit_cnt <= 6:
        member_price = 2500 * 2 ** (not_commit_cnt - 2)
    elif not_commit_cnt >= 7:
        member_price = 50000
    print(members_name[i], ' No commit this month : ', not_commit_cnt, ' Your penalty... : ', member_price)
    not_commit_cnt = 0
