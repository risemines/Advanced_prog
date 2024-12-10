nb_people_ride=int(input("How many people need a ride?"))
nb_people_fit=int(input("How many people fit in one taxi?"))
nb_taxi=nb_people_ride // nb_people_fit
if nb_taxi % 2 ==0 :
  nb_taxi=nb_taxi+1
print("Number of taxis needed: {nb_taxi}")