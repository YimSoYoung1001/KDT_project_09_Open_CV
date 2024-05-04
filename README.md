# KDT_project_09_Open_CV

경북대학교 KDT(Korea Digital Training) 빅데이터 전문가 양성과정 5기 : OpenCV 5팀입니다

임소영 : [깃허브 링크](https://github.com/YimSoYoung1001)  
이화은 : [깃허브 링크](https://github.com/Skylee0310)  
손예림 : [깃허브 링크](https://github.com/osllzd)  
명노아 : [깃허브 링크](https://github.com/noah2397)

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

<hr/>

### 맡은 역할      

**1. 데이터 준비**    

- 크롬에서 크롤링한 사진 자료와 캐글에서 음식 및 강아지 관련 데이터를 활용하였습니다.

**2. 데이터 전처리 및 DataSet 및 DataLoader 생성**
    
- 전처리 순서     
  - 사진 크기를 (150, 150)으로 조정
  - tensor로 변형
  - 정규화 실시 (mean = 0.5, std = 0.5 로 실시)     

- Dataset 분리 
  - 비율은 train : valid : test = 0.7 : 0.1 : 0.2로 설정했습니다.  

- DataLoader 생성
  - 배치 사이즈는 10으로 설정하여 생성하였습니다.

**3. 모델 생성**    

- 전이학습을 실시하였습니다.   
- 사전학습된 모델 : Resnet18

**4. train, valid, test 함수 정의**    

- optimizer은 Adam으로 설정하였습니다.
- 손실함수는 BCELoss로 설정하였습니다.

**5. 모델 클래스와 함수들을 활용하여 학습 및 검증 실시**    

- scheduler 적용 : MultiStepLR    

**6. 성능 평가**     

- Loss, Accuracy, Precision, Recall, F1_score 값을 통해 성능 평가를 실시했습니다.

**7. Resnet 종류별 성능 비교**

- resnet34, resnet50, resnet101, resnet152를 이용하여 학습 후 각 모델 별 성능을 비교했습니다.      

**8. 모델 시연**   

- 새로운 외부 데이터를 활용하여 생성된 모델을 시연하였습니다.

