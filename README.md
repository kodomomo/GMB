# How to use

1. [GMB 페이스북 페이지](https://www.facebook.com/profile.php?id=100076381742807)에서 메시지 보내기 클릭
2. Secret으로 사용할 내용 전송
3. 아래와 같은 형식의 메시지가 반환될 때 까지 대기
<p align=center>
  
  <img width="500" alt="스크린샷 2023-02-20 오후 6 48 45" src="https://user-images.githubusercontent.com/80697064/220071073-6abbae38-f93f-42f4-acf5-24625173e759.png">

</p>

4. Event를 수신 받을 Repository로 이동    
5. Settings > Webhook > Add Webhook 순으로 클릭 

<p align=center>

https://user-images.githubusercontent.com/80697064/220069455-f883db99-2069-4205-a353-67dae55e3672.mov

</p>

6. 각 항목에 맞는 값 입력
  - `Payload URL` :: 전달 받은 Redirect URL
  - `Content Type` :: application/json 선택
  - `Secret` :: 전달 받은 Secret

7. 전달 받을 Event 선택
8. Active 활성화

----
- Special thanks to [MallyCrip](https://github.com/Mallycrip) about [random string](https://github.com/kodomomo/dsm-payments-util/blob/6bc0fd2d890ac2f98f010229381baefbcad4720e/generate_random_id.py#L2) 
