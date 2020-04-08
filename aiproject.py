from experta import *


#This system is capable of diagnosing respiratory illnesses and 
# decide if someone is having just a common cold or flu. 
# The system requests the user to enter the symptoms as input and 
# it checks if the symptom is flu or common cold.
# Also, if the user enters less than 3 symptoms, it asks to enter more 
# symptoms to diagnose their state. Finally, it compares between flu and 
# cold counter to print the result.  

class FluOrCold(KnowledgeEngine):


    @DefFacts()
    def symptoms(self):
        yield Fact(action="flu_or_cold")

    #################
    #Cold Symptoms
    #Fever
    @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="no fever"),
             Fact(symptom="mild fever"),
             Fact(symptom="no temperature"),
             Fact(symptom="mild temperature"),
             Fact(symptom="no hyperthermia"),
             Fact(symptom="mild hyperthermia"),
             Fact(symptom="no pyrexia"),
             Fact(symptom="mild pyrexia")))
    def fever_cold(self):
       global cold_symptoms
       cold_symptoms +=1

    #Coughing
    @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="producing cough"),
             Fact(symptom="mucus cough")))
    def coughing_cold(self):
       global cold_symptoms
       cold_symptoms +=1

    #Nasal discharge
    @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="stuffy nose"),
             Fact(symptom="runny nose")))
    def nasal_discharge_cold(self):
       global cold_symptoms
       cold_symptoms +=1

    #Tiredness
    @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="mild tiredness"),
             Fact(symptom="mild fatigue"),
             Fact(symptom="mild exhaustion")))
    def tiredness_cold(self):
       global cold_symptoms
       cold_symptoms +=1

    #Headache
    @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="headache"),
           Fact(symptom="mild headache"),
           Fact(symptom="mild migraine"),
           Fact(symptom="mild head pain")), salience=0)
    def headache_cold(self):
       global cold_symptoms
       cold_symptoms +=1

    #Dizziness
    @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="no lightheadedness"),
            Fact(symptom="no syncope"),
            Fact(symptom="no fainting"),
            Fact(symptom="no dizziness")))
    def dizziness_flu(self):
       global cold_symptoms
       cold_symptoms +=1

    #Nausea
    @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="no nausea"),
            Fact(symptom="no vomiting"),
            Fact(symptom="no stomach upset"),
            Fact(symptom="no sickness"),
            Fact(symptom="no low appetite")))
    def nausea_cold(self):
       global cold_symptoms
       cold_symptoms +=1     


    #################
    #Cold Symptoms
    #Fever
    @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="high fever"),
            Fact(symptom="moderate fever"),
            Fact(symptom="high temperature"),
            Fact(symptom="moderate temperature"),
            Fact(symptom="high hyperthermia"),
            Fact(symptom="moderate hyperthermia"),
            Fact(symptom="high pyrexia"),
            Fact(symptom="moderate pyrexia")))
    def fever_flu(self):
       global flu_symptoms
       flu_symptoms +=1


    #Coughing
    @Rule(Fact(action='flu_or_cold'),
         Fact(symptom="dry cough"))
    def coughing_flu(self):
       global flu_symptoms
       flu_symptoms +=1


    #Nasal discharge
    @Rule(Fact(action='flu_or_cold'),
          Fact(symptom="runny nose"))
    def nasal_discharge_flu(self):
       global flu_symptoms
       flu_symptoms +=1

    #Tiredness
    @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="moderate tiredness"),
             Fact(symptom="severe tiredness"),
             Fact(symptom="moderate fatigue"),
             Fact(symptom="severe fatigue"),
             Fact(symptom="moderate exhaustion"),
             Fact(symptom="severe exhaustion")))
    def tiredness_flu(self):
       global flu_symptoms
       flu_symptoms +=1

    #Headache
    @Rule(Fact(action='flu_or_cold'),
        OR(Fact(symptom="headache"),
           Fact(symptom="moderate headache"),
           Fact(symptom="severe headache"),
           Fact(symptom="moderate migraine"),
           Fact(symptom="severe migraine"),
           Fact(symptom="moderate head pain"),
           Fact(symptom="severe head pain")), salience=1)
    def headache_flu(self):
       global flu_symptoms
       flu_symptoms +=1

    #Dizziness
    @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="lightheadedness"),
            Fact(symptom="syncope"),
            Fact(symptom="fainting"),
            Fact(symptom="dizziness")))
    def dizziness_flu(self):
       global flu_symptoms
       flu_symptoms +=1

    #Nausea
    @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="nausea"),
            Fact(symptom="vomiting"),
            Fact(symptom="stomach upset"),
            Fact(symptom="sickness"),
            Fact(symptom="low appetite")))
    def nausea_cold(self):
       global flu_symptoms
       flu_symptoms +=1

    #################
    #Common Symptoms
    #Sneezing
    @Rule(Fact(action='flu_or_cold'),
         Fact(symptom="sneezing"))
    def sneezing_cold_flu(self):
       global cold_symptoms
       cold_symptoms +=1
       global flu_symptoms
       flu_symptoms +=1


    #Sore Throat
    @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="pain throat"),
            Fact(symptom="throat sore"),
            Fact(symptom="sore throat")))
    def sore_throat_cold_flu(self):
       global cold_symptoms
       cold_symptoms +=1
       global flu_symptoms
       flu_symptoms +=1

          
##################################################33       
#Output
flu_symptoms =0
cold_symptoms =0
print("Please not the inputs aren't case sensitive")
print("\n Cold or Flu ".center(40, "*"))
print(" Note ".center(40, "*"))
print (" Enter one symptom in line ".center(40, "*"))
print ("Enter '''That's it''' to stop and show your state ".center(40, "*"))
name = input("Please enter you name : ")
print("Please enter your symptoms from the following {}".format(name))
print("Please note the following list are the examples and you need to enter any symptom like 'high fever' or 'no fever'")
print("Did you check any Fever : 'no/mild/moderate/high fever', 'mild fever', 'no/mild/moderate/high temperature, 'no/mild/moderate/high hyerthermia', 'no/mild/moderate/high thermia'")
print("You got any Cough : 'producing/mucus/dry cough")
print("How's your Nose : 'stuffy/runny nose' ")
print("How are you feeling : 'mild tiredness/fatigue/exhaustion'")
print("You got any Headache : 'mild headache/migraine/head pain'")
print("You feeling Dizzy : 'dizziness / no dizziness")
print("and so on")

engine = FluOrCold() #object created

i = 1
while(1):
    print("What is your symptom {}?".format(i))
    i += 1
    symptom = input()
    #Exit from loop if the input equal " that's it"
    if symptom.strip().lower() == "that's it":
      break
    engine.reset()  # Prepare the engine for the execution.
    engine.declare(Fact(symptom=symptom.strip().lower()))
    engine.run()  # Run it

#print(flu_symptoms)
#print(cold_symptoms)
#Check if user enter less than 3 symptoms      
if ((flu_symptoms < 3) and (cold_symptoms < 3)):
    print("Sorry, You must enter more symptoms {}".format(name))
#Cann't diagnose user state when the flu and cold symptoms are equal 
elif((flu_symptoms == cold_symptoms)):
    print("Sorry, This looks ambigous, your symptoms sound like both flu and the common cold. I Suggest you please visit a doctor. Take Care {}".format(name))
#If the flu counter greater than cold counter, then the user has flu
elif ((flu_symptoms >= 3) and (flu_symptoms > cold_symptoms)):
    print ("Okay might have flu, nothing to worry about {}, please visit your doctor for medication".format(name))
#If the cold counter greater than flu counter, then the user has cold
elif ((cold_symptoms >= 3) and (flu_symptoms < cold_symptoms)):
    print ("Well, Good news, this might be just a small common cold, haha, were you dusting you room today {} ? Anyways nothing to worry about, take an anti-histame and get some rest, take plenty of fluids and if the symptoms get worse or they still persist, please vist a doctor, Take care {}".format(name))



