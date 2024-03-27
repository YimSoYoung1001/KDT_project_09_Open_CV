# _KDT05-OpenCV Project_

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

#### 개발환경

| 패키지 이름  | 버전   | 사용 커맨드(Version command) |
| ------------ | ------ | ---------------------------- |
| Python       | 3.8.18 | python --version             |
| jupyter      | 1.0.0  | pip show jupyter             |
| ipython      | 8.12.2 | pip show ipython             |
| notebook     | 7.0.6  | pip show notebook            |
| numpy        | 1.24.3 | pip show numpy               |
| pandas       | 2.0.3  | pip show pandas              |
| matplotlib   | 3.7.2  | pip show matplotlib          |
| skicit-learn | 1.3.0  | print(sklearn.**version**)   |

<hr/>

### KDT(Korea Digital Training)-OpenCV

<hr/>

#### 사용한 데이터 사이트

1. []()
<hr/>

###### 주제 : ????

- 목차

* 1. 주제 선정 배경
* 2. 전처리
  </hr>

###### 역할 분담

|          역할 | 참여인원 |
| ------------: | -------- |
|      주제선정 |          |
|          코딩 |          |
|          발표 |          |
|       git관리 |          |
|   Readme 작성 |          |
|      PPT 제작 |          |
| PPT 관리,병합 |          |

### 소주제 개요(개인 항목)

<details>
  <summary>
    임소영     

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

  </summary>
</details>




</hr>

<details>
  <summary>
    이화은 
  </summary>

</details>

</hr>

<details>
  <summary>
    명노아 
  </summary>

</details>

</hr>

<details>
  <summary>
    손예림 
  </summary>

</details>
<hr/>
