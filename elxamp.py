import pandas as pd
original_data = pd.read_csv('googleplaystore.csv') #csv 파일 읽기
# original_data
#1. 선택된 feature로 새로운 데이터 프레임 생성
selected_data = original_data[['App', 'Category','Rating','Installs']]
# selected_data
#2. 이상한 값 빼서 새로 생성
selected_data = selected_data[selected_data.Category != '1.9']
# selected_data
#2. 중복행 제거
selected_data = selected_data.drop_duplicates()
# selected_data
#3. nan값 지우기
nan_drop_data = selected_data.dropna(how='any')
# nan_drop_data
#4. rating 평균 내기
rating_mean = "%0.1f" % nan_drop_data.Rating.mean()
# print(rating_mean)
#5. install 평균 내기
install = []
int_to_install = []

for ele in nan_drop_data.Installs:
    install.append(ele)
    
for ele in install:
    ele = ele.replace("," ,"")
    ele = ele.replace("+","")
    int_to_install.append(int(ele))
# print(int_to_install)
import numpy as np
install_mean = int(np.mean(int_to_install))
# print(install_mean)
selected_data = selected_data.replace({'Rating': np.nan},{'Rating' : rating_mean})
selected_data.replace({'Installs': np.nan},{'Installs' : install_mean})
install = []
int_to_install = []
for ele in selected_data.Installs:
    install.append(ele)
    
for ele in install:
    ele = ele.replace("," ,"")
    ele = ele.replace("+","")
    int_to_install.append(int(ele))
# print(int_to_install)
selected_data = selected_data.drop('Installs',1)
# selected_data
# 평균낸 값들로 2번 데이터 프레임에 추가
selected_data["Installs"] = int_to_install
# selected_data
rating = []
for ele in selected_data.Rating:
    rating.append(float(ele))
min_rating = min(rating)
max_rating = max(rating)
# print(rating)
normalization_rating = []
for ele in rating:
    normalization = (ele - min_rating) / (max_rating - min_rating)
    normalization_rating.append(normalization)
# print(normalization_rating)
installs = []
for ele in selected_data.Installs:
    installs.append(ele)
min_installs = min(installs)
max_installs = max(installs)
# print(min_installs, max_installs)
# print(installs)
normalization_installs = []
for ele in installs:
    normalization = (ele - min_installs) / (max_installs - min_installs)
    normalization_installs.append(normalization)
# print(normalization_installs)
#8. score 열 만들기
score = []
for rating, installs in zip(normalization_rating, normalization_installs):
    ele_score = (rating + installs) /2
    score.append(ele_score)
# print(score)
selected_data["Score"] = score
# selected_data
selected_data = selected_data.sort_values(by=['Score'], axis=0, ascending=False)
# selected_data
#9. category별로 score 순으로 정렬
category = set()
category_dict = {}
for i in selected_data.Category:
    category.add(i)
category = list(category)
for item in category:
    category_dict[item] = 0
# category_dict
for key in category_dict:
    category_dict[key] = selected_data[selected_data.Category == key]
# FINANCE = selected_data[selected_data.Category == 'FINANCE']
# type(FINANCE)
# category_dict
# for key in category_dict:
#     print(category_dict[key])
# print(category_dict['TOOLS'])
# category_dict['MEDICAL']
# category_dict_arr = {}
# for category in category_dict:
#     print('category : ', category)
#     category_dict_arr[category] = []
#     for index in category_dict[category].index:
#         category_dict_arr[category].append(category_dict[category].loc[index])
# arr1=[]
# arr1.append(category_dict_arr["FAMILY"][0].App)
# arr1.append(category_dict_arr["FAMILY"][0].Category)
# arr1.append(category_dict_arr["FAMILY"][0].Rating)
# arr1.append(category_dict_arr["FAMILY"][0].Installs)
# arr1.append(category_dict_arr["FAMILY"][0].Score)
# arr1.append(category_dict_arr["FAMILY"][1].App)
# arr1.append(category_dict_arr["FAMILY"][1].Category)
# arr1.append(category_dict_arr["FAMILY"][1].Rating)
# arr1.append(category_dict_arr["FAMILY"][1].Installs)
# arr1.append(category_dict_arr["FAMILY"][1].Score)
# arr1.extend([category_dict_arr["FAMILY"][0].App,category_dict_arr["FAMILY"][0].Category,category_dict_arr["FAMILY"][0].Rating,category_dict_arr["FAMILY"][0].Installs,category_dict_arr["FAMILY"][0].Score])
# print(arr1)
import tkinter
from tkinter import ttk
class pro():
    win = tkinter.Tk ()
    win.title("구글 플레이스토어 카테고리별 랭킹")
    win.geometry('800x600+100+100')
    label=tkinter.Label(win,text="",width=1000)
    def __init__(self):
        value=['HEALTH_AND_FITNESS','PRODUCTIVITY','WEATHER','VIDEO_PLAYERS','TRAVEL_AND_LOCAL','BUSINESS','PHOTOGRAPHY','DATING','FOOD_AND_DRINK','HOUSE_AND_HOME','EVENTS','PARENTING','TOOLS','MAPS_AND_NAVIGATION','COMMUNICATION','SPORTS','ART_AND_DESIGN','AUTO_AND_VEHICLES','LIBRARIES_AND_DEMO','SHOPPING','MEDICAL','SOCIAL','FINANCE','BEAUTY','COMICS','EDUCATION','NEWS_AND_MAGAZINES','PERSONALIZATION','LIFESTYLE','FAMILY','ENTERTAINMENT','GAME','BOOKS_AND_REFERENCE']
        self.combo = ttk.Combobox(self.win, width=20,  values=value)
        self.action=ttk.Button(self.win, text="검색", command=self.clickMe)
        self.action2=ttk.Button(self.win, text="초기화", command=self.removeMe)
    def clickMe(self):
        self.removeMe()
        self.label=tkinter.Label(self.win,text=category_dict[self.combo.get()].head())
        self.label.pack()
    def removeMe(self):
        self.label.forget()
    def start(self):
        self.combo.pack()
        self.action.pack()
        self.action2.pack()
        self.win.mainloop()
play=pro()
play.start()
# print(category_dict_arr["FAMILY"][0].App)
# print(category_dict_arr["FAMILY"][0].Category)
# print(category_dict_arr["FAMILY"][0].Rating)
# print(category_dict_arr["FAMILY"][0].Installs)
# print(category_dict_arr["FAMILY"][0].Score)

# for i in range(len(arr1)):
    # print(arr1[i],end="\t")
    # if(i!=0 and (i+1)%5==0):
        # print("")
# print("hello")