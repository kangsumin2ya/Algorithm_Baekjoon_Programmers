def solution(progresses, speeds):
    answer = []
    
    proceed_left = []
    deploy_day = []
    
    for i in range(len(progresses)):
        proceed_left.append(100-progresses[i])
    # print(proceed_left)
    
    for j in range(len(proceed_left)):
        if proceed_left[j] % speeds[j] == 0:
            deploy_day.append(int(proceed_left[j] / speeds[j]))
            
        else:
            deploy_day.append(int(proceed_left[j] / speeds[j])+1)
    print(deploy_day)
    
#     days = 1
#     for k in range(1, len(deploy_day)):
#         if deploy_day[k-1] > deploy_day[k]:
#             print(deploy_day[k-1])
#             days += 1

#         else:
#             answer.append(days)
#             print(f"Days:{days}")
#             days = 1
    while deploy_day:
        tmp = deploy_day.pop(0)
        count = 1
        
        while deploy_day and tmp >= deploy_day[0]:
            deploy_day.pop(0)
            count +=1 
        answer.append(count)
        
        
    return answer