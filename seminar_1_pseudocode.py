def main():
    def intersection():
        going_straight = True
        going_right = True
        going_left = True
        protocols_breached = False
        Traffic_lights = input("Check traffic lights via sensors: ")
        right_of_way = ("Check if there is no cars to your right.")
        Obstacles = ("Check if there are any obstructions on the road.")
        pedestrian_present = ("Check if there are any pedestrians on the road.")
        road_anomalies_present = ("Check if there are any anomalies such as animals, branches ect.")
        speed = ("How fast the car is going.")
        stop_sign_present = False
        Turning_right_prohibited = ("Check if a sign is prohibiting from turning to the right.")
        Turning_left_prohibited =  ("Check if a sign is prohibiting from turning to the left.")
        open("Road_signs", "r")
        if Traffic_lights == "Yellow" and speed > 0:
            "Slow down until stopping"
            if speed <= 0:
                "Stop and wait the Green light."
        elif  Traffic_lights == "Red":
            if speed > 0:
                "Slow down until stopping"
            elif speed <= 0:
                "Wait until the light goes green"
        else: 
            Traffic_lights = "Green"
            while not continue_driving == True:
                if going_straight == True:
                    while not protocols_breached == True:
                        if right_of_way == False:
                            "wait for right of way"
                        elif Obstacles == True:
                            "wait for the road to clear up"
                        else:
                            "pass"
                            right_of_way = True
                            Obstacles = False
                            open('Going_forward', "r")
                            continue_driving = True
                elif going_right == True:
                    while not protocols_breached == True and Turning_right_prohibited == False:
                        if right_of_way == False:
                            "wait for right of way"
                        elif Obstacles == True:
                            "wait for the road to clear up"
                        else:
                            "pass"
                            right_of_way = True
                            Obstacles = False
                            open('Intersection_Going_right', "r")
                            continue_driving = True
                elif going_left == True and Turning_left_prohibited == False:
                    while not protocols_breached == True:
                        if right_of_way == False:
                            "wait for right of way"
                        elif Obstacles == True:
                            "wait for the road to clear up"
                        else:
                            "pass"
                            right_of_way = True
                            Obstacles = False
                            open('Intersection_Going_left', "r")
                            continue_driving = True
            if continue_driving == True:
                "Check Spatial Awareness"
                open("Road_sign_databank", "r")
                while not stop_sign_present == True:
                    "Pass"
                else:
                    "Stop"
                    while not obstructions_present == True:
                        if pedestrian_present == True:
                            obstructions_present = True
                        elif road_anomalies_present == True:
                            obstructions_present = True
                        else:
                            obstructions_present == False
                            "pass"
                            break
