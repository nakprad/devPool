# devpool Project

# **วิธีการ RUN**
สามารถ run ได้ 2 แบบ คือ run บนเครื่อง local หรือ run บน google colab 

แต่วิธีการตังต่อไปนี้ขอแนะนำการ run บน เครื่อง local

**สิ่งที่ต้องเครียม**
1. Jupyter Notebook 
2. library pyspark และอื่นๆ เช่น math ,time ,numpy ,pandas 

**วิธีการ RUN**
1. เปิด jupyter notebook ขึ้นมา
![1](https://user-images.githubusercontent.com/37319352/166199556-468d5938-9285-40bf-abaf-68a35e2adfc8.png)
2. ทำการ New file (python 3 ipykernal) ขึ้นมาดังภาพ จะได้หน้าต่าง jupyter เปล่าๆ
![2](https://user-images.githubusercontent.com/37319352/166199665-d45ae4dc-7418-47fe-a45a-22bf952436af.PNG)
![3](https://user-images.githubusercontent.com/37319352/166199765-4d8c116a-9558-4c2e-aa92-3f7976bddaf6.PNG)
3. ทำการ copy code จาก folfer hat file devpool.ipynb ไปใส่ไว้ใน file ที่เราสร้างขึ้นใหม่ จากนั้นทำการ `shift + enter` เพื่อทำการ RUN คำสั่ง โดยเริ่มจากคำสั่งส่วนแรกเพื่อทำการ configและ spark ทำงาน

	![4](https://user-images.githubusercontent.com/37319352/166200922-ced89fa2-3e09-4ec6-991c-52d9e99fd15d.png)
	
4. กำหนด schema ของ data 
 	- ทำการ read file konn.csv +
 	- จากนั้นทำการตัด column ที่ไม่ใช้งานออก 
 	- ใช้คำสั่ง .collect() เพื่อดูผลลัพทธ์ทั้งหมด
![5](https://user-images.githubusercontent.com/37319352/166201464-262f62aa-5cdd-4c8d-bcf2-fc167f315b31.PNG)

5. เตรียมข้อมูลให้เพราะสำหรับการ run

	![6](https://user-images.githubusercontent.com/37319352/166201950-f2f15950-2837-475c-9acf-29933256bb08.PNG)
	
6. ทำการ run code ตามไฟล์ โดยผลลัพทธ์จะปรากฏด้านล่าง
	
	![7](https://user-images.githubusercontent.com/37319352/166202121-7162adff-25ff-436e-b5dc-e70e39d573bd.PNG)
7. code ส่วนสุดท้ายเป็นการ export to csv และทำการสรุปผล ผลการ Run จะถูก save ชื่อ output_konn_k5.csv
![8](https://user-images.githubusercontent.com/37319352/166202410-2ada787e-a1c4-4439-9b0a-3bbbffc9767b.PNG)
