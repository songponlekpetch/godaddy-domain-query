# godaddy-domain-query
For query domain from Godaddy API

# Installation
1. ดาวน์โหลดโปรแกรม Docker Desktop https://www.docker.com/products/docker-desktop/
2. เปิดโปรเเกรม Docker Desktop
3. สร้างไฟล์ .env ใน folder project เเล้วใส่ค่า paramter ตามตัวอย่างในไฟล์ .env.example 
3. Run command ```docker-compose build``` ที่ folder ของ project เพื่อทำการ Build docker image
   
# Run command
1. ```docker-compose run --rm app python main.py show-columns``` เพื่อเเสดง columns ที่สามารถ filter ได้
2. ```docker-compose run --rm app python main.py show-domais``` เพื่อเเสดงข้อมูล domain
   - หากต้องการปรับ columns ที่เเสดงผล สามารถใส่ parameter เเบบนี้ได้ ```docker-compose run --rm app python main.py show-domais --columnes domain,expires```
   
