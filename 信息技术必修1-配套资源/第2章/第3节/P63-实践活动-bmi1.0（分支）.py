h = float(input("��������ߣ���λ���ף���"))
w = float(input("����������ֵ����λ��ǧ�ˣ���"))
bmi = round(w/(h*h),1)
if bmi <= 16.4:
    print("BMIֵΪ��",bmi,",���ڵ�����") 
elif bmi <= 23.2:
    print("BMIֵΪ��",bmi,",������������".format(bmi))
elif bmi < 26.4:
    print("BMIֵΪ��",bmi,",���ڳ���".format(bmi))
else:
    print("BMIֵΪ��",bmi,",���ڷ���".format(bmi))

