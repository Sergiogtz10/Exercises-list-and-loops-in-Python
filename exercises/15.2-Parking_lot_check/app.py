parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(dict):
  state = {}
  total_slots = 0
  available_slots = 0
  occupied_slots = 0

  for i in dict:
    for slot in i:
      total_slots += 1
      if slot == 2:
        available_slots += 1
      elif slot == 1:
        occupied_slots += 1
  state["total_slots"] = total_slots
  state["available_slots"] = available_slots
  state["occupied_slots"] = occupied_slots
  
  return state

print(get_parking_lot(parking_state))


