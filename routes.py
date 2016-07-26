#Define octet list to iterate over
second_octet = range(1,10)
third_octet = range(1,255)
fourth_octet = range(1,255)

#open new file
setfile = open("set_route.set", "w")

# create nested loop for each octect
for i in second_octet:
  second_str = str(i)
  if second_str <= '254':
    for r in third_octet:
      third_str = str(r)
      if third_str <= '254':
        for t in fourth_octet:
          fourth_str = str(t)
# Write file to set_route.set
          setfile.write("set routing-options static route 1."+ second_str +"."+ third_str +"." + fourth_str + "/32 discard\n")
#Close + Write to file
setfile.close()
