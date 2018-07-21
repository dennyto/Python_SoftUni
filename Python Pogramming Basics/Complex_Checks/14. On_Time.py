exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrive_time = arrive_hour * 60 + arrive_min

if exam_time == arrive_time or 0 < exam_time - arrive_time <= 30:
    print("On time")
    early_min = exam_time - arrive_time
    if early_min > 0:
        print(str(early_min) + " minutes before the start")
elif exam_time < arrive_time:
    print("Late")
    late_time = arrive_time - exam_time
    if late_time >= 60:
        late_hour = late_time // 60
        late_min = late_time % 60
        if late_min < 10:
            print(str(late_hour) + ":0" + str(late_min) + " hours after the start")
        else:
            print(str(late_hour) + ":" + str(late_min) + " hours after the start")
    else:
        late_min = arrive_time - exam_time
        print(str(late_min) + " minutes after the start")
else:
    print("Early")
    early_time = exam_time - arrive_time
    if early_time >= 60:
        early_hour = early_time // 60
        early_min = early_time % 60
        if early_min < 10:
            print(str(early_hour) + ":0" + str(early_min) + " hours before the start")
        else:
            print(str(early_hour) + ":" + str(early_min) + " hours before the start")
    else:
        late_min = exam_time - arrive_time
        print(str(late_min) + " minutes before the start")

