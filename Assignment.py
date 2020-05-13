import json


value = []

Large = 10 
XLarge = 20  
two_XLarge = 40 
four_XLarge = 80 
eight_XLarge = 160 
ten_XLarge = 320 


data_dict = {

    'New_York':{
    "Large": 120,
    'XLarge': 230,
    '2XLarge': 450,
    '4XLarge': 774,
    '8XLarge': 1400,
    '10XLarge': 2820
    },

     'India':{
    'Large': 140,
    'XLarge': 1,
    '2XLarge': 413,
    '4XLarge': 890,
    '8XLarge': 1300,
    '10XLarge': 2970
    },

     'China':{
    'Large': 110,
    'XLarge': 200,
    '2XLarge': 0,
    '4XLarge': 670,
    '8XLarge': 1180,
    '10XLarge': 0
    },

}

def Calculate():

    if total > ten_XLarge:
        while not (total == sum(value)):
            value.append(int(eight_XLarge))
            if sum(value) > total:
                value.pop()
                break

        # First Check 
        if sum(value) == total:
            print("You have reached the total in First_Check")

        # Now This step is to fill the remaining of the total with the next lowest value y
        else:
            #print(sum(value))
            while not (total == sum(value)):
                value.append(int(four_XLarge))
                if sum(value) > total:
                    value.pop()
                    break

        # Second Check 
        if sum(value) == total:
            print("You have reached the total in Second_Check")
            
        else:
            #print(sum(value))
            while not (total == sum(value)):
                value.append(int(two_XLarge))
                if sum(value) > total:
                    value.pop()
                    break

        # Third Check 
        if sum(value) == total: 
            print("You have reached the total in Third_Check")
            
        else:
            #print(sum(value))
            while not (total == sum(value)):
                value.append(int(XLarge))
                if sum(value) > total:
                    value.pop()
                    break

        # Fourth Check 
        if sum(value) == total: 
            print("You have reached the total in Fourth_Check")
            
        else:
            #print(sum(value))
            while not (total == sum(value)):
                value.append(int(Large))
                if sum(value) > total:
                    value.pop()
                    break

            # to find the total count used      
            total_ten_XLarge = 0
            total_eight_XLarge = 0
            total_four_XLarge = 0
            total_two_XLarge = 0
            total_XLarge = 0
            total_Large = 0

            for i in range(len(value)):
                if value[i] == ten_XLarge:
                    total_ten_XLarge += 1
                elif value[i] == eight_XLarge:
                    total_eight_XLarge += 1
                elif value[i] == four_XLarge:
                    total_four_XLarge += 1
                elif value[i] == two_XLarge:
                    total_two_XLarge += 1
                elif value[i] == XLarge:
                    total_XLarge += 1
                elif value[i] == Large:
                    total_Large += 1

                else:
                    None

        All_list = [total_Large,total_XLarge,total_two_XLarge,total_four_XLarge,total_eight_XLarge,total_ten_XLarge]

    # If the price of the required is less than the highest price of our product 
    # or if individual wants to buy the product in less scale
    if total <= ten_XLarge:

        while not (total == sum(value)):
            value.append(int(two_XLarge))
            if sum(value) > total:
                value.pop()
                break

        # First Check for second case 
        if sum(value) == total:
            print("You have reached the total in First_Check_less")

        else:
            while not (total == sum(value)):
                value.append(int(XLarge))
                if sum(value) > total:
                    value.pop()
                    break

        # Second Check for second case 
        if sum(value) == total:
            print("You have reached the total in Second_Check_less")

        else:
            while not (total == sum(value)):
                value.append(int(Large))
                if sum(value) > total:
                    value.pop()
                    break

        # to find the total count used      
        total_two_XLarge = 0
        total_XLarge = 0
        total_Large = 0

        for i in range(len(value)):
            if value[i] == two_XLarge:
                total_two_XLarge += 1
            elif value[i] == XLarge:
                total_XLarge += 1
            elif value[i] == Large:
                total_Large += 1

            else:
                return None

        # To Analyse the final Units of the Machines

        All_list = [total_Large,total_XLarge,total_two_XLarge]


    Machine_list = {'Large':0,'XLarge':0,'2XLarge':0,'4XLarge':0,'8XLarge':0,'10XLarge':0}
    key_1 = []
    Value_1 = []

    for i in range(len(All_list)):
        if All_list[i] != 0:
            asd = list(Machine_list.keys())[i]
            Unit_key = key_1.append(asd)
            Unit_Value = Value_1.append(All_list[i]) 


    Req_Machine = dict(zip(key_1,Value_1))  # Machine Count and The Unit Count
    print(Req_Machine)


    Region = [] # The Total Regions to be Listed

    for x,y in enumerate(data_dict.items()):
        region_from = list(data_dict.keys())[x]
        Region.append(region_from)

    #print(Region)

    Price = []
    for i in range(len(key_1)):
        for j in key_1:
            sas = list(data_dict.values())[i][j]
            Price.append(sas)

    # Price for countries with respect to their Machine required
    
    num  = len(key_1)
    New_York_Prices = Price[0:num] 
    India_Prices = Price[num:num*2]
    China_Prices = Price[num*2:num*3]
    # Total Price
    Prices_New_York_Units = []
    Prices_Indian_Units = []
    Prices_China_Units = []

    for i in range(len(Value_1)):
        P = Value_1[i]*New_York_Prices[i]*time
        Q = Value_1[i]*India_Prices[i]*time
        R = Value_1[i]*China_Prices[i]*time

        Prices_New_York_Units.append(P)
        Prices_Indian_Units.append(Q)
        Prices_China_Units.append(R)

    Total_Price = [sum(Prices_New_York_Units),sum(Prices_Indian_Units),sum(Prices_China_Units)]

    country = ['New_York','India','China']

    Country_New_York = {'New_York':{'Total_Cost':Total_Price[0],'Machine':Req_Machine}}
    Country_India = {'India':{'Total_Cost':Total_Price[1],'Machine':Req_Machine}}
    Country_China = {'China':{'Total_Cost':Total_Price[2],'Machine':Req_Machine}}

    
    final = [Country_New_York,Country_India,Country_China]
    
    print(json.dumps(final, indent = 4)) 

total = int(input("Enter the required Units:"))
time = int(input("Enter the required time:"))

Calculate()

