finalCostFloat = 0
finalWeightFloat = 0
deliveryCostFloat = 0
preDeliveryCostFloat = 0
terminateBoolean = False 

ordersInt = 0
finalTrackPriceFloat = 0

def ComputeAvgPrice():
    #Based on the information, the average price will be calculated for all orders
    avgCost = 0
    if ordersInt == 0:
        avgCost = 0
    else:
        avgCost = finalTrackPriceFloat / ordersInt
    return avgCost    
       
def CalcDeliveryCost(totalWeight):
    #Based on the weight total, the shipping cost will be calculated
    shipping = 0
    if(totalWeight <= 5):
        shipping = 3.5;
    elif(totalWeight <= 20):
        shipping = 10;
    else: shipping = 9.5 + (.1 * totalWeight)
    return shipping
        

def CalcOrderPricing(artichoke, carrots, beets):
    #Calculate the price of an order based on # of pounds of artichokes
    #carrots, and beets
    return (artichoke * 2.67) + (carrots * 1.49) + (beets * .67)

#There will be a continous loop as long as user wishes to input data
while terminateBoolean == False:
    artichokeFloat = float(input("Enter Artichoke pounds: "))
    carrotsFloat = float(input("Enter Carrot pounds: "))
    beetsFloat = float(input("Enter beets pounds: "))

#Discount Rate & Amount
    rateFloat = .05
    amountFloat = 0

    #Compute cost and total number of pounds
    finalCostFloat = CalcOrderPricing(artichokeFloat,carrotsFloat,beetsFloat)
    finalWeightFloat = artichokeFloat + carrotsFloat + beetsFloat

    #Determine if discount needs to be applied
    if(finalCostFloat > 100):
        amountFloat = rateFloat * finalCostFloat

    finalCostFloat = finalCostFloat - amountFloat
    preDeliveryCostFloat = finalCostFloat

    #Update the information that has been collected
    ordersInt += 1
    finalTrackPriceFloat = finalTrackPriceFloat + preDeliveryCostFloat

    #Here is where the shipping cost will be calculated
    shippingFloat = CalcDeliveryCost(finalWeightFloat)
    #Include the shipping cost
    finalCostFloat = finalCostFloat + shippingFloat

    print ("\n" + "Order Price: $",  '%.2f' %preDeliveryCostFloat)
    print ("Shipping Cost: $", '%.2f' %shippingFloat)
    print ("Total Order Cost: $", '%.2f' %finalCostFloat, "\n")

    print("Do you want to enter another order?")

    userResponse = input("If yes, enter 'Y', otherwise 'N' for no")

    #Based on the user response, the boolean will be altered
    if(userResponse == "Y"):
       terminateBoolean = False
    else:
       terminateBoolean = True
       avgOrdPriceFloat = ComputeAvgPrice()
       print ("\n" + "Total Price: $",  '%.2f' %finalTrackPriceFloat)
       print ("Number of orders: ", ordersInt)
       print("Average price per order: $", '%.2f' %avgOrdPriceFloat)


