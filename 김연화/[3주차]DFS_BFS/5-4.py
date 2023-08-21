def recursive_function(i):
  if i == 100:
    return 
  print(i,"번째에서 ", i+1,"번째 호출")
  recursive_function(i+1)

recursive_function(1)
