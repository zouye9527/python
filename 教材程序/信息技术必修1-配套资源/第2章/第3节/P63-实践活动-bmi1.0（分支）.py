h = float(input("请输入身高（单位：米）："))
w = float(input("请输入体重值（单位：千克）："))
bmi = round(w/(h*h),1)
if bmi <= 16.4:
    print("BMI值为：",bmi,",属于低体重") 
elif bmi <= 23.2:
    print("BMI值为：",bmi,",属于正常体重".format(bmi))
elif bmi < 26.4:
    print("BMI值为：",bmi,",属于超重".format(bmi))
else:
    print("BMI值为：",bmi,",属于肥胖".format(bmi))

