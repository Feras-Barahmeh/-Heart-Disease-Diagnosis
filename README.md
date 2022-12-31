# Heart Diagnosis
This Fuzzy Logic In this study, a fuzzy system was designed to determine the risk of heart disease.
The system consists of _**24 rule bases**_ and has a **MISO** (Multi Input Single Output) 
system structure consisting of **_`6 inputs`_** - single outputs. 
Input values of the person; age, blood pressure, cholesterol, blood sugar, LDL and HDL values. 
The output value consists of the “**_`risk`_**” Fuzzy extraction engine and the center of gravity rinser.
The risk of heart disease is calculated by applying the necessary procedures to the information received from the user.

### The Rules Table
![1](Images/rules.png)

### Inputs

<img src="Images/age.png" width=49% height=50%/> <img src="Images/blood-pressure.png" width=49% height=10%/>
<img src="Images/cholestrol.png" width=49% height=10%/> <img src="Images/blood-sugar.png" width=49% height=10%/>
<img src="Images/LDL.png" width=49% height=10%/> <img src="Images/HDL.png" width=49% height=10%/>

### Risk 
[<img src="Images/risk.png" width=50% height=50%/>](Risk)


#### Test System

 **I tried our model with these data 👇 and It calculated Coroner Heart Diagnosis value is 3.5 .
 So in this example, this people has no risk for Coroner Heart Disease.**

 [<img src="Images/output.png" width=100% height=50%/>](Output)
 
**These Defuzzification are relative to the previous inputs 👆**

 [<img src="Images/defuzzification.png" width=100% height=50%/>](Defuzzification)


### Represent crisp and sense something _As Figure_
 [<img src="Images/crisb.png" width=100% height=50%/>](output)
 

# References
 * Matplotlib Python
   - https://matplotlib.org/
 * Numpy Python
   - https://numpy.org/
 * Skfuzzy Python
   - https://pythonhosted.org/scikit-fuzzy/
 * Fuzzy inference systems
   - https://www.cs.princeton.edu/courses/archive/fall07/cos436/HIDDEN/Knapp/fuzzy004.htm
 
# Good Videos Youtube

   1) 
      https://youtu.be/moQak7BXsI8
    
   2) Parts
      1) https://youtu.be/MQrDmU6Sn4s (part 1)
      2) https://youtu.be/MQrDmU6Sn4s (part 2)
