
def item_select(items, query):
    '''
    input:
    items -> dictionary of items, with id as the key and list of items as the value
    query -> list of 2 values
    output:
    item_name -> name of the item with higher confidence value, showing it drives the growth of the other item
    '''
    item_name = ""
    
    # Your Code Starts here
    # Find the confidence value for each item in the items dictionary
    confidence = {}
    for item_id, item_list in items.items():
        for item in item_list:
            if item not in confidence:
                confidence[item] = 0
            confidence[item] += 1 / len(item_list)
    print("Confidence values for items: {}".format(confidence))
            
    # Calculate the confidence value for the query items
    query_confidence = {}
    for item in query:
        if item in confidence:
            query_confidence[item] = confidence[item]
        else:
            query_confidence[item] = 0
    print("Confidence values for query items: {}".format(query_confidence))
            
    # Determine which item has the higher confidence value
    if len(query_confidence) == 2:
        if query_confidence[query[0]] > query_confidence[query[1]]:
            item_name = query[0]
        else:
            item_name = query[1]
    elif len(query_confidence) == 1:
        item_name = list(query_confidence.keys())[0]
    else:
        item_name = "No items found"        
    
    # Your Code Ends here
    return item_name


def item_select_2(items, query):
    '''
    input:
    items -> dictionary of items, with id as the key and list of items as the value
    query -> list of 2 values
    output:
    item_name -> name of the item with higher confidence value, showing it drives the growth of the other item
    '''
    item_name = ""
    
    # Your Code Starts here

    sup_A = 0
    sup_B = 0
    sup_AB = 0
    A = query[0]
    B = query[1]
    for id in items:
      if A in items[id] and B in items[id]:
        sup_AB += 1
        sup_A += 1
        sup_B += 1
      elif A in items[id]:
        sup_A += 1
      elif B in items[id]:
        sup_B += 1
      else:
        continue
    conf_AB = sup_AB/sup_A
    conf_BA = sup_AB/sup_B

    if conf_AB > conf_BA:
      item_name = A
    elif conf_AB < conf_BA:
      item_name = B 
    else:
      item_name = "same"
        
    
    # Your Code Ends here
    return item_name    
    

items = {"id1": ["Bread","Milk", "Butter"], "id2": ["Bread", "Eggs", "Butter"], "id3": ["Eggs", "Milk", "Cola", "Butter", "Beer"], "id4": ["Bread", "Beer"], "id5": ["Diapers", "Beer", "Shampoo", "Cola", "Bread"]}
query = ["Bread", "Butter"]

ret = item_select(items, query)
print("The item with higher confidence value is: {}".format(ret))


ret = item_select_2(items, query)
print("The item with higher confidence value is: {}".format(ret))